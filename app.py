
from flask import Flask, render_template, request, redirect, url_for, flash
from database import *
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = "sqlguard_secret_key"

# Create Database
create_database()


# ----------------------------------
# SQL Injection Detection
# ----------------------------------

def detect_sql_injection(user_input):

    patterns = [
        r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
        r"(\bOR\b|\bAND\b).*=.*",
        r"UNION\s+SELECT",
        r"DROP\s+TABLE",
        r"INSERT\s+INTO",
        r"DELETE\s+FROM",
        r"UPDATE\s+.*SET",
        r"EXEC\s+",
        r"xp_cmdshell",
        r"WAITFOR\s+DELAY",
        r"1=1",
        r"admin'--"
    ]

    for pattern in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return True

    return False


# ----------------------------------
# Dashboard
# ----------------------------------

@app.route('/')
def dashboard():

    total_users = get_total_users()

    total_attacks = get_total_attacks()

    logs = get_logs()

    return render_template(
        "index.html",
        users=total_users,
        attacks=total_attacks,
        logs=logs
    )


# ----------------------------------
# Login Page
# ----------------------------------

@app.route('/login')
def login():

    return render_template(
        "login.html"
    )


# ----------------------------------
# Register Page
# ----------------------------------

@app.route('/register')
def register():

    return render_template(
        "register.html"
    )


# ----------------------------------
# SQL Test Lab
# ----------------------------------

@app.route('/testlab')
def testlab():

    return render_template(
        "testlab.html"
    )


# ----------------------------------
# Register User
# ----------------------------------

@app.route('/register_user', methods=["POST"])
def register_user():

    username = request.form["username"]
    email = request.form["email"]
    phone = request.form["phone"]
    password = request.form["password"]

    if add_user(
        username,
        email,
        phone,
        password
    ):

        flash("Registration Successful")

    else:

        flash("Username Already Exists")

    return redirect(
        url_for("register")
    )


# ----------------------------------
# Login User
# ----------------------------------

@app.route('/login_user', methods=["POST"])
def login_user_route():

    username = request.form["username"]
    password = request.form["password"]

    user = login_user(
        username,
        password
    )

    if user:

        flash("Login Successful")

        return redirect(
            url_for("dashboard")
        )

    else:

        flash("Invalid Username or Password")

        return redirect(
            url_for("login")
        )


# ----------------------------------
# SQL Injection Analyzer
# ----------------------------------

@app.route('/analyze', methods=["POST"])
def analyze():

    attack = request.form["attack"]

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    if detect_sql_injection(attack):

        save_attack(
            attack,
            "Blocked",
            current_time
        )

        flash(
            "⚠ SQL Injection Attack Detected!"
        )

    else:

        save_attack(
            attack,
            "Safe",
            current_time
        )

        flash(
            "✓ Safe Input"
        )

    return redirect(
        url_for("testlab")
    )


# ----------------------------------
# View Logs
# ----------------------------------

@app.route('/logs')
def logs():

    data = get_all_logs()

    return render_template(
        "index.html",
        users=get_total_users(),
        attacks=get_total_attacks(),
        logs=data
    )


# ----------------------------------
# Logout
# ----------------------------------

@app.route('/logout')
def logout():

    flash("Logged Out Successfully")

    return redirect(
        url_for("dashboard")
    )


# ----------------------------------
# Run Server
# ----------------------------------

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
