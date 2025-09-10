from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "初めまして!"

@app.route("/about")
def about():
    return "aboutの画面です"

if __name__ == "__main__":
    app.run(debug=True)