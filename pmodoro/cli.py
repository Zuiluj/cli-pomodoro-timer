from typing import Optional
from typing_extensions import Annotated
import typer
from rich import print

from pmodoro import __version__, __app_name__
from pmodoro.pmdoro import Pmodoro


app = typer.Typer(rich_markup_mode="markdown")


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
    ),
) -> None:
    """
    Pomodoro CLI - A command-line interface for managing pomodoro tasks.

    This tool helps you manage your pomodoro sessions and tasks efficiently.
    """


@app.command()
def start(
    duration_in_mins: Annotated[
        float,
        typer.Argument(
            help="Start timer by giving duration in mins",
        ),
    ] = 25,
    msg: Annotated[
        str, typer.Option(help="The message to show when concentrating.")
    ] = "",
    msg_done: Annotated[
        str, typer.Option(help="Message to show when session is done.")
    ] = "",
    color_complete: Annotated[
        str,
        typer.Option(help="Color of the completed gauge. Word color or hex."),
    ] = "green",
) -> None:
    duration_in_secs = duration_in_mins * 60
    runner = Pmodoro(color_complete)
    runner.timer(duration_in_secs, msg, msg_done)
