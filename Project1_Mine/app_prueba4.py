from flask import Flask, jsonify, request

#Intitialise the app
app = Flask(__name__)

# Define with app does

@app.get("/greet")
def index():

    name = request.args.get("name")
    response = {"data": f"Hello, {name} !"}

    return jsonify(response)


"""
 para que salga datos la url sería: http://127.0.0.1:5000/greet?name=Marina

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 25
Server: Werkzeug/2.0.1 Python/3.9.13
Date: Fri, 06 Dec 2024 18:54:37 GMT

{"data":"Hello, Marina"}

"""