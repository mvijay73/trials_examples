from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    res = "Hello from kubeapp. Click on the this link http://localhost:5001/check"
    return res

@app.route("/check")
def check():
    return "Web service is ready, You can login using the URL: <href>http://localhost:5001/login</href>"

@app.route("/login")
def login():
    return "Please enter your user name"
if __name__ == "__main__":
    app.run(host='0.0.0.0')
