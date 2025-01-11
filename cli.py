from typer import Typer, echo
from hackernews_api import HackerNewsAPI
from rich.console import Console

app = Typer(rich_markup_mode="rich")
console = Console()
hn_API = HackerNewsAPI()


@app.command()
def top(limit: int = 10):
    ids = hn_API.get_top(limit)
    with console.status("Working..."):
        console.rule()
        for id in ids[:limit]:
            item = hn_API.get_item(id)
            console.print(f"[bold][link={item.url}]{item.title}[/link][bold] ")
            console.print(f"{item.score} by {item.by} | comments {item.descendants}")


@app.command()
def job(limit: int):
    echo("Ici les jobs")


@app.command()
def ask(limit: int):
    echo("Ici les questions")


@app.command()
def new(limit: int):
    """
    Cette fonction affiche les nouvelles.
    """
    echo("Ici les plus nouvelles")
