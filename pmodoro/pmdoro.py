import time
import datetime
from typing import Text
from rich import print
from rich.markdown import Markdown
from rich.progress import (
    BarColumn,
    TextColumn,
    TimeRemainingColumn,
)
from rich.progress import Task
from rich.text import Text


from pmodoro.progress import PmodoroProgress


class PmodoroTimeRemainingColumn(TimeRemainingColumn):
    """Custom class to show accurate time remaining and not estimated"""

    def render(self, task: Task) -> Text:
        if task.total is None:
            return Text("", style="blue")
        return Text(
            str(datetime.timedelta(seconds=(round(task.total - task.completed)))),
            style="blue",
        )


class Pmodoro:
    def __init__(self, color_complete: str):
        self.progress = PmodoroProgress(
            TextColumn("{task.description}"),
            BarColumn(complete_style=color_complete),
            "[progress.percentage]{task.percentage:>3.1f}%",
            PmodoroTimeRemainingColumn(),
        )

    def timer(self, duration_in_sec: float, message: str, message_finished: str):
        print(Text("⏳ Started at: ", style="bold"), end="")
        print(time.ctime())
        msg = message or "Concentrating..."
        finished_msg = message_finished or "🥳 Done!"
        self.progress.start()
        for value in self.progress.track(
            range(round(duration_in_sec), 0, -1), description=msg
        ):
            time.sleep(1)
        self.progress.stop()
        print(finished_msg)
