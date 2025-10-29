"""
SWORD Project interface for accessing biblical texts.

This module provides a clean interface to the PySword library for accessing
200+ Bible translations and original language texts through SWORD modules.
"""

import os
import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

try:
    from pysword.modules import SwordModules
    from pysword.bible import Bible
    PYSWORD_AVAILABLE = True
except ImportError:
    PYSWORD_AVAILABLE = False
    Bible = None  # Type hint placeholder when PySword not available
    SwordModules = None
    print("Warning: PySword not installed. Install with: pip install pysword")


@dataclass
class VerseReference:
    """Structured verse reference."""
    book: str
    chapter: int
    verse: int

    def __str__(self):
        return f"{self.book} {self.chapter}:{self.verse}"


@dataclass
class VerseText:
    """Verse text with metadata."""
    reference: VerseReference
    text: str
    module_name: str
    clean_text: str = ""  # Text with markup removed

    def __post_init__(self):
        if not self.clean_text:
            self.clean_text = self._clean_markup(self.text)

    @staticmethod
    def _clean_markup(text: str) -> str:
        """Remove OSIS/GBF/ThML markup from text."""
        # Remove XML-style tags
        text = re.sub(r'<[^>]+>', '', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        return text.strip()


class SWORDInterface:
    """
    Interface to SWORD Project modules via PySword.

    Provides methods for:
    - Discovering installed modules
    - Retrieving verse text
    - Searching for keywords
    - Accessing original language texts with markup
    """

    def __init__(self, sword_dir: Optional[str] = None):
        """
        Initialize SWORD interface.

        Args:
            sword_dir: Optional path to SWORD modules directory.
                      If None, uses PySword's auto-detection.
        """
        if not PYSWORD_AVAILABLE:
            raise ImportError(
                "PySword is required. Install with: pip install pysword"
            )

        self.sword_dir = sword_dir
        self.modules = SwordModules(sword_dir) if sword_dir else SwordModules()
        self._available_modules = None
        self._loaded_bibles = {}

    def discover_modules(self, refresh: bool = False) -> Dict[str, dict]:
        """
        Discover all available SWORD modules.

        Args:
            refresh: Force re-scan of modules directory

        Returns:
            Dictionary of module_name -> module_info
        """
        if self._available_modules is None or refresh:
            self._available_modules = self.modules.parse_modules()

        return self._available_modules

    def list_bible_modules(self) -> List[str]:
        """
        Get list of available Bible translation modules.

        Returns:
            List of module names (e.g., ['KJV', 'ESV', 'ASV'])
        """
        modules = self.discover_modules()
        # Filter for Bible modules (not commentaries, dictionaries, etc.)
        bible_modules = [
            name for name, info in modules.items()
            if info.get('category') == 'Biblical Texts'
        ]
        return sorted(bible_modules)

    def get_bible(self, module_name: str) -> Bible:
        """
        Load a specific Bible module.

        Args:
            module_name: Name of the SWORD module (e.g., 'KJV')

        Returns:
            PySword Bible object

        Raises:
            ValueError: If module not found
        """
        if module_name in self._loaded_bibles:
            return self._loaded_bibles[module_name]

        try:
            bible = self.modules.get_bible_from_module(module_name)
            self._loaded_bibles[module_name] = bible
            return bible
        except Exception as e:
            available = self.list_bible_modules()
            raise ValueError(
                f"Module '{module_name}' not found. "
                f"Available modules: {', '.join(available)}"
            ) from e

    def get_verse(
        self,
        module_name: str,
        book: str,
        chapter: int,
        verse: int,
        clean_markup: bool = True
    ) -> VerseText:
        """
        Retrieve a single verse.

        Args:
            module_name: SWORD module name (e.g., 'KJV')
            book: Book name (e.g., 'John', 'Genesis')
            chapter: Chapter number
            verse: Verse number
            clean_markup: Remove OSIS/GBF markup if True

        Returns:
            VerseText object with text and metadata

        Example:
            >>> sword = SWORDInterface()
            >>> verse = sword.get_verse('KJV', 'John', 3, 16)
            >>> print(verse.clean_text)
        """
        bible = self.get_bible(module_name)

        result = bible.get(
            books=[book],
            chapters=[chapter],
            verses=[verse]
        )

        reference = VerseReference(book, chapter, verse)

        if result and len(result) > 0:
            # PySword returns list of verse data
            verse_data = result[0]
            text = verse_data.get('text', '')
            return VerseText(reference, text, module_name)
        else:
            # Verse not found
            return VerseText(reference, "", module_name)

    def get_verses(
        self,
        module_name: str,
        book: str,
        chapter: Optional[int] = None,
        verses: Optional[List[int]] = None,
        clean_markup: bool = True
    ) -> List[VerseText]:
        """
        Retrieve multiple verses from a book.

        Args:
            module_name: SWORD module name
            book: Book name
            chapter: Optional specific chapter
            verses: Optional list of specific verses
            clean_markup: Remove markup if True

        Returns:
            List of VerseText objects

        Example:
            >>> # Get all of John 3
            >>> verses = sword.get_verses('KJV', 'John', chapter=3)
            >>> # Get John 3:16-17
            >>> verses = sword.get_verses('KJV', 'John', chapter=3, verses=[16, 17])
        """
        bible = self.get_bible(module_name)

        # Build query parameters
        kwargs = {'books': [book]}
        if chapter is not None:
            kwargs['chapters'] = [chapter]
        if verses is not None:
            kwargs['verses'] = verses

        results = bible.get(**kwargs)

        verse_texts = []
        for verse_data in results:
            # Parse reference from result
            ref_match = re.match(
                r'(\w+)\s+(\d+):(\d+)',
                verse_data.get('reference', '')
            )
            if ref_match:
                book_name, chap, ver = ref_match.groups()
                reference = VerseReference(book_name, int(chap), int(ver))
                text = verse_data.get('text', '')
                verse_texts.append(VerseText(reference, text, module_name))

        return verse_texts

    def search_keyword(
        self,
        module_name: str,
        keyword: str,
        book: Optional[str] = None
    ) -> List[VerseText]:
        """
        Search for keyword in Bible text.

        Args:
            module_name: SWORD module name
            keyword: Word or phrase to search for
            book: Optional book name to limit search

        Returns:
            List of matching verses

        Example:
            >>> results = sword.search_keyword('KJV', 'sin', book='Romans')
        """
        bible = self.get_bible(module_name)

        # Get all verses from target book(s)
        if book:
            verses = self.get_verses(module_name, book)
        else:
            # Would need to iterate all books - expensive operation
            # For now, require book specification
            raise ValueError("Must specify book for keyword search")

        # Filter verses containing keyword (case-insensitive)
        keyword_lower = keyword.lower()
        matching = [
            v for v in verses
            if keyword_lower in v.clean_text.lower()
        ]

        return matching

    def get_structure_info(self, module_name: str) -> Dict[str, any]:
        """
        Get information about Bible structure in this module.

        Returns:
            Dictionary with books, chapter counts, etc.
        """
        bible = self.get_bible(module_name)

        # PySword Bible objects have a 'books' attribute
        books = bible.books if hasattr(bible, 'books') else []

        return {
            'module_name': module_name,
            'books': books,
            'book_count': len(books)
        }


# Utility functions for reference parsing

def parse_reference(ref_string: str) -> Optional[Tuple[str, int, int]]:
    """
    Parse a verse reference string.

    Args:
        ref_string: Reference like "John 3:16" or "Genesis 1:1"

    Returns:
        Tuple of (book, chapter, verse) or None if invalid

    Example:
        >>> parse_reference("John 3:16")
        ('John', 3, 16)
    """
    # Match patterns like "John 3:16" or "1 John 3:16"
    match = re.match(
        r'^(\d?\s*\w+)\s+(\d+):(\d+)$',
        ref_string.strip()
    )
    if match:
        book = match.group(1).strip()
        chapter = int(match.group(2))
        verse = int(match.group(3))
        return (book, chapter, verse)
    return None


def format_reference(book: str, chapter: int, verse: int) -> str:
    """
    Format a verse reference.

    Args:
        book: Book name
        chapter: Chapter number
        verse: Verse number

    Returns:
        Formatted string like "John 3:16"
    """
    return f"{book} {chapter}:{verse}"


# Module-level convenience instance
_default_sword = None


def get_default_sword() -> SWORDInterface:
    """Get or create the default SWORD interface instance."""
    global _default_sword
    if _default_sword is None:
        _default_sword = SWORDInterface()
    return _default_sword


if __name__ == '__main__':
    # Simple test/demo
    print("SWORD Interface Demo")
    print("=" * 50)

    try:
        sword = SWORDInterface()
        modules = sword.list_bible_modules()
        print(f"\nFound {len(modules)} Bible modules:")
        for mod in modules[:10]:  # Show first 10
            print(f"  - {mod}")

        if modules:
            # Try to get a verse from first available module
            test_module = modules[0]
            print(f"\nTesting with module: {test_module}")

            verse = sword.get_verse(test_module, 'John', 3, 16)
            print(f"\n{verse.reference}: {verse.clean_text}")

    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure PySword is installed: pip install pysword")
        print("And SWORD modules are installed (run: installmgr -init)")
