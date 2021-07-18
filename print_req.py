from flask import Flask
from flask import Response
from flask import request

app = Flask(__name__)

@app.route("/")

def print_request():
    args_passed = request.args
    return args_passed

if __name__ == "__main__":
    app.run(host="0.0.0.0",  port=5000, debug=True)
