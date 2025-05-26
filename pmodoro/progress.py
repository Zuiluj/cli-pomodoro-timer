import datetime
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table


class MyProgress(Progress):
    pass
    # def get_renderables(self):
    #     yield Panel(self.make_tasks_table(self.tasks))
