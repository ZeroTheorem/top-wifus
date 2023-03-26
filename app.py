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
            curs.execute(f"UPDATE topwifus SET RIAS={result}")
            conn.commit()

        if 'vote_Asia' in request.form:
            result = request.form['vote_Asia']
            curs.execute(f"UPDATE topwifus SET ASIA={result}")
            conn.commit()

        if 'vote_Akeno' in request.form:
            result = request.form['vote_Akeno']
            curs.execute(f"UPDATE topwifus SET AKENO={result}")
            conn.commit()

        if 'vote_Koneko' in request.form:
            result = request.form['vote_Koneko']
            curs.execute(f"UPDATE topwifus SET KONEKO={result}")
            conn.commit()

        if 'vote_Kuroka' in request.form:
            result = request.form['vote_Kuroka']
            curs.execute(f"UPDATE topwifus SET KUROKA={result}")
            conn.commit()

        if 'vote_Grayfia' in request.form:
            result = request.form['vote_Grayfia']
            curs.execute(f"UPDATE topwifus SET GRAYFIA={result}")
            conn.commit()

        if 'vote_Serafall' in request.form:
            result = request.form['vote_Serafall']
            curs.execute(f"UPDATE topwifus SET SERAFALL={result}")
            conn.commit()

        if 'vote_Xenovia' in request.form:
            result = request.form['vote_Xenovia']
            curs.execute(f"UPDATE topwifus SET XENOVIA={result}")
            conn.commit()

        if 'vote_Irina' in request.form:
            result = request.form['vote_Irina']
            curs.execute(f"UPDATE topwifus SET IRINA={result}")
            conn.commit()

        if 'vote_Yasaka' in request.form:
            result = request.form['vote_Yasaka']
            curs.execute(f"UPDATE topwifus SET YASAKA={result}")
            conn.commit()

        if 'vote_Raynare' in request.form:
            result = request.form['vote_Raynare']
            curs.execute(f"UPDATE topwifus SET RAYNARE={result}")
            conn.commit()

        if 'vote_Rossweisse' in request.form:
            result = request.form['vote_Rossweisse']
            curs.execute(f"UPDATE topwifus SET ROSSWEISSE={result}")
            conn.commit()

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


if __name__ == '__main__':
    app.run(debug=True)
