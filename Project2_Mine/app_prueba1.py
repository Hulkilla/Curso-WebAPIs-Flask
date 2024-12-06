from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    """
    TODO:
    Render the home page provided under templates/index.html in the repository
    """
    return "TODO"
    

@app.get("/search")
def search():
    """
    todo:
    1. Capture the word that is being searched
    2. Search for the word on Google and display results
    """
    return "todo"


if __name__ == "__main__":
    app.run()