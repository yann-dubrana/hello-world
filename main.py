import typer


app = typer.Typer()

@app.command()
def hello():
    print("Hello World!")

@app.command()
def hi(name:str = typer.Option("yann")):
    print(f"Hello {name}")

@app.command()
def goodbye():
    print("Goodbye")

if __name__ == "__main__":
    app()
