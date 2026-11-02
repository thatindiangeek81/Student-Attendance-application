from flask import Flask, render_template, request
from attendance import attendance, attendance_report

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin123":
            return render_template("dashboard.html", percent=attendance(18, 24), report=attendance_report(attendance(18, 24)))
        message = "Invalid credentials"
    return render_template("login.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
