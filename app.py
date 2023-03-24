from flask import Flask, render_template, request, redirect

app = Flask(__name__)

score = {
    "Rias": 9.0,
    "Asia": 8.0,
    "Akeno": 9.9,
    "Koneko": 7.0
}


@app.route("/")
def test():
    return render_template("index.html", score=score)


@app.route("/Rias", methods=['POST', 'GET'])
def vote_Rias():
    if request.method == 'POST':
        score_Rias = request.form['vote_Rias']
        score["Rias"] = score_Rias
        return redirect("/")

    return render_template("vote_Rias.html")


@app.route("/Asia", methods=['POST', 'GET'])
def vote_Asia():
    if request.method == 'POST':
        score_Asia = request.form['vote_Asia']
        score["Asia"] = score_Asia
        return redirect("/")

    return render_template("vote_Asia.html")


@app.route("/Akeno", methods=['POST', 'GET'])
def vote_Akeno():
    if request.method == 'POST':
        score_Akeno = request.form['vote_Akeno']
        score["Akeno"] = score_Akeno
        return redirect("/")

    return render_template("vote_Akeno.html")


@app.route("/Koneko", methods=['POST', 'GET'])
def vote_Koneko():
    if request.method == 'POST':
        score_Koneko = request.form['vote_Koneko']
        score["Koneko"] = score_Koneko
        return redirect("/")

    return render_template("vote_Koneko.html")


if __name__ == '__main__':
    app.run(debug=True)
