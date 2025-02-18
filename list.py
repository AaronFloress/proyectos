from flask import Flask, render_template, request, redirect, url_for
import pymysql

app=Flask(__name__)

connection=pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    db="tasks"
)

cur=connection.cursor()

@app.route("/")
def index():
    cur.execute("SELECT * FROM LIST")
    pending=cur.fetchall()
    return render_template("index.html", pending=pending)

@app.route("/add", methods=["POST"])
def add():
    new_task=request.form["add_task"]
    new_task=new_task.upper()
    cur.execute("INSERT INTO LIST (pending) VALUES (%s)", (new_task,))
    connection.commit()
    return redirect(url_for("index"))

@app.route("/dele/<pending>")
def dele(pending):
    cur.execute("DELETE FROM LIST WHERE PENDING=%s", (pending,))
    connection.commit()
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
