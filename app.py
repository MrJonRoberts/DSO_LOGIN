from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "flaskLogin"
app.config['SESSION_TYPE'] = 'filesystem'
@app.before_first_request
def before_first_request_func():
    session['isLoggedIn'] = False

@app.route('/')
def home():  # put application's code here
    if session['isLoggedIn'] == True:

        return render_template("home.html")
    else:
        return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    # only get here if POST form.
    username = request.form['uname']
    password = request.form['pwd']

    if username == "bob" and password == "1234":
        session['isLoggedIn'] = True
        session['user'] = username
        return render_template("home.html")
    else:
        return render_template("login.html", msg="WRONG USER or PWD")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
