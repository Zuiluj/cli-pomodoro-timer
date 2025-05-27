import time
from rich import print

from pmodoro.progress import MyProgress


class Pmodoro:
    def __init__(self):
        self.progress = MyProgress()

    def timer(self, duration_in_sec: int, message: str, message_finished: str):
        print(f"⏳ Started at: {time.ctime()}")
        msg = message or "Concentrating..."
        finished_msg = message_finished or "🥳 Done!"
        self.progress.start()
        for value in self.progress.track(
            range(duration_in_sec, 0, -1), description=msg
        ):
            time.sleep(1)
        self.progress.stop()
        print(finished_msg)
