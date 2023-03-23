from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def test():
    score_rias = 9.5
    score_asia = 8.0
    score_akeno = 9.9
    score_koneko = 7.9

    return render_template("index.html", score_rias=score_rias,
                           score_asia=score_asia, score_akeno=score_akeno, score_koneko=score_koneko)


@app.route("/Rias")
def vote_Rias():
    return render_template("vote_Rias.html")


if __name__ == '__main__':
    app.run(debug=True)
