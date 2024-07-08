from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)


@app.route("/test")
def test():
    return render_template("firstpage.j2")


@app.route("/")
def index():
    user_name = session.get('user_name')
    return render_template("index.html", user_name=user_name)


@app.route("/login", methods=["GET"])
def login_landing():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_action():
    email = request.form.get("email")
    password = request.form.get("password")
    if email == "admin@admin.com":
        if password == "password123":
            session['user_name'] = "admin"
            return redirect('/')
        else:
            redirect('login.j2')
    else:
        redirect('login.j2')
