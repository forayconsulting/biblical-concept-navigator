# Open-Source Tools and Resources for Hebrew and Greek Linguistic Analysis

This document catalogs open-source tools, datasets, and resources for linguistic analysis of biblical Hebrew and Greek texts.

---

## 1. LEXICONS AND DICTIONARIES

### 1.1 Hebrew Lexicons

#### Brown-Driver-Briggs (BDB) Hebrew Lexicon
- **Description**: Comprehensive Hebrew and English lexicon of the Old Testament based on Gesenius
- **Digital Access**:
  - GitHub Repository: https://github.com/eliranwong/unabridged-BDB-Hebrew-lexicon
  - Internet Archive: https://archive.org/details/BDBHebrewLexicon
  - Online at Sefaria: https://www.sefaria.org/BDB
  - Blue Letter Bible: https://www.blueletterbible.org/resources/lexical/bdb.cfm
- **Format**: XML, JSON (via GitHub projects)
- **License**: Public domain
- **Programmatic Access**: XML/JSON files available for download and parsing
- **Coverage**: All Hebrew and Aramaic words in the Old Testament
- **Notes**: Includes Strong's number mapping in some versions

#### HALOT (Hebrew and Aramaic Lexicon of the Old Testament)
- **Description**: Scholarly lexicon by Koehler and Baumgartner
- **Digital Access**:
  - Free online version: https://dictionaries.brillonline.com/halot
  - Internet Archive: https://archive.org/details/hebrewaramaiclex0002kohl
- **Format**: Online interface, PDF
- **License**: Copyrighted by Brill (not open source, but free access available)
- **Programmatic Access**: Limited - primarily web interface
- **Coverage**: Comprehensive Hebrew and Aramaic lexicon
- **Notes**: Gold standard scholarly lexicon, but not truly open source

### 1.2 Greek Lexicons

#### Strong's Concordance (Greek)
- **Description**: Concordance with Greek lexicon entries
- **Digital Access**:
  - GitHub OpenScriptures: https://github.com/openscriptures/strongs
  - JSON format: http://github.com/openscriptures/strongs/tree/master/greek/
- **Format**: JSON, XML
- **License**: Creative Commons Attribution-ShareAlike (CC-BY-SA)
- **Programmatic Access**: Direct JSON/XML file access
- **Coverage**: All NT Greek words with Strong's numbers
- **Notes**: Includes conversion scripts between XML and JSON formats

#### Thayer's Greek Lexicon
- **Description**: Greek-English lexicon of the New Testament
- **Digital Access**:
  - Available through various Bible software platforms
  - Blue Letter Bible: https://www.blueletterbible.org/
- **Format**: Varies by platform
- **License**: Public domain
- **Programmatic Access**: Limited structured data availability
- **Coverage**: New Testament Greek

#### Liddell-Scott-Jones (LSJ) Greek Lexicon
- **Description**: Comprehensive ancient Greek lexicon (classical and biblical)
- **Digital Access**:
  - Perseids Project (JavaScript): https://github.com/perseids-project/lsj-js
  - TEI XML format: https://github.com/gcelano/LSJ_GreekUnicode
  - Online interface: https://lsj.gr/wiki/Main_Page
  - TLG: https://stephanus.tlg.uci.edu/lsj/
- **Format**: TEI XML, JavaScript web app
- **License**: Creative Commons ShareAlike/Non-Commercial/Attribution (Perseus)
- **Programmatic Access**: XML files and JavaScript library available
- **Coverage**: Classical Greek (broader than biblical)
- **Notes**: Can work offline; highly comprehensive for NT Greek word studies

---

## 2. MORPHOLOGICAL ANALYSIS TOOLS

### 2.1 Hebrew Morphology Analyzers

#### MorphHB (Open Scriptures Hebrew Bible)
- **Description**: Complete morphological analysis of the Hebrew Bible
- **Repository**: https://github.com/openscriptures/morphhb
- **Format**: OSIS XML, JSON (via NPM package)
- **License**: Creative Commons Attribution 4.0
- **Features**:
  - Full lemmatization of Hebrew Bible
  - Strong's number augmentation
  - Part-of-speech tagging
  - Morphological codes for every word
- **Coverage**: Complete Hebrew Bible (Westminster Leningrad Codex)
- **Programmatic Access**: Direct XML/JSON access, Python parsing available
- **Notes**: Community project with 300+ contributors over 10 years

#### ETCBC BHSA (Biblia Hebraica Stuttgartensia Amstelodamensis)
- **Description**: Highly detailed linguistic database of the Hebrew Bible
- **Repository**: https://github.com/ETCBC/bhsa
- **Format**: Text-Fabric format
- **License**: Creative Commons
- **Features**:
  - Advanced syntactic annotations
  - Clause and phrase analysis
  - Semantic domain tagging
  - Multiple linguistic layers
- **Coverage**: Complete Hebrew Bible based on BHS
- **Programmatic Access**: Text-Fabric Python library
- **Usage**: Best accessed via Jupyter Notebook with Text-Fabric
- **Notes**: Most comprehensive linguistic annotation available; multiple versions (2011-present)

#### HebPipe
- **Description**: End-to-end NLP pipeline for Hebrew text
- **Repository**: https://github.com/amir-zeldes/HebPipe
- **Features**:
  - Tokenization
  - POS tagging
  - Morphological analysis
  - Lemmatization
  - Dependency parsing
  - Named entity recognition
  - Coreference resolution
- **Language**: Python
- **Notes**: Modern and biblical Hebrew support

#### YAP (Yet Another Parser)
- **Description**: Morphological analyzer and dependency parser
- **Language**: Go
- **License**: Apache 2.0
- **Features**:
  - Morphological analysis
  - Disambiguation
  - Dependency parsing
- **Notes**: Based on BGU Lexicon

### 2.2 Greek Morphology Analyzers

#### Morpheus
- **Description**: Perseus Project morphological analysis engine
- **Repositories**:
  - https://github.com/perseids-tools/morpheus
  - https://github.com/PerseusDL/morpheus
  - https://github.com/alpheios-project/morpheus
- **Format**: Command-line tool
- **License**: Open source (various)
- **Features**:
  - Lemmatization
  - Full morphological breakdown (POS, case, number, gender, person, mood, tense, voice)
  - Ancient Greek and Latin support
- **Coverage**: Classical and biblical Greek
- **Programmatic Access**: Command-line interface, can be integrated into pipelines
- **Notes**: Gold standard for Greek morphological analysis

#### Kanōnes
- **Description**: System for building corpus-specific Greek morphological parsers
- **Website**: http://neelsmith.github.io/greeklang/morphology/
- **Format**: CSV-based configuration
- **Features**:
  - Customizable lexical stems
  - Configurable inflectional patterns
  - URN-based analysis identification
  - No coding required
- **Usage**: Edit CSV files to build custom parsers
- **Notes**: Ideal for tailoring to specific biblical texts

---

## 3. OPEN DATASETS

### 3.1 Morphologically Tagged Biblical Texts

#### OpenGNT (Open Greek New Testament)
- **Description**: NA28-equivalent Greek NT with comprehensive annotations
- **Repository**: https://github.com/eliranwong/OpenGNT
- **Format**: Tab-delimited text (138k lines, one per word)
- **License**: Creative Commons Attribution-ShareAlike 4.0
- **Data Columns** (11 total):
  1. Clause ID
  2. Book/Chapter/Verse
  3. Greek text (with accents)
  4. Greek text (without accents)
  5. Morphological analysis codes
  6. Strong's numbers
  7. Lexicon entry IDs
  8. Transliterations
  9. Translations/glosses
  10. Punctuation marks
  11. Additional metadata
- **Features**:
  - Robinson's morphological codes
  - Tyndale Amalgamated NT Tagged texts integration
  - OpenText linguistic annotations
  - Berean interlinear translations
  - Mounce dictionary data
- **Programmatic Access**: Direct file download and parsing
- **Notes**: Most comprehensive open dataset for NT Greek

#### SBLGNT (SBL Greek New Testament)
- **Description**: Critically edited Greek NT
- **Repository**: https://github.com/LogosBible/SBLGNT
- **Format**: XML, OSIS, plain text
- **License**: Creative Commons Attribution 4.0
- **Coverage**: Complete New Testament
- **Notes**: High-quality critical text; morphological tagging available through MorphGNT project

#### MorphGNT SBLGNT
- **Description**: Morphological tagging of SBLGNT
- **Repository**: https://github.com/morphgnt/sblgnt
- **Format**: Plain text UTF-8, TAN-LM XML
- **License**: Open source
- **Features**: Complete morphological analysis of SBLGNT

#### LXX Rahlfs 1935 (Septuagint)
- **Description**: Morphologically tagged Septuagint
- **Repository**: https://github.com/eliranwong/LXX-Rahlfs-1935
- **Format**: Similar to OpenGNT structure
- **License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0
- **Coverage**: Complete Septuagint (Greek OT)
- **Notes**: Based on CATSS/LXXM morphological analysis

### 3.2 Hebrew Word Frequency Lists

#### Frequency Dictionary of the Hebrew Bible
- **Description**: Comprehensive frequency analysis of biblical Hebrew
- **Website**: https://hebrew.byu.edu/about-frequency-dictionary
- **Coverage**: All 9,375 headwords and 400,000+ inflected forms
- **Notes**: Top 28 Hebrew words constitute ~50% of all biblical text

#### Teach Me Hebrew Frequency List
- **Access**: https://archive.org/details/Teachmehebrew.comHebrewFrequencyListTeachMeHebrew
- **Format**: Downloadable
- **License**: Open source
- **Coverage**: Biblical Hebrew vocabulary

#### OpenHebrewBible Project
- **Repository**: Aligns BHS with WLC
- **Features**: Bridges ETCBC, OpenScriptures, and Berean data
- **Format**: Text files with linguistic annotations

### 3.3 Greek Word Frequency Lists

#### Wiktionary Greek NT Word Frequency
- **Access**: https://en.wiktionary.org/wiki/Appendix:Word_frequency_in_the_Greek_New_Testament
- **Format**: Wiki table, web scraping possible
- **Coverage**: Words occurring 10+ times in NT
- **Organization**: By part of speech, sorted by frequency
- **Notes**: Based on Aland's concordance and Metzger's Lexical Aids

#### Trenchard's Complete Vocabulary Guide
- **Access**: https://archive.org/details/studentscomplete0000tren
- **Format**: PDF, downloadable
- **Coverage**: Complete NT Greek vocabulary with frequency data
- **Features**: Cognate groupings, principal parts

#### BiblicalGreek.org Frequency List
- **Website**: https://biblicalgreek.org/grammar/vocabulary-frequency-list/
- **Format**: Web-based
- **Notes**: Based on Trenchard's data

### 3.4 Semantic Domain Mappings

#### Louw-Nida Semantic Domains (Greek)
- **Description**: 93 semantic domains organizing NT Greek vocabulary
- **Coverage**: Every NT Greek word categorized by meaning
- **Access**: Commercial (Logos, Accordance, Verbum)
- **License**: Proprietary (not open source)
- **Structure**: Hierarchical domain organization
- **Domains Include**: Plants, Animals, Foods, Learn, Agriculture, Value, Time, Contests, etc.
- **Notes**: No free open-source version available; gold standard for NT semantic analysis

#### Swanson's Dictionary (Hebrew)
- **Description**: Dictionary of Biblical Languages with Semantic Domains for Hebrew
- **Published**: 1997
- **License**: Proprietary
- **Notes**: Semantic domain approach for OT Hebrew

#### Research on Hebrew Semantic Domains
- **Status**: Active research area
- **Note**: No direct Louw-Nida equivalent exists for Hebrew
- **Reference**: Academic papers available on Academia.edu exploring methodology
- **Challenge**: Semantic domains cannot be universally mapped across languages

---

## 4. NLP LIBRARIES FOR BIBLICAL LANGUAGES

### 4.1 General Biblical Language Processing

#### Classical Language Toolkit (CLTK)
- **Description**: NLP library for pre-modern languages
- **Repository**: https://github.com/cltk/cltk
- **Website**: https://cltk.org/
- **Documentation**: https://docs.cltk.org
- **Installation**: `pip install cltk`
- **Language Support**:
  - Ancient Greek (comprehensive)
  - Latin (comprehensive)
  - Classical Hebrew (in development)
  - Sanskrit, Coptic, Classical Chinese, Pali, Hindi, and others
- **Features**:
  - Tokenization
  - Lemmatization
  - Morphological analysis
  - POS tagging
  - Phonological analysis
  - Metrical analysis
  - Corpus management
- **License**: Open source
- **Best For**: Classical Greek analysis, extensible framework
- **Notes**: Most mature for Greek; Hebrew support growing

#### Text-Fabric
- **Description**: Framework for working with ancient text databases
- **Primary Use**: ETCBC Hebrew Bible database
- **Installation**: `pip install text-fabric`
- **Format**: Highly efficient text database format
- **Features**:
  - Fast querying of linguistic features
  - Multiple annotation layers
  - Jupyter Notebook integration
  - Search and analysis capabilities
- **Best For**: Advanced Hebrew Bible linguistic research
- **Repository**: https://github.com/annotation/text-fabric

### 4.2 Transliteration Tools

#### transliterate (Python)
- **PyPI**: https://pypi.org/project/transliterate/
- **Installation**: `pip install transliterate`
- **Language Support**: Hebrew, Greek, Armenian, Georgian, Russian
- **Features**:
  - Bi-directional transliteration
  - Automatic language detection
  - Reversible transformations
- **License**: Open source
- **Best For**: General Hebrew/Greek transliteration

#### Gimeltra
- **Description**: Specialized Semitic script transliteration
- **Repository**: https://github.com/twardoch/gimeltra
- **Installation**: `pip install gimeltra`
- **Language Support**: 20+ scripts, specializing in Semitic
- **Features**:
  - Command-line tool
  - Python library
  - Abjad-only simplified transliteration
- **Best For**: Hebrew and related Semitic languages

#### polyglot
- **Description**: Multi-language NLP library
- **Website**: https://polyglot.readthedocs.io/
- **Features**: Transliteration for 69+ languages including Hebrew and Greek
- **Installation**: `pip install polyglot`

#### betacode (Python)
- **Description**: Beta Code to Unicode converter for Greek
- **Repositories**:
  - https://github.com/matgrioni/betacode
  - https://github.com/willf/betacode
  - https://github.com/perseids-tools/beta-code-py
- **Installation**: `pip install betacode`
- **Usage**:
  ```python
  import betacode.conv
  betacode.conv.beta_to_uni('mh=nin')  # returns 'μῆνιν'
  ```
- **Features**:
  - Fast conversion (3-4 seconds for entire corpus)
  - Bi-directional conversion
  - Based on TLG Beta Code Manual
- **Best For**: Working with Perseus/TLG Greek texts

### 4.3 Hebrew-Specific Python Libraries

#### hebrew (Python package)
- **PyPI**: https://pypi.org/project/hebrew/
- **Installation**: `pip install hebrew`
- **Features**:
  - Hebrew text manipulation
  - Gematria calculations
  - Text complexity handling
- **Notes**: Focused on text processing rather than morphology

#### Hebrew Dependency Parser
- **Language**: Python + Cython
- **Features**:
  - POS tagging
  - Morphological segmentation
  - Dependency parsing
- **License**: Open source
- **Notes**: Java tagger with Python wrapper

### 4.4 Parallel Text and Alignment

#### Multilingual Bible Parallel Corpus
- **Description**: Multi-language parallel Bible corpus
- **Website**: https://christos-c.com/bible/
- **Format**: Sentence-aligned using Book/Chapter/Verse indices
- **Coverage**: Many languages
- **License**: Open source
- **Best For**: Machine translation research, multi-language studies

#### HELFI Corpus
- **Description**: Hebrew-Greek-Finnish parallel corpus with morpheme alignment
- **Access**: ACL Anthology: https://aclanthology.org/2020.lrec-1.522/
- **Features**:
  - Cross-lingual morpheme alignment
  - Morphological analyses
  - Manually constructed alignments
- **License**: Freely available
- **Coverage**: Hebrew OT, Greek LXX, Finnish translations
- **Best For**: Translation studies, alignment research

---

## 5. CONCORDANCE AND SEARCH TOOLS

### 5.1 Open Source Concordance Tools

#### STEP Bible
- **Description**: Scripture Tools for Every Person
- **Developer**: Tyndale House, Cambridge
- **Website**: https://www.stepbible.org/
- **Access**: Free online
- **Features**:
  - Original language search
  - Morphological tagging
  - LXX Rahlfs with morphology
  - Multiple Bible versions
  - Strong's concordance integration
- **License**: Free to use
- **Best For**: Online Bible study with original languages

#### Blue Letter Bible
- **Website**: https://www.blueletterbible.org/
- **Access**: Free online
- **Features**:
  - Strong's concordance
  - Hebrew/Greek lexicons (BDB, Strong's, Thayer's)
  - Concordance searches (KJV, NASB)
  - Interlinear texts
- **License**: Free to use
- **Best For**: Quick concordance lookups and word studies

#### BibleHub
- **Website**: https://biblehub.com/
- **Features**:
  - Interlinear Bible (Hebrew, Greek, Transliterated, English)
  - Strong's concordance
  - Multiple lexicons
  - Parallel translations
- **Access**: Free online
- **Best For**: Comprehensive word study interface

### 5.2 Downloadable Tools and Libraries

#### OpenScriptures Strongs
- **Repository**: https://github.com/openscriptures/strongs
- **Format**: JSON, XML
- **Coverage**: Hebrew and Greek Strong's entries
- **License**: CC-BY-SA
- **Usage**: Can be integrated into custom applications

---

## 6. ADDITIONAL RESOURCES

### 6.1 Research Databases

#### Perseus Digital Library
- **Website**: http://www.perseus.tufts.edu/
- **Contents**: Classical texts, lexicons, morphological tools
- **License**: Open source (varies by resource)
- **Best For**: Classical Greek research, source of many tools (Morpheus, LSJ)

#### Biblical Humanities Dashboard
- **Website**: http://biblicalhumanities.org/dashboard/
- **Description**: Hub for biblical humanities projects and datasets
- **Resources**: Links to various open biblical data projects

### 6.2 Hebrew NLP Resource Compilations

#### Awesome Hebrew NLP
- **Repository**: https://github.com/iddoberger/awesome-hebrew-nlp
- **Description**: Curated list of Hebrew NLP resources
- **Contents**: Tools, datasets, papers, libraries
- **Regularly Updated**: Yes

#### Hebrew Resources (NNLP-IL)
- **Repository**: https://github.com/NNLP-IL/Hebrew-Resources
- **Description**: Comprehensive Hebrew NLP resource list
- **Contents**:
  - Corpora and annotated datasets
  - Lexicons and dictionaries
  - Word lists
  - Word embeddings
  - NLP tools

### 6.3 Recommended Workflows

#### For Hebrew Bible Analysis:
1. **Text Source**: MorphHB or ETCBC BHSA
2. **Morphology**: Built-in to both sources
3. **Analysis Framework**: Text-Fabric (for BHSA) or custom parsing (for MorphHB)
4. **Lexicon**: BDB (from GitHub in JSON/XML)
5. **Frequency Data**: Use BHSA or create from MorphHB

#### For Greek NT Analysis:
1. **Text Source**: OpenGNT or SBLGNT
2. **Morphology**: OpenGNT (built-in) or MorphGNT SBLGNT
3. **Analysis Framework**: CLTK or custom Python scripts
4. **Lexicon**: LSJ (TEI XML) or Strong's (JSON)
5. **Frequency Data**: Wiktionary or create from OpenGNT

#### For Cross-Language Studies:
1. **Parallel Texts**: HELFI corpus or Multilingual Bible Parallel Corpus
2. **Alignment**: Manual or use existing alignments
3. **Morphology**: Combine OpenGNT + MorphHB
4. **Semantic Analysis**: Research papers on semantic domain mapping

---

## 7. LICENSING SUMMARY

### Fully Open Source (CC-BY or similar):
- OpenGNT (CC-BY-SA 4.0)
- MorphHB (CC-BY 4.0)
- SBLGNT (CC-BY 4.0)
- Strong's Concordance data (CC-BY-SA)
- BDB Hebrew Lexicon (Public Domain)
- LSJ Greek Lexicon (CC-BY-NC-SA via Perseus)
- ETCBC BHSA (CC)

### Free but Non-Commercial:
- LXX Rahlfs 1935 (CC-BY-NC-SA 4.0)
- Westminster Hebrew Morphology (CC-BY-NC-ND 4.0)
- Some CATSS/LXXM derivatives

### Proprietary but Free Access:
- HALOT (Free online via Brill, but copyrighted)
- Louw-Nida (Commercial only)

### Public Domain:
- Thayer's Greek Lexicon
- Brown-Driver-Briggs Hebrew Lexicon

---

## 8. PRACTICAL INTEGRATION EXAMPLES

### Example 1: Setting Up Hebrew Analysis Pipeline

```python
# Install required packages
# pip install text-fabric requests

from tf.app import use

# Load ETCBC BHSA database
A = use('bhsa', hoist=globals())

# Query for all occurrences of a specific Hebrew word
query = '''
word lex=אֱלֹהִים
'''

results = A.search(query)
A.show(results, start=1, end=10)
```

### Example 2: Greek Morphological Analysis

```python
# Using OpenGNT data
import csv

def load_opengnt(filepath):
    """Load OpenGNT tab-delimited file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        data = []
        for row in reader:
            if len(row) >= 11:
                word_data = {
                    'clause_id': row[0],
                    'reference': row[1],
                    'greek_with_accents': row[2],
                    'greek_no_accents': row[3],
                    'morphology': row[4],
                    'strongs': row[5],
                    'lexicon_id': row[6],
                    'transliteration': row[7],
                    'translation': row[8],
                    'punctuation': row[9]
                }
                data.append(word_data)
    return data

# Usage
gnt_data = load_opengnt('OpenGNT_version3_3.txt')
# Find all aorist verbs
aorist_verbs = [w for w in gnt_data if 'V-AAI' in w['morphology']]
```

### Example 3: Transliteration

```python
# Hebrew transliteration with transliterate
from transliterate import translit

hebrew_text = "בְּרֵאשִׁית בָּרָא אֱלֹהִים"
transliterated = translit(hebrew_text, 'he', reversed=True)
print(transliterated)

# Greek transliteration with betacode
import betacode.conv

beta = 'e)n a)rxh=| h)=n o( lo/gos'
unicode_greek = betacode.conv.beta_to_uni(beta)
print(unicode_greek)  # ἐν ἀρχῇ ἦν ὁ λόγος
```

---

## 9. RECOMMENDED NEXT STEPS FOR YOUR PROJECT

Based on this research, here are recommended resources for building a biblical concept navigator:

### Core Data Sources:
1. **OpenGNT** - Primary Greek NT source (comprehensive, well-structured)
2. **MorphHB** - Primary Hebrew Bible source (CC-BY 4.0, complete)
3. **Strong's Data** (JSON) - For concordance mapping
4. **BDB Lexicon** (JSON/XML) - For Hebrew definitions
5. **LSJ Lexicon** (TEI XML) - For Greek definitions

### Processing Libraries:
1. **CLTK** - For Greek text processing
2. **Text-Fabric** - For advanced Hebrew analysis (if using BHSA)
3. **betacode** - For Greek text normalization
4. **transliterate** - For user-friendly transliteration

### Frequency and Statistical Data:
1. Generate from OpenGNT and MorphHB (most accurate)
2. Cross-reference with Wiktionary frequency lists
3. Consider ETCBC BHSA for advanced Hebrew statistics

### Semantic Domains:
1. Manual categorization (Louw-Nida not freely available)
2. Research papers for Hebrew semantic groupings
3. Consider building custom semantic mappings based on lexicon entries

### Development Priority:
1. Start with morphologically tagged texts (OpenGNT, MorphHB)
2. Build parsing layer for easy querying
3. Integrate lexicon data (BDB, LSJ, Strong's)
4. Add frequency analysis
5. Develop semantic domain mappings (manual/semi-automated)

---

## 10. CONTACT AND SUPPORT

### Communities and Forums:
- **Digital Classicist**: https://wiki.digitalclassicist.org/
- **OpenScriptures Google Group**: https://groups.google.com/g/openscriptures
- **Biblical Humanities**: http://biblicalhumanities.org/

### Academic Centers:
- **Eep Talstra Centre for Bible and Computer** (ETCBC): https://etcbc.nl/
- **J. Alan Groves Center**: https://grovescenter.org/
- **Tyndale House Cambridge**: https://www.tyndalehouse.com/

### GitHub Organizations:
- **OpenScriptures**: https://github.com/openscriptures
- **ETCBC**: https://github.com/ETCBC
- **Perseus Digital Library**: https://github.com/PerseusDL
- **Perseids Project**: https://github.com/perseids-project

---

**Document Created**: 2025-10-28
**Purpose**: Resource compilation for Biblical Concept Navigator project
**Research Coverage**: Lexicons, morphological tools, datasets, NLP libraries, transliteration, semantic domains, concordances
