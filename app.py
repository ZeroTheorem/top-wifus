from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def test():
    return render_template("index.html")


@app.route("/Rias")
def vote_Rias():
    return render_template("vote_Rias.html")


if __name__ == '__main__':
    app.run()
