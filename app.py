from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def test():
    score = {
        "Rias": 9.8,
        "Asia": 8.0,
        "Akeno": 9.9,
        "Koneko": 7.0
    }

    return render_template("index.html", score=score)


@app.route("/Rias")
def vote_Rias():
    return render_template("vote_Rias.html")


if __name__ == '__main__':
    app.run(debug=True)
