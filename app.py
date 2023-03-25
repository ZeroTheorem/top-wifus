from flask import Flask, render_template, request, redirect
import sqlite3 as sq


conn = sq.connect("topwifus.bd", check_same_thread=False)
curs = sq.Cursor(conn)


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        result = request.form['vote_Rias']
        curs.execute(f"UPDATE topwifus SET RIAS={result}")
        conn.commit()
        return redirect("/")

    curs.execute("SELECT * FROM topwifus")
    reuslt = curs.fetchone()
    score = {"Rias": reuslt[0],
             "Asia": reuslt[1],
             "Akeno": reuslt[2],
             "Koneko": reuslt[3]}

    return render_template("index.html", score=score)


@app.route("/Rias", methods=['POST', 'GET'])
def vote_Rias():
    if request.method == 'POST':
        result = request.form['vote_Rias']
        curs.execute(f"UPDATE topwifus SET RIAS={result}")
        conn.commit()
        return redirect("/")

    return render_template("vote_Rias.html")


@app.route("/Asia", methods=['POST', 'GET'])
def vote_Asia():
    if request.method == 'POST':
        result = request.form['vote_Asia']
        curs.execute(f"UPDATE topwifus SET ASIA={result}")
        conn.commit()
        return redirect("/")

    return render_template("vote_Asia.html")


@app.route("/Akeno", methods=['POST', 'GET'])
def vote_Akeno():
    if request.method == 'POST':
        result = request.form['vote_Akeno']
        curs.execute(f"UPDATE topwifus SET AKENO={result}")
        conn.commit()
        return redirect("/")

    return render_template("vote_Akeno.html")


@app.route("/Koneko", methods=['POST', 'GET'])
def vote_Koneko():
    if request.method == 'POST':
        result = request.form['vote_Koneko']
        curs.execute(f"UPDATE topwifus SET KONEKO={result}")
        conn.commit()
        return redirect("/")

    return render_template("vote_Koneko.html")


if __name__ == '__main__':
    app.run(debug=True)
