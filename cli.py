from typer import Typer
from hackernews_api import HackerNewsAPI
from models import StoryType
from rich.console import Console

app = Typer(rich_markup_mode="rich")
console = Console()
hn_API = HackerNewsAPI()

def print_item(ids :list[int],limit:int):
    with console.status("Downloading..."):
        console.rule()
        for id in ids[:limit]:
            item = hn_API.get_item(id)
            console.print(f"[bold][link={item.url}]{item.title}[/link][bold] ")
            console.print(f"{item.score} by {item.by} | comments {item.descendants}")

@app.command()
def top(limit: int = 10):
    ids = hn_API.get_stories(story_type=StoryType.Top,limit=limit)
    print_item(ids=ids,limit=limit)


@app.command()
def job(limit: int = 10):
    ids = hn_API.get_stories(story_type=StoryType.Job,limit=limit)
    print_item(ids=ids,limit=limit)


@app.command()
def ask(limit: int = 10):
    ids = hn_API.get_stories(story_type=StoryType.Ask,limit=limit)
    print_item(ids=ids,limit=limit)


@app.command()
def new(limit: int = 10):
    ids = hn_API.get_stories(story_type=StoryType.New,limit=limit)
    print_item(ids=ids,limit=limit)

@app.command()
def show(limit: int = 10):
    ids = hn_API.get_stories(story_type=StoryType.Show,limit=limit)
    print_item(ids=ids,limit=limit)

@app.command()
def best(limit: int = 10):
    ids = hn_API.get_stories(story_type=StoryType.Best,limit=limit)
    print_item(ids=ids,limit=limit)
