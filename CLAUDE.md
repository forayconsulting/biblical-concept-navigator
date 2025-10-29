# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Biblical Concept Navigator is a Python-based research system for deep biblical concept analysis across six interconnected dimensions: textual (manuscripts), linguistic (morphology), semantic (metaphors), historical (source criticism/dating), theological (remedies), and comparative (extra-biblical context).

**Core Goal**: Enable queries like "Find all references to 'Sin' with original language words, manuscript sources, metaphors used, dating/JEPD assignments, proposed remedies, and extra-biblical usage context."

## Development Commands

### Environment Setup
```bash
# Activate virtual environment (always required)
source venv/bin/activate

# Install package in development mode
pip install -e .

# Install all dependencies
pip install -r requirements.txt
```

### Core Commands
```bash
# Initialize database and check dependencies
python -m src.cli init

# Check system status
python -m src.cli status

# Download core datasets (morphhb, MACULA, Strong's, bible_databases)
python -m src.cli download

# List available SWORD Bible modules
python -m src.cli list-modules

# Get specific verse
python -m src.cli get-verse "John 3:16" --module KJV

# Search for concept (framework in place, full implementation pending)
python -m src.cli search "sin" --book Romans
```

### Testing
```bash
# Run all tests (when implemented)
pytest tests/

# Run specific test file
pytest tests/test_database.py

# Run with coverage
pytest --cov=src tests/
```

### Direct Module Execution
```bash
# Test SWORD interface directly
python src/text_acquisition/sword_interface.py

# Test database schema
python -c "from src.database.schema import init_db; init_db()"
```

## Architecture: Six-Engine Query System

The system uses a **modular engine architecture** where each research dimension is handled by a specialized engine coordinated by a central orchestrator:

```
User Query ("Sin")
    ↓
Query Orchestrator (src/query/)
    ↓
┌─────────────┬──────────────┬─────────────┬─────────────┬──────────────┐
│ Text Engine │ Ling Engine  │ Man Engine  │ Sem Engine  │ Extra Engine │
│ (SWORD)     │ (morphhb)    │ (MT/LXX)    │ (NLP)       │ (CAL/Sefaria)│
└─────────────┴──────────────┴─────────────┴─────────────┴──────────────┘
                            ↓
                    SQLite Database
                    (11 interconnected tables)
                            ↓
                    Aggregated Results
```

### Key Modules

**`src/database/schema.py`** - SQLAlchemy ORM with 11 tables:
- Core data model defining 6 research dimensions
- Uses SQLAlchemy relationships, not manual foreign key management
- `init_db()` creates all tables with proper indexes
- Access via `get_session(engine)` for queries

**`src/text_acquisition/sword_interface.py`** - SWORD Project integration:
- `SWORDInterface` class provides Bible text access to 200+ translations
- `get_verse()`, `get_verses()`, `search_keyword()` methods
- Automatic markup cleaning (OSIS/GBF/ThML → plain text)
- `parse_reference()` utility for "John 3:16" → (book, chapter, verse)
- Module caching in `_loaded_bibles` dict

**`src/utils/config.py`** - Environment-based configuration:
- `get_config()` returns singleton `Config` dataclass
- Paths: `PROJECT_ROOT`, `DATA_DIR`, `RAW_DATA_DIR`, `PROCESSED_DATA_DIR`
- Database: `DATABASE_URL` (defaults to SQLite in data/processed/)
- API keys: `SEFARIA_API_BASE`, `API_BIBLE_KEY`
- Processing: `BATCH_SIZE`, `MAX_WORKERS`

**`src/cli.py`** - Click-based CLI with Rich terminal UI:
- Entry point: `bcn` command (registered in setup.py)
- All commands use `console` (Rich Console) for output
- Follow existing patterns for new commands

## Database Schema Design Principles

The 11 tables map directly to research dimensions:

**Textual Dimension:**
- `manuscripts` → Different traditions (MT, LXX, DSS, Peshitta, Vulgate)
- `books` → Biblical books with canonical metadata
- `verses` → Verse text per manuscript (many-to-many with self for cross-refs)
- `verse_cross_references` → Association table with weight

**Linguistic Dimension:**
- `lemmas` → Root words with Strong's numbers, indexed by `strongs_number` and `word`
- `word_occurrences` → Every word instance with full morphology (POS, tense, voice, mood, case)

**Historical Dimension:**
- `source_assignments` → JEPD framework, dating ranges, confidence scores

**Semantic Dimension:**
- `concepts` → Biblical themes (Sin, Covenant, Grace)
- `concept_occurrences` → Links concepts to verses with detection metadata
- `metaphors` → Analogies with source_domain and type classification

**Theological Dimension:**
- `remedies` → Solutions for concepts (sacrifice, repentance, forgiveness)

**Comparative Dimension:**
- `extra_biblical_references` → Word usage in ANE texts, rabbinic literature

**System:**
- `import_logs` → Track data imports (use `import_metadata` not `metadata` - reserved word)

## Data Flow and Integration Patterns

### Adding New Data Sources

1. **Download**: Add to `scripts/download_data.py` using `clone_git_repo()` or `download_file()`
2. **Import**: Create importer in appropriate module (e.g., `src/linguistic/morphhb_importer.py`)
3. **Pattern**: Use batch processing with `config.BATCH_SIZE`, track with `ImportLog`
4. **Session management**: Always use context managers or explicit commit/rollback

```python
from src.database.schema import get_session, init_db, ImportLog
from src.utils.config import get_config

config = get_config()
engine = init_db(config.DATABASE_URL)
session = get_session(engine)

# Create import log
log = ImportLog(import_type='morphhb', status='started')
session.add(log)
session.commit()

try:
    # Import data in batches
    for batch in process_in_batches(data, config.BATCH_SIZE):
        session.bulk_insert_mappings(Lemma, batch)
        session.commit()

    log.status = 'success'
    log.records_imported = total_count
except Exception as e:
    log.status = 'failed'
    log.error_message = str(e)
    session.rollback()
finally:
    log.completed_at = datetime.utcnow()
    session.commit()
```

### SWORD Module Integration

PySword auto-detects modules in `~/.sword/` (or `SWORD_DIR` env var). The interface caches loaded modules for performance. When adding SWORD functionality:

- Use `SWORDInterface` instance methods, not direct PySword calls
- Handle `ImportError` gracefully (PySword may not be installed)
- Clean markup automatically with `VerseText.clean_text`
- Parse references with `parse_reference()` before queries

## Module Implementation Status

**✅ Completed (Sprint 1):**
- Database schema (all 11 tables)
- SWORD interface (verse retrieval, search)
- CLI framework (6 commands operational)
- Configuration system
- Download automation script

**🚧 Next Priority (Sprint 2 - Linguistic Analysis):**
- `src/linguistic/morphhb_importer.py` - Parse and import Hebrew morphology
- `src/linguistic/strongs_importer.py` - Load concordance data
- `src/linguistic/morphology_parser.py` - Decode morphology codes
- `src/linguistic/word_family.py` - Analyze roots and derivatives

**📋 Pending Implementation:**
- `src/manuscript/` - Parallel text comparison (MT vs LXX vs Peshitta)
- `src/semantic/` - NLP metaphor detection, semantic clustering
- `src/extra_biblical/` - CAL, Perseus, Sefaria API clients
- `src/query/orchestrator.py` - Central query coordination
- Export functionality (JSON, CSV, Markdown, Obsidian)

## Critical Design Constraints

**SWORD Modules**: Users install via CrossWire InstallMgr, not bundled. Document installation in README if adding SWORD-dependent features.

**JEPD Source Data**: No free/open dataset exists. Current options:
1. Manual digitization from Friedman's "The Bible with Sources Revealed" (2003)
2. License Logos Source Criticism Dataset (commercial)
3. Use scholarly consensus for dating only (skip detailed source assignments)

**Hebrew/Greek Text Processing**:
- Use `transliterate` library for romanization
- Store both original script and transliteration in database
- morphhb uses Westminster Leningrad Codex (WLC) format
- MACULA uses Nestle 1904 for Greek

**Performance**:
- Index all foreign keys and frequently queried fields
- Use batch operations for bulk imports (never individual inserts in loops)
- Consider read replicas if query load increases
- Cache SWORD module instances (already implemented)

## External Data Sources

All sources are open/freely licensed (documented in HEBREW_GREEK_RESOURCES.md):

**Primary Sources:**
- OpenScriptures morphhb (GitHub) - Hebrew morphology, CC BY 4.0
- MACULA Greek (GitHub) - Greek NT morphology, freely licensed
- Strong's Concordance (GitHub) - Public domain
- OpenBible.info - 340,000+ cross-references, public domain
- Sefaria API - Jewish texts, open API

**APIs Available:**
- Sefaria: `https://www.sefaria.org/api` (no key required)
- API.Bible: `https://api.scripture.api.bible/v1` (free tier, key in `API_BIBLE_KEY` env)

## Testing Philosophy

When tests are implemented:
- Test database operations with in-memory SQLite (`:memory:`)
- Mock external APIs (SWORD, Sefaria) to avoid network dependencies
- Use fixtures for common test data (sample verses, lemmas)
- Separate unit tests (single module) from integration tests (cross-module)

## Common Gotchas

1. **SQLAlchemy reserved words**: `metadata` is reserved, use `import_metadata` or similar
2. **SWORD module availability**: Always check if modules exist before querying
3. **Unicode handling**: Hebrew/Greek text requires UTF-8 throughout
4. **Virtual environment**: Always activate before running commands
5. **Path handling**: Use `Path` objects, never string concatenation for paths
6. **Reference parsing**: Handles "1 John 3:16" (multi-word books) correctly

## Configuration via Environment Variables

Create `.env` file in project root (gitignored):

```bash
# Database (optional, defaults to SQLite in data/processed/)
DATABASE_URL=sqlite:///data/processed/biblical_navigator.db

# API keys (optional)
API_BIBLE_KEY=your_key_here

# SWORD modules directory (optional)
SWORD_DIR=/path/to/sword/modules

# Processing (optional)
BATCH_SIZE=5000
MAX_WORKERS=8
```

Load with `python-dotenv` (add to requirements.txt if using .env files).

## Next Steps for Development

Current focus: **Sprint 2 - Linguistic Analysis**

1. Implement `src/linguistic/morphhb_importer.py`:
   - Parse morphhb XML files from `data/raw/morphhb/`
   - Extract lemmas with Strong's numbers
   - Parse morphology codes (POS, gender, number, etc.)
   - Bulk insert into `lemmas` and `word_occurrences` tables

2. Build word family analyzer for Hebrew roots (חטא → חטאת, חטאים, etc.)

3. Test end-to-end: Query all Hebrew words for "sin" concept with morphology

4. Document morphology code system in module docstrings

See STATUS.md for detailed sprint planning and research resources.
