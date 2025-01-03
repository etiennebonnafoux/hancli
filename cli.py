from typer import Typer,echo

app = Typer(rich_markup_mode="rich")

@app.command()
def top(limit : int):
    echo("Ici les plus belles histoires")

@app.command()
def job(limit : int):
    echo("Ici les jobs")

@app.command()
def ask(limit : int):
    echo("Ici les questions")

@app.command()
def new(limit : int):
    echo("Ici les plus nouvelles")