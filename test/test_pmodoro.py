import unittest
from typer.testing import CliRunner

from pmodoro import __app_name__, __version__, cli

runner = CliRunner()


class TestCliMethods(unittest.TestCase):
    def test_version(self):
        result = runner.invoke(cli.app, ["--version"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(f"{__app_name__} version {__version__}\n", result.stdout)
