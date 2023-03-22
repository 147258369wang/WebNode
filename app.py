from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route("/")
def index():
    return render_template("index.html.jinja2", messages=messages)

@app.route("/post/add/", methods=["POST"])
def add_post():
    message = request.form["message"]
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages.append({"message": message, "time_stamp": time_stamp})
    return render_template("index.html.jinja2", messages=messages)

if __name__ == "__main__":
    app.run(debug=True) 