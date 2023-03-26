from flask import Flask, render_template, request, redirect
import sqlite3 as sq


conn = sq.connect("topwifus.bd", check_same_thread=False)
curs = sq.Cursor(conn)


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        if 'vote_Rias' in request.form:
            result = request.form['vote_Rias']
            try:
                curs.execute(f"UPDATE topwifus SET RIAS={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Asia' in request.form:
            result = request.form['vote_Asia']
            try:
                curs.execute(f"UPDATE topwifus SET ASIA={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Akeno' in request.form:
            result = request.form['vote_Akeno']
            try:
                curs.execute(f"UPDATE topwifus SET AKENO={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Koneko' in request.form:
            result = request.form['vote_Koneko']
            try:
                curs.execute(f"UPDATE topwifus SET KONEKO={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Kuroka' in request.form:
            result = request.form['vote_Kuroka']
            try:
                curs.execute(f"UPDATE topwifus SET KUROKA={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Grayfia' in request.form:
            result = request.form['vote_Grayfia']
            try:
                curs.execute(f"UPDATE topwifus SET GRAYFIA={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Serafall' in request.form:
            result = request.form['vote_Serafall']
            try:
                curs.execute(f"UPDATE topwifus SET SERAFALL={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Xenovia' in request.form:
            result = request.form['vote_Xenovia']
            try:
                curs.execute(f"UPDATE topwifus SET XENOVIA={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Irina' in request.form:
            result = request.form['vote_Irina']
            try:
                curs.execute(f"UPDATE topwifus SET IRINA={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Yasaka' in request.form:
            result = request.form['vote_Yasaka']
            try:
                curs.execute(f"UPDATE topwifus SET YASAKA={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Raynare' in request.form:
            result = request.form['vote_Raynare']
            try:
                curs.execute(f"UPDATE topwifus SET RAYNARE={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")

        if 'vote_Rossweisse' in request.form:
            result = request.form['vote_Rossweisse']
            try:
                curs.execute(f"UPDATE topwifus SET ROSSWEISSE={result}")
                conn.commit()
                return redirect("/message")
            except:
                return redirect("/error")
    else:
        curs.execute("SELECT * FROM topwifus")
        result = curs.fetchone()
        score = {"Rias": result[0],
                 "Asia": result[1],
                 "Akeno": result[2],
                 "Koneko": result[3],
                 "Kuroka": result[4],
                 "Grayfia": result[5],
                 "Serafall": result[6],
                 "Xenovia": result[7],
                 "Irina": result[8],
                 "Yasaka": result[9],
                 "Raynare": result[10],
                 "Rossweisse": result[11]}

        return render_template("index.html", score=score)


@app.route("/message", methods=['POST', 'GET'])
def message():
    if request.method == 'POST':
        return redirect("/")
    return render_template("message.html")


@app.route("/error", methods=['POST', 'GET'])
def error():
    if request.method == 'POST':
        return redirect("/")
    return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True)
