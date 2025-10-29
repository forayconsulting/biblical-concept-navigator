# Biblical Concept Navigator

A comprehensive Python-based system for deep biblical concept research across multiple manuscript traditions, original languages, and extra-biblical sources.

## Features

- **Multi-Manuscript Support**: Analyze concepts across Masoretic Text, Septuagint, Dead Sea Scrolls, Peshitta, Vulgate, and Targums
- **Original Language Analysis**: Full Hebrew, Greek, and Aramaic morphological analysis
- **Semantic Detection**: NLP-based metaphor and analogy detection
- **Source Criticism**: JEPD framework and historical dating information
- **Extra-Biblical Context**: Integration with Ancient Near Eastern texts, rabbinic literature, and classical sources
- **Cross-Reference Mapping**: 340,000+ biblical cross-references with graph visualization

## Project Structure

```
biblical-concept-navigator/
├── src/                    # Source code
│   ├── database/          # Database schemas and models
│   ├── text_acquisition/  # Bible text access (SWORD, APIs)
│   ├── linguistic/        # Morphology and lexicon analysis
│   ├── manuscript/        # Manuscript comparison
│   ├── semantic/          # NLP and semantic analysis
│   ├── extra_biblical/    # External corpus queries
│   ├── query/             # Query orchestration
│   └── utils/             # Utilities
├── data/                   # Data storage
│   ├── raw/               # Raw data downloads
│   └── processed/         # Processed databases
├── scripts/               # Import and setup scripts
├── tests/                 # Unit tests
└── notebooks/             # Jupyter notebooks
```

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download required data
python scripts/download_data.py
```

## Quick Start

```python
from src.query.orchestrator import ConceptNavigator

# Initialize the navigator
navigator = ConceptNavigator()

# Query a concept
results = navigator.query_concept("Sin")

# Results include:
# - Original language words and morphology
# - Manuscript distribution
# - Detected metaphors and analogies
# - Source criticism (JEPD) assignments
# - Proposed remedies
# - Extra-biblical usage context
```

## Data Sources

All data sources are open-source, public domain, or freely licensed:

- **Bible Texts**: SWORD Project (200+ modules)
- **Hebrew Morphology**: OpenScriptures morphhb (CC BY 4.0)
- **Greek Morphology**: MACULA Greek (freely licensed)
- **Lexicons**: Strong's, BDB, Thayer's (public domain)
- **Cross-References**: OpenBible.info (340,000+ references)
- **Extra-Biblical**: CAL, Perseus, Sefaria, ORACC

## License

MIT License - See LICENSE file for details

## Research Dimensions

This tool addresses six interconnected research dimensions:

1. **Textual**: Which manuscripts contain references
2. **Linguistic**: Original Hebrew/Greek/Aramaic words and morphology
3. **Semantic**: Analogies, metaphors, conceptual frameworks
4. **Historical**: Dating, redaction layers, source criticism
5. **Theological**: Proposed remedies and solutions
6. **Comparative**: Extra-biblical usage for semantic context

## Development Status

Current Sprint: Foundation (Week 1-2)
- [x] Project structure setup
- [ ] PySword integration
- [ ] Database schema creation
- [ ] Basic verse retrieval API
- [ ] morphhb data import

## Contributing

This is a research project. Contributions welcome! Please see CONTRIBUTING.md for guidelines.

## Citation

If you use this tool in academic work, please cite:
```
Biblical Concept Navigator (2025)
https://github.com/yourusername/biblical-concept-navigator
```
