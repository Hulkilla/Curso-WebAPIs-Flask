from flask import Flask, jsonify, request

#Intitialise the app
app = Flask(__name__)

# Define with app does

@app.get("/greet")
def index():

    response = {"data": "Hello World!!!"}

    return jsonify(response)

"""
Para interactuar con la consola y no ir a la web a ver que sale sería tener dos cmd abiertas
1. donde inicializar la app "flask run"
2 y otra donde hacer esta llamada: curl -i -X GET http://127.0.0.1:5000/greet (local/greet en nuestro caso)
La respuesta que da si todo esta bien es:

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 26
Server: Werkzeug/2.0.1 Python/3.9.13
Date: Fri, 06 Dec 2024 18:42:24 GMT

{"data":"Hello World!!!"}

"""