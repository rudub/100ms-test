import requests

app = Flask(__name__)

@app.route("/")

def print_request():
    payload = requests.get("http://127.0.0.1:5000/")
    language = request.args.get('language')
    return '''<h1>The language is : {}</h1>'''.format(language)

if "__name__" == "__main__":
    app.run(host="0.0.0.0",  port=5000)
