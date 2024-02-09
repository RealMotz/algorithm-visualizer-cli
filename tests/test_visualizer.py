from typer.testing import CliRunner
from visualizer import __app_name__, __version__, cli
from visualizer.visualizer import normalize_stars

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}" in result.stdout

def test_normalize_stars():
    numbers = [5,4,3,2,1]
    case1 = [33, 27, 20, 13, 7]
    numbers2 = [1,1,1,1,1]
    case2 = [20, 20, 20, 20, 20]
    assert normalize_stars(numbers) == case1
    assert normalize_stars(numbers2) == case2