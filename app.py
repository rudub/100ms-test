from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/")

def print_query():
    args_passed = request.args
    return args_passed
    #return '''<h1>The language is : {}</h1>'''.format(language)

if "__name__" == "__main__":
    app.run(host="0.0.0.0",  port=5000, debug=True)
