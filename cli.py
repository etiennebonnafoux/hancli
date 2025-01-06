from typer import Typer, echo
from hackernews_api import HackerNewsAPI

app = Typer(rich_markup_mode="rich")
hn_API = HackerNewsAPI()


@app.command()
def top(limit: int):
    ids = hn_API.get_top(limit)
    for id in ids[:limit]:
        echo(hn_API.get_item(id))


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
