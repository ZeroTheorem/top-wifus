from flask import Flask, render_template, request, redirect
import sqlalchemy as sa
from init_db import topwifus


app = Flask(__name__)
engine = sa.create_engine('sqlite:///topwifus.db')


@app.route("/", methods=['POST', 'GET'])
def test():
    if request.method == "POST":
        for x, y in request.form.items():
            with engine.connect() as conn:
                conn.execute(sa.update(topwifus).where(
                    topwifus.c.name_form == x).values(score=y))
                conn.commit()

    with engine.connect() as conn:
        result = conn.execute(sa.select(topwifus)).fetchall()
    return render_template("index.html", result=sorted(result, reverse=True))


@app.route("/message", methods=['POST', 'GET'])
def message():
    if request.method == 'POST':
        return redirect("/")
    return render_template("message.html")


if __name__ == '__main__':
    app.run(debug=True)
