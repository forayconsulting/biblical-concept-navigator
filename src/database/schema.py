"""
Database schema for Biblical Concept Navigator.

This module defines the SQLAlchemy ORM models for storing biblical texts,
morphology, manuscripts, cross-references, and analytical data across
six research dimensions.
"""

from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    Table,
    Float,
    Boolean,
    DateTime,
    Index,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


# Many-to-many relationship tables
verse_cross_references = Table(
    'verse_cross_references',
    Base.metadata,
    Column('source_verse_id', Integer, ForeignKey('verses.id')),
    Column('target_verse_id', Integer, ForeignKey('verses.id')),
    Column('weight', Float, default=1.0),  # Strength of connection
)


class Manuscript(Base):
    """Represents different biblical manuscript traditions."""

    __tablename__ = 'manuscripts'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    tradition = Column(String(50))  # MT, LXX, Peshitta, Vulgate, DSS, etc.
    language = Column(String(20))  # Hebrew, Greek, Aramaic, Latin, etc.
    date_earliest = Column(Integer)  # Earliest estimated date (BCE/CE)
    date_latest = Column(Integer)  # Latest estimated date
    description = Column(Text)
    source_url = Column(String(500))

    verses = relationship('Verse', back_populates='manuscript')

    def __repr__(self):
        return f"<Manuscript(name='{self.name}', tradition='{self.tradition}')>"


class Book(Base):
    """Biblical books (66 canonical + apocrypha)."""

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    abbreviation = Column(String(10), nullable=False)
    testament = Column(String(10))  # OT, NT, Apocrypha
    order = Column(Integer)  # Canonical order
    chapters = Column(Integer)  # Number of chapters

    verses = relationship('Verse', back_populates='book')
    source_assignments = relationship('SourceAssignment', back_populates='book')

    __table_args__ = (
        Index('idx_book_abbrev', 'abbreviation'),
    )

    def __repr__(self):
        return f"<Book(name='{self.name}', testament='{self.testament}')>"


class Verse(Base):
    """Individual verse text across different manuscripts."""

    __tablename__ = 'verses'

    id = Column(Integer, primary_key=True)
    manuscript_id = Column(Integer, ForeignKey('manuscripts.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    chapter = Column(Integer, nullable=False)
    verse = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    transliteration = Column(Text)  # Romanized text for non-Latin scripts

    manuscript = relationship('Manuscript', back_populates='verses')
    book = relationship('Book', back_populates='verses')
    word_occurrences = relationship('WordOccurrence', back_populates='verse')

    # Self-referential many-to-many for cross-references
    cross_references = relationship(
        'Verse',
        secondary=verse_cross_references,
        primaryjoin=id == verse_cross_references.c.source_verse_id,
        secondaryjoin=id == verse_cross_references.c.target_verse_id,
    )

    __table_args__ = (
        Index('idx_verse_ref', 'book_id', 'chapter', 'verse'),
        Index('idx_verse_manuscript', 'manuscript_id'),
    )

    def __repr__(self):
        return f"<Verse({self.book.abbreviation} {self.chapter}:{self.verse})>"


class Lemma(Base):
    """Root words/lemmas in original languages."""

    __tablename__ = 'lemmas'

    id = Column(Integer, primary_key=True)
    word = Column(String(100), nullable=False)  # Original script
    transliteration = Column(String(100))  # Romanized
    language = Column(String(20), nullable=False)  # Hebrew, Greek, Aramaic
    strongs_number = Column(String(10))  # H1234 or G1234 format
    definition = Column(Text)
    etymology = Column(Text)
    semantic_domain = Column(String(100))

    word_occurrences = relationship('WordOccurrence', back_populates='lemma')

    __table_args__ = (
        Index('idx_lemma_strongs', 'strongs_number'),
        Index('idx_lemma_word', 'word'),
    )

    def __repr__(self):
        return f"<Lemma(word='{self.word}', strongs='{self.strongs_number}')>"


class WordOccurrence(Base):
    """Specific occurrences of words in verses with morphology."""

    __tablename__ = 'word_occurrences'

    id = Column(Integer, primary_key=True)
    verse_id = Column(Integer, ForeignKey('verses.id'), nullable=False)
    lemma_id = Column(Integer, ForeignKey('lemmas.id'), nullable=False)
    word_position = Column(Integer)  # Position in verse (1-indexed)
    word_form = Column(String(100))  # Inflected form
    morphology_code = Column(String(50))  # Standardized morphology code

    # Parsed morphological features
    part_of_speech = Column(String(20))
    person = Column(String(10))
    gender = Column(String(10))
    number = Column(String(10))
    tense = Column(String(20))
    voice = Column(String(20))
    mood = Column(String(20))
    case = Column(String(20))

    verse = relationship('Verse', back_populates='word_occurrences')
    lemma = relationship('Lemma', back_populates='word_occurrences')

    __table_args__ = (
        Index('idx_word_verse', 'verse_id'),
        Index('idx_word_lemma', 'lemma_id'),
    )

    def __repr__(self):
        return f"<WordOccurrence(form='{self.word_form}', lemma='{self.lemma.word}')>"


class SourceAssignment(Base):
    """Documentary Hypothesis (JEPD) source assignments."""

    __tablename__ = 'source_assignments'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    chapter_start = Column(Integer, nullable=False)
    verse_start = Column(Integer, nullable=False)
    chapter_end = Column(Integer)
    verse_end = Column(Integer)

    source = Column(String(10))  # J, E, D, P, R, etc.
    confidence = Column(Float)  # 0.0 to 1.0
    scholar_source = Column(String(200))  # Attribution (e.g., "Friedman 2003")
    notes = Column(Text)

    # Dating information
    date_earliest = Column(Integer)  # Estimated composition date (BCE/CE)
    date_latest = Column(Integer)
    consensus_date = Column(Integer)

    book = relationship('Book', back_populates='source_assignments')

    __table_args__ = (
        Index('idx_source_book', 'book_id'),
        Index('idx_source_type', 'source'),
    )

    def __repr__(self):
        return f"<SourceAssignment(source='{self.source}', book='{self.book.name}')>"


class Concept(Base):
    """Biblical concepts and themes (e.g., 'Sin', 'Covenant', 'Grace')."""

    __tablename__ = 'concepts'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    category = Column(String(50))  # Theological, ethical, ritual, etc.

    concept_occurrences = relationship('ConceptOccurrence', back_populates='concept')
    metaphors = relationship('Metaphor', back_populates='concept')
    remedies = relationship('Remedy', back_populates='concept')

    def __repr__(self):
        return f"<Concept(name='{self.name}')>"


class ConceptOccurrence(Base):
    """Links concepts to specific verses where they appear."""

    __tablename__ = 'concept_occurrences'

    id = Column(Integer, primary_key=True)
    concept_id = Column(Integer, ForeignKey('concepts.id'), nullable=False)
    verse_id = Column(Integer, ForeignKey('verses.id'), nullable=False)
    word_occurrence_id = Column(Integer, ForeignKey('word_occurrences.id'))

    # Detection metadata
    detection_method = Column(String(50))  # manual, keyword, semantic, etc.
    confidence = Column(Float)

    concept = relationship('Concept', back_populates='concept_occurrences')
    verse = relationship('Verse')
    word_occurrence = relationship('WordOccurrence')

    __table_args__ = (
        Index('idx_concept_verse', 'concept_id', 'verse_id'),
    )


class Metaphor(Base):
    """Metaphors and analogies used to describe concepts."""

    __tablename__ = 'metaphors'

    id = Column(Integer, primary_key=True)
    concept_id = Column(Integer, ForeignKey('concepts.id'), nullable=False)
    verse_id = Column(Integer, ForeignKey('verses.id'), nullable=False)

    metaphor_type = Column(String(50))  # simile, metaphor, personification, etc.
    source_domain = Column(String(100))  # What it's compared to (e.g., "stain")
    description = Column(Text)

    concept = relationship('Concept', back_populates='metaphors')
    verse = relationship('Verse')

    def __repr__(self):
        return f"<Metaphor(concept='{self.concept.name}', type='{self.metaphor_type}')>"


class Remedy(Base):
    """Proposed remedies or solutions for concepts (especially negative ones)."""

    __tablename__ = 'remedies'

    id = Column(Integer, primary_key=True)
    concept_id = Column(Integer, ForeignKey('concepts.id'), nullable=False)
    verse_id = Column(Integer, ForeignKey('verses.id'), nullable=False)

    remedy_type = Column(String(50))  # sacrifice, repentance, forgiveness, etc.
    description = Column(Text)
    theological_framework = Column(String(100))

    concept = relationship('Concept', back_populates='remedies')
    verse = relationship('Verse')

    def __repr__(self):
        return f"<Remedy(concept='{self.concept.name}', type='{self.remedy_type}')>"


class ExtraBiblicalReference(Base):
    """References to concept words in extra-biblical literature."""

    __tablename__ = 'extra_biblical_references'

    id = Column(Integer, primary_key=True)
    lemma_id = Column(Integer, ForeignKey('lemmas.id'), nullable=False)

    corpus = Column(String(50))  # CAL, Perseus, ORACC, Sefaria, etc.
    source_text = Column(String(200))  # Specific work/document
    citation = Column(String(200))  # Location within source
    context = Column(Text)  # Surrounding text
    translation = Column(Text)

    language = Column(String(20))
    date_estimated = Column(Integer)
    url = Column(String(500))

    lemma = relationship('Lemma')

    __table_args__ = (
        Index('idx_extra_biblical_lemma', 'lemma_id'),
        Index('idx_extra_biblical_corpus', 'corpus'),
    )

    def __repr__(self):
        return f"<ExtraBiblicalRef(corpus='{self.corpus}', source='{self.source_text}')>"


class ImportLog(Base):
    """Track data imports and updates."""

    __tablename__ = 'import_logs'

    id = Column(Integer, primary_key=True)
    import_type = Column(String(50), nullable=False)  # morphhb, strongs, etc.
    status = Column(String(20))  # success, failed, partial
    records_imported = Column(Integer)
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)
    error_message = Column(Text)
    import_metadata = Column(Text)  # JSON string with additional info

    def __repr__(self):
        return f"<ImportLog(type='{self.import_type}', status='{self.status}')>"


# Database initialization function
def init_db(database_url='sqlite:///data/processed/biblical_navigator.db'):
    """Initialize the database and create all tables."""
    engine = create_engine(database_url, echo=False)
    Base.metadata.create_all(engine)
    return engine


def get_session(engine):
    """Create a new database session."""
    Session = sessionmaker(bind=engine)
    return Session()
