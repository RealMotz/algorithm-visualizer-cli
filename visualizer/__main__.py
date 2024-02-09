import sys
from visualizer import cli

def default_command():
    """
    Algorithms Visualizer CLI app.

    Displays each step of the sorting process for the chosen algorithm
    """
    print("Welcome to the Algorithms Visualizer CLI! Use --help to see available commands and options.")

def main():
    cli.app()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        default_command()
    else:
        main()