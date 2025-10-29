"""Setup script for Biblical Concept Navigator."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

setup(
    name="biblical-concept-navigator",
    version="0.1.0",
    description="Deep biblical concept research across manuscripts, languages, and traditions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Clayton Chancey",
    url="https://github.com/yourusername/biblical-concept-navigator",
    packages=find_packages(),
    install_requires=[
        "pysword>=0.2.7",
        "sqlalchemy>=2.0.0",
        "click>=8.1.0",
        "rich>=13.7.0",
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.11.0",
            "flake8>=6.1.0",
        ],
        "full": [
            "spacy>=3.7.0",
            "scikit-learn>=1.3.0",
            "pandas>=2.1.0",
            "numpy>=1.24.0",
            "networkx>=3.2.0",
            "jupyter>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "bcn=src.cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Religion",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
