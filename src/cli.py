#!/usr/bin/env python3
"""
Command-line interface for Biblical Concept Navigator.
"""

import click
from rich.console import Console
from rich.table import Table
from pathlib import Path

console = Console()


@click.group()
@click.version_option(version='0.1.0')
def cli():
    """Biblical Concept Navigator - Deep biblical concept research tool."""
    pass


@cli.command()
def init():
    """Initialize the database and check dependencies."""
    console.print("[bold]Initializing Biblical Concept Navigator...[/bold]\n")

    # Check PySword
    try:
        import pysword
        console.print("[green]✓[/green] PySword installed")
    except ImportError:
        console.print("[red]✗[/red] PySword not installed")
        console.print("  Install with: [cyan]pip install pysword[/cyan]")

    # Check database
    from src.database.schema import init_db
    from src.utils.config import get_config

    config = get_config()
    console.print(f"\nDatabase: {config.DATABASE_URL}")

    try:
        engine = init_db(config.DATABASE_URL)
        console.print("[green]✓[/green] Database initialized")
    except Exception as e:
        console.print(f"[red]✗[/red] Database initialization failed: {e}")

    console.print("\n[bold green]Initialization complete![/bold green]")


@cli.command()
@click.argument('module', default='KJV')
def list_modules(module):
    """List available SWORD modules."""
    try:
        from src.text_acquisition.sword_interface import SWORDInterface

        sword = SWORDInterface()
        modules = sword.list_bible_modules()

        table = Table(title=f"Available SWORD Modules ({len(modules)} found)")
        table.add_column("Module", style="cyan")
        table.add_column("Count", justify="right")

        for i, mod in enumerate(modules, 1):
            table.add_row(mod, str(i))

        console.print(table)

    except ImportError as e:
        console.print(f"[red]Error:[/red] {e}")
        console.print("Install PySword: [cyan]pip install pysword[/cyan]")


@cli.command()
@click.argument('reference')
@click.option('--module', '-m', default='KJV', help='Bible module to use')
def get_verse(reference, module):
    """
    Get a verse by reference.

    Example: bcn get-verse "John 3:16"
    """
    from src.text_acquisition.sword_interface import SWORDInterface, parse_reference

    parsed = parse_reference(reference)
    if not parsed:
        console.print(f"[red]Error:[/red] Invalid reference: {reference}")
        console.print("Format: 'Book Chapter:Verse' (e.g., 'John 3:16')")
        return

    book, chapter, verse = parsed

    try:
        sword = SWORDInterface()
        verse_text = sword.get_verse(module, book, chapter, verse)

        console.print(f"\n[bold]{verse_text.reference}[/bold] ({module})")
        console.print(f"{verse_text.clean_text}\n")

    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")


@cli.command()
@click.argument('concept')
@click.option('--book', '-b', help='Limit search to specific book')
@click.option('--module', '-m', default='KJV', help='Bible module to use')
def search(concept, book, module):
    """
    Search for a concept across the Bible.

    Example: bcn search "sin" --book Romans
    """
    console.print(f"[bold]Searching for:[/bold] {concept}")
    console.print(f"[bold]Module:[/bold] {module}")
    if book:
        console.print(f"[bold]Book:[/bold] {book}")

    console.print("\n[yellow]Note: Full concept search not yet implemented[/yellow]")
    console.print("[dim]Coming soon: multi-dimensional concept analysis[/dim]")


@cli.command()
def download():
    """Download required data sources."""
    console.print("[bold]Launching data download...[/bold]\n")

    import subprocess
    import sys
    from pathlib import Path

    script_path = Path(__file__).parent.parent / "scripts" / "download_data.py"

    try:
        subprocess.run([sys.executable, str(script_path)], check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Download failed:[/red] {e}")


@cli.command()
def status():
    """Check system status and data availability."""
    from src.utils.config import get_config

    config = get_config()

    table = Table(title="System Status")
    table.add_column("Component", style="cyan")
    table.add_column("Status")
    table.add_column("Location", style="dim")

    # Check data directories
    raw_exists = config.RAW_DATA_DIR.exists()
    table.add_row(
        "Raw Data Directory",
        "[green]✓[/green]" if raw_exists else "[red]✗[/red]",
        str(config.RAW_DATA_DIR)
    )

    processed_exists = config.PROCESSED_DATA_DIR.exists()
    table.add_row(
        "Processed Data Directory",
        "[green]✓[/green]" if processed_exists else "[red]✗[/red]",
        str(config.PROCESSED_DATA_DIR)
    )

    # Check database
    db_path = Path(config.DATABASE_URL.replace('sqlite:///', ''))
    db_exists = db_path.exists()
    table.add_row(
        "Database",
        "[green]✓[/green]" if db_exists else "[red]✗[/red]",
        str(db_path)
    )

    # Check data sources
    data_sources = [
        ("morphhb", "Hebrew Morphology"),
        ("macula-greek", "Greek Morphology"),
        ("strongs", "Strong's Concordance"),
        ("bible_databases", "Bible Databases"),
    ]

    for dirname, description in data_sources:
        source_path = config.RAW_DATA_DIR / dirname
        exists = source_path.exists()
        table.add_row(
            description,
            "[green]✓[/green]" if exists else "[yellow]⊘[/yellow]",
            str(source_path) if exists else "Not downloaded"
        )

    console.print(table)

    # Recommendations
    if not all([raw_exists, processed_exists]):
        console.print("\n[yellow]Run:[/yellow] [cyan]bcn init[/cyan] to create directories")

    if not db_exists:
        console.print("[yellow]Run:[/yellow] [cyan]bcn init[/cyan] to initialize database")

    missing_data = any(
        not (config.RAW_DATA_DIR / dirname).exists()
        for dirname, _ in data_sources
    )
    if missing_data:
        console.print("[yellow]Run:[/yellow] [cyan]bcn download[/cyan] to get data sources")


def main():
    """Entry point for CLI."""
    cli()


if __name__ == '__main__':
    main()
