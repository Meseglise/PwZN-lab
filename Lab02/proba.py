from rich.console import Console
import rich.traceback
from rich.progress import track
import time

console = Console()
console.clear()

console.rule("Proba")
console.print()
console.print("[bold red]Proba[/bold red] wyświetlania progress bara")

def do_work():
    time.sleep(1)

for i in track(range(10)):
    do_work()