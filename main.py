import typer
from rich import print

app = typer.Typer()

@app.command()
def hello(name: str = "world"):
    print(f"[green]Hello {name}![/green]")

if __name__ == "__main__":
    app()
