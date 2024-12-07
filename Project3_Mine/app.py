from flask import Flask, request, jsonify
from model.dbHandler import match_exact, match_like

app = Flask(__name__)

@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instruction formattes as JSON
    """
    response = {"usage": "/dict?=<words>"}
    # Since this is a website with front-end, we don't need to send the usage instructions
    
    return jsonify(response)
    

@app.get("/dict")
def dictionary():
    """
    DEFAULT MODE
    This method will
    1. Accept a words from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    words = request.args.getlist("word")
    error_msg = {"status" : "error", "word":"words", "data": "word not found"}

    if not words:
        return jsonify(error_msg)

    response = {"words": []}

    for word in words: 
        definitions = match_exact(word)
        if definitions:
            response["words"].append({"status": "success", "data": definitions, "word": word})
        else:
            definitions = match_like(word)
            if definitions:
                response["words"].append({"status": "partial", "data": definitions, "word": word})
            else:
                response["words"].append(error_msg)

    return jsonify(response)

if __name__ == "__main__":
    app.run()

