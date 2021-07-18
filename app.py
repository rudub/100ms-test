from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route("/")

def print_query():
    args_passed = request.args
    return args_passed

if __name__ == "__main__":
    app.run(host="0.0.0.0",  port=5000, debug=True)
