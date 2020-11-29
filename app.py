import os
from flask import (
    Flask, flash, render_template, url_for,
    redirect, request, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MOINGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    areas = list(mongo.db.areas.find())
    return render_template("index.html", areas=areas)


@app.route("/area/<area_name>/<hill_name>")
def area(area_name, hill_name):
    groups = list(mongo.db.groups.find({"area": area_name}))
    areas = list(mongo.db.areas.find())
    area = mongo.db.areas.find_one({"area": area_name})
    hills = list(mongo.db.hills.find({"area": area_name}))
    hill = mongo.db.hills.find_one({"name": hill_name})
    comments = list(mongo.db.comments.find())
    return render_template(
        "areas.html", hills=hills, areas=areas,
         area=area, groups=groups, hill=hill, comments=comments)


@app.route("/login", methods=["GET", "POST"])
def login():
    areas = list(mongo.db.areas.find())

    if request.method == "POST":
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user:
            if check_password_hash(
                user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Successfully logged in, welcome back")
                return redirect(url_for("profile", username=session["user"], areas=areas))
            
            else:
                flash("password wrong")
                return redirect(url_for("login"))

        else:
            flash("username doesnt exist")
            return redirect(url_for("login"))

    return render_template("login.html", areas=areas)


@app.route("/register", methods=["GET", "POST"])
def register():
    areas = list(mongo.db.areas.find())

    if request.method == "POST":
        # Checks if the username already exists in Database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if the username already exists then display a 
        # flash message telling the user
        if existing_user:
            flash("This username already exists, please choose another")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)

        # putting the new user into the 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        # This return just goes to the index right now, havent built any kind of profile page
        return redirect(url_for("index"))
    return render_template("register.html", areas=areas)


@app.route("/logout")
def logout():
    areas = list(mongo.db.areas.find())

    flash("Logged out. Happy Walking!")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    areas = list(mongo.db.areas.find())

    # gab session users username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username, areas=areas)
    
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # Make sure this set to false when deployed!
