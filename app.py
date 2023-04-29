from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("html/login.html")

@app.route("/login", methods=["POST"])
def login():
    user_name = request.form.get("user_name")
    pass_word = request.form.get("pass_word")
    print(user_name)
    if user_name == "admin" and pass_word == "admin":
        return render_template("html/home.html")
    else:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
