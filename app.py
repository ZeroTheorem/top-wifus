from flask import Flask, render_template

app = Flask(__name__)

score = {
    "Rias": 9.8,
    "Asia": 8.0,
    "Akeno": 9.9,
    "Koneko": 7.0
}


@app.route("/")
def test():
    return render_template("index.html", score=score)


@app.route("/Rias")
def vote_Rias():
    return render_template("vote_Rias.html")


@app.route("/Asia")
def vote_Asia():
    return render_template("vote_Asia.html")


@app.route("/Akeno")
def vote_Akeno():
    return render_template("vote_Akeno.html")


@app.route("/Koneko")
def vote_Koneko():
    return render_template("vote_Koneko.html")


if __name__ == '__main__':
    app.run(debug=True)
