from flask import Flask, request, render_template, redirect
from model.dbHandler import match_exact, match_like

app = Flask(__name__)

@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instruction formattes as JSON
    """
    # response = {"usage": "/dict?=<word>"}
    # Since this is a website with front-end, we don't need to send the usage instructions
    
    return "TODO"
    

@app.get("/dict")
def dictionary():
    """
    DEFAULT MODE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """

    return "TODO"


if __name__ == "__main__":
    app.run()