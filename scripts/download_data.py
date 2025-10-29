#!/usr/bin/env python3
"""
Download and setup initial data sources for Biblical Concept Navigator.

This script downloads:
1. OpenScriptures morphhb (Hebrew morphology)
2. MACULA Greek (Greek morphology)
3. Strong's Concordance data
4. OpenBible.info cross-references
5. Bible databases
"""

import os
import sys
import subprocess
from pathlib import Path
import urllib.request
import zipfile
import json

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.config import get_config
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()


def clone_git_repo(url: str, target_dir: Path, name: str):
    """Clone a git repository if it doesn't exist."""
    if target_dir.exists():
        console.print(f"[yellow]✓[/yellow] {name} already exists at {target_dir}")
        return

    console.print(f"[blue]Downloading {name}...[/blue]")
    try:
        subprocess.run(
            ['git', 'clone', url, str(target_dir)],
            check=True,
            capture_output=True
        )
        console.print(f"[green]✓[/green] Downloaded {name}")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗[/red] Failed to download {name}: {e}")
        console.print(f"[dim]{e.stderr.decode()}[/dim]")


def download_file(url: str, target_path: Path, name: str):
    """Download a file if it doesn't exist."""
    if target_path.exists():
        console.print(f"[yellow]✓[/yellow] {name} already exists")
        return

    console.print(f"[blue]Downloading {name}...[/blue]")
    try:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, target_path)
        console.print(f"[green]✓[/green] Downloaded {name}")
    except Exception as e:
        console.print(f"[red]✗[/red] Failed to download {name}: {e}")


def main():
    """Main download orchestration."""
    console.print("\n[bold]Biblical Concept Navigator - Data Download[/bold]\n")

    config = get_config()
    raw_data = config.RAW_DATA_DIR

    # Ensure directories exist
    raw_data.mkdir(parents=True, exist_ok=True)

    console.print(f"Data directory: {raw_data}\n")

    # 1. OpenScriptures morphhb (Hebrew morphology)
    console.print("[bold cyan]1. Hebrew Morphology (morphhb)[/bold cyan]")
    clone_git_repo(
        "https://github.com/openscriptures/morphhb.git",
        raw_data / "morphhb",
        "OpenScriptures morphhb"
    )

    # 2. MACULA Greek (Greek morphology)
    console.print("\n[bold cyan]2. Greek Morphology (MACULA)[/bold cyan]")
    clone_git_repo(
        "https://github.com/Clear-Bible/macula-greek.git",
        raw_data / "macula-greek",
        "MACULA Greek"
    )

    # 3. Strong's Concordance
    console.print("\n[bold cyan]3. Strong's Concordance[/bold cyan]")
    clone_git_repo(
        "https://github.com/openscriptures/strongs.git",
        raw_data / "strongs",
        "Strong's Concordance"
    )

    # 4. Bible Databases
    console.print("\n[bold cyan]4. Bible Databases[/bold cyan]")
    clone_git_repo(
        "https://github.com/scrollmapper/bible_databases.git",
        raw_data / "bible_databases",
        "Bible Databases"
    )

    # 5. OpenBible.info cross-references
    console.print("\n[bold cyan]5. Cross-References (OpenBible.info)[/bold cyan]")
    console.print("[yellow]Note: Manual download required from OpenBible.info[/yellow]")
    console.print("[dim]Visit: https://www.openbible.info/labs/cross-references/[/dim]")
    console.print("[dim]Download the TSV file to: data/raw/cross_references.txt[/dim]")

    # Summary
    console.print("\n[bold green]Download Summary:[/bold green]")
    console.print("✓ Core datasets downloaded")
    console.print("\n[bold]Next Steps:[/bold]")
    console.print("1. Download OpenBible cross-references manually (see link above)")
    console.print("2. Run: [cyan]python scripts/import_data.py[/cyan] to process data")
    console.print("3. Install SWORD modules: [cyan]installmgr -init[/cyan] (if using SWORD)")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Download cancelled[/yellow]")
        sys.exit(1)
