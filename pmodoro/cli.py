from typing import Optional
import typer
from pmodoro import __version__, __app_name__

app = typer.Typer()


def _version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} version {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=_version_callback,
        is_eager=True,
        help="Show the version and exit.",
    )
) -> None:
    """
    Pomodoro CLI - A command-line interface for managing pomodoro tasks.

    This tool helps you manage your pomodoro sessions and tasks efficiently.
    """
    return
