from flask import Flask, request, render_template, jsonify
from model.dbHandler import match_exact, match_like

app = Flask(__name__)

@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instruction formattes as JSON
    """
    response = {"usage": "/dict?=<word>"}
    # Since this is a website with front-end, we don't need to send the usage instructions
    
    return jsonify(response)
    

@app.get("/dict")
def dictionary():
    """
    DEFAULT MODE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    word = request.args.get("word")
    error_msg = {"status" : "error", "data": "word not found"}

    if not word:
        return jsonify(error_msg)

    
    definitions = match_exact(word)
    if definitions:
        return jsonify({"status": "success", "data": definitions, "word": word})


    definitions = match_like(word)
    if definitions:
        return jsonify({"status": "partial", "data": definitions})
    else:
        return jsonify(error_msg) 


if __name__ == "__main__":
    app.run()

"""
Hemos empezado a crear la app que nos va a dar definiciones. 
Hemos creado las distitnas respuestas en las distintas posibilidades que hay. 
Ahora lo que hay que hacer es construir la conexión a la bbdd que nos dará las definiciones de las palabras que busquemos
en el archivo dbHandler.py
"""