from flask import Flask, jsonify, request

#Intitialise the app
app = Flask(__name__)

# Define with app does

@app.get("/greet")
def index():
    """
    TODO:
    1. Capture first and last name
    2. if either is not provided: respond with an error
    3. if fisrt name is not provided but second is: respond with "Hello Mr >second-name>!"
    4. if fisrt name is provided but second not: respond with "Hello Mr >first-name>!"
    5. if both are provided: respond with a question: "Is your name: <first> <second>?
    """
    return jsonify("TODO")

"""
Para inicializar ejecutar desde consola cmd: flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

 Nos sales este mensaje. Si te das cuenta arriba tenemos puesto un /greet
 Pues si en el navegador pones esa url /greet, te sale de dentro de la función index
"""
