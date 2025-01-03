from flask import flask
app = flask(__name__)
@app.route("/")
def home():
    return "hello, heroku! Your app is running s
    if __name__ == "__main__":
        app.run(debug=True)