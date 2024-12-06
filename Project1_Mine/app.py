from flask import Flask, jsonify, request

#Intitialise the app
app = Flask(__name__)

error_message = {"status": "error"}
# Define with app does

@app.get("/greet")
def index():

    fname = request.args.get("fname")
    sname = request.args.get("sname")

    if not fname and not sname:
        return jsonify(error_message)
    elif fname and not sname:
        response = {"data": f"Hello, {fname}!"}    
    elif not fname and sname:
        response = {"data": f"Hello, Mr. {sname}!"}    
    else:
        response = {"data": f"Is your name: {fname} {sname}?"}   
    
    return jsonify(response)  


