from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<H1>Hello...<BR>  Welcome to Docker !!! </H1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
