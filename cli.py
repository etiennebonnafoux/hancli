from typer import Typer
from hackernews_api import HackerNewsAPI
from models import StoryType
from rich.console import Console
from config import Config

app = Typer(rich_markup_mode="rich")
console = Console()
hn_API = HackerNewsAPI()
config = Config()

def print_item(ids: list[int], limit: int):
    with console.status("Downloading..."):
        console.rule()
        for id in ids[:limit]:
            item = hn_API.get_item(id)
            console.print(f"[{config.colors['title']} bold][link={item.url}]{item.title}[/link][/]")
            console.print(f"[{config.colors['score']}]{item.score}[/] by [{config.colors['author']}]{item.by}[/] | comments {item.descendants}")

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
