from typing import Optional
import typer
from rich.prompt import IntPrompt
from visualizer import __app_name__, __version__
from visualizer.visualizer import plot

app = typer.Typer()

def _version_callback(version: bool) -> None:
    if(version):
        print(f"{__app_name__} v{__version__}")
        raise typer.Exit()

option = typer.Option(None,
                      "--version",
                      "-v",
                      help="Show current version",
                      callback=_version_callback,
                      is_eager=True,)

@app.command()
def sort() -> None:
    options = ["Bubble Sort", "Merge Sort", "Insertion Sort"]
    for index, option in enumerate(options, start=1):
        print(f"{index}: {option}")
    choice = IntPrompt.ask("Sorting type: ", choices=[str(index) for index, _ in enumerate(options, start=1)])
    plot(choice)

@app.callback()
def main(version: Optional[bool] = option) -> None:
    return