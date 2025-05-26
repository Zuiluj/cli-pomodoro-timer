import time
from rich import print

from pmodoro.progress import MyProgress


class Pmodoro:
    def __init__(self):
        self.progress = MyProgress()

    def timer(self, duration_in_sec: int):
        print(f"⏳ Started at: {time.ctime()}")
        self.progress.start()
        for value in self.progress.track(
            range(duration_in_sec, 0, -1), description="Concentrating... "
        ):
            time.sleep(1)
        self.progress.stop()
        print(f"🥳 Done!", flush=True)
