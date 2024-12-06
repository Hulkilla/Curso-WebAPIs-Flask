from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():

    return render_template("index.html")

# Esta función renderiza el index-html que está en la carpeta templates. Ojo hay que seguir esta estructura!!    

# si das a buscar, te sale esta url: "http://127.0.0.1:5000/search?q=", lo que está detrás de la que es lo que se busca
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