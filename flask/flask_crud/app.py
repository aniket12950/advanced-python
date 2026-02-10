from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    return render_template("index.html")


# 🔍 Search + Sort API (NO REFRESH)
@app.route("/search")
def search():
    query = request.args.get("q", "")
    order = request.args.get("order", "asc")

    order = "ASC" if order == "asc" else "DESC"

    conn = get_db_connection()
    employees = conn.execute(
        f"""
        SELECT * FROM employee
        WHERE name LIKE ?
           OR designation LIKE ?
           OR department LIKE ?
        ORDER BY id {order}
        """,
        (f"%{query}%", f"%{query}%", f"%{query}%")
    ).fetchall()
    conn.close()

    data = [dict(row) for row in employees]
    return jsonify(data)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = (
            request.form["name"],
            request.form["join_date"],
            request.form["salary"],
            request.form["designation"],
            request.form["department"]
        )

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO employee (name, join_date, salary, designation, department)
            VALUES (?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db_connection()
    emp = conn.execute("SELECT * FROM employee WHERE id=?", (id,)).fetchone()

    if request.method == "POST":
        conn.execute("""
            UPDATE employee
            SET name=?, join_date=?, salary=?, designation=?, department=?
            WHERE id=?
        """, (
            request.form["name"],
            request.form["join_date"],
            request.form["salary"],
            request.form["designation"],
            request.form["department"],
            id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    conn.close()
    return render_template("edit.html", employee=emp)


@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM employee WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
