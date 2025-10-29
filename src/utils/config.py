"""
Configuration management for Biblical Concept Navigator.
"""

import os
from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass
class Config:
    """Application configuration."""

    # Project paths
    PROJECT_ROOT: Path
    DATA_DIR: Path
    RAW_DATA_DIR: Path
    PROCESSED_DATA_DIR: Path
    SWORD_DIR: Optional[Path]

    # Database
    DATABASE_URL: str

    # API keys and endpoints
    SEFARIA_API_BASE: str = "https://www.sefaria.org/api"
    API_BIBLE_KEY: Optional[str] = None
    API_BIBLE_BASE: str = "https://api.scripture.api.bible/v1"

    # Processing options
    BATCH_SIZE: int = 1000
    MAX_WORKERS: int = 4

    @classmethod
    def from_env(cls) -> 'Config':
        """Create config from environment variables."""
        project_root = Path(__file__).parent.parent.parent
        data_dir = project_root / 'data'

        return cls(
            PROJECT_ROOT=project_root,
            DATA_DIR=data_dir,
            RAW_DATA_DIR=data_dir / 'raw',
            PROCESSED_DATA_DIR=data_dir / 'processed',
            SWORD_DIR=Path(os.getenv('SWORD_DIR', '~/.sword')).expanduser()
            if os.getenv('SWORD_DIR')
            else None,
            DATABASE_URL=os.getenv(
                'DATABASE_URL',
                f'sqlite:///{data_dir}/processed/biblical_navigator.db'
            ),
            API_BIBLE_KEY=os.getenv('API_BIBLE_KEY'),
            BATCH_SIZE=int(os.getenv('BATCH_SIZE', '1000')),
            MAX_WORKERS=int(os.getenv('MAX_WORKERS', '4')),
        )


# Global config instance
_config: Optional[Config] = None


def get_config() -> Config:
    """Get or create the global configuration instance."""
    global _config
    if _config is None:
        _config = Config.from_env()
    return _config


def set_config(config: Config):
    """Set the global configuration instance."""
    global _config
    _config = config
