from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! How are you? I am testing CI/CD."
