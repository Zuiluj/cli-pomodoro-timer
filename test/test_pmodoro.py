import unittest
from typer.testing import CliRunner

from pmodoro import __app_name__, __version__, cli

runner = CliRunner()


class TestCliMethods(unittest.TestCase):
    def test_version(self):
        result = runner.invoke(cli.app, ["--version"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(f"{__app_name__} version {__version__}\n", result.stdout)

    def test_timer_setup(self):
        # Test that the timer is set up correctly with a given duration
        duration = 0.0001
        result = runner.invoke(cli.app, ["start", str(duration)])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(f"⏳ Started at:", result.stdout)

    def test_timer_msg(self):
        duration = 0.0001
        result = runner.invoke(
            cli.app, ["start", str(duration), "--msg=Custom message"]
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn(f"Custom message", result.stdout)

    def test_timer_msg_done(self):
        duration = 0.0001
        result = runner.invoke(
            cli.app, ["start", str(duration), "--msg-done=custom done!"]
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn(f"custom done!", result.stdout)

    def test_timer_msg_and_msg_done(self):
        duration = 0.0001
        result = runner.invoke(
            cli.app,
            ["start", str(duration), "--msg=Custom message", "--msg-done=custom done!"],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn(f"Custom message", result.stdout)
        self.assertIn(f"custom done!", result.stdout)
