import os
from datetime import datetime
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


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.update({"username": session["user"]},
         { "$set": {"profile_image_name": profile_image.filename}})

        flash("Image uploaded")
        return redirect(url_for('profile', username=session["user"]))


@app.route("/area/<area_name>/<hill_name>")
def area(area_name, hill_name):
    groups = list(mongo.db.groups.find({"area": area_name}))
    areas = list(mongo.db.areas.find())
    area = mongo.db.areas.find_one({"area": area_name})
    hills = list(mongo.db.hills.find({"area": area_name}))
    hill = mongo.db.hills.find_one({"name": hill_name})
    
    return render_template(
        "areas.html", hills=hills, areas=areas,
         area=area, groups=groups, hill=hill)


@app.route("/file/<filename>")
def file(filename):
    return mongo.send_file(filename)


@app.route("/walk/<hill_name>")
def walk(hill_name):
    areas = list(mongo.db.areas.find())
    walk = mongo.db.walks.find_one({"hill_name": hill_name})
    comments = list(mongo.db.comments.find())
    return render_template("walk.html", walk=walk, areas=areas, comments=comments)


@app.route("/hill_check/<area_name>/<hill_name>/<group_name>", methods=["GET", "POST"])
def hill_check(area_name, hill_name, group_name):
    groups = list(mongo.db.groups.find({"area": area_name}))
    areas = list(mongo.db.areas.find())
    area = mongo.db.areas.find_one({"area": area_name})
    hills = list(mongo.db.hills.find({"area": area_name}))
    hill = mongo.db.hills.find_one({"name": hill_name})

    already_checked = mongo.db.users.find_one(
        {"username": session["user"], "hills_walked.hill_name": hill_name})

    if already_checked:
        flash("You have already checked this hill!")
        return render_template(
            "areas.html", hills=hills, areas=areas, area=area, groups=groups, hill=hill)

    mongo.db.users.update(
        {"username": session["user"]},
        {
            "$push": {
                "hills_walked": {
                    "$each": [
                        {"hill_name": hill_name, "area_name": area_name, "group_name": group_name}]
                }
            }
        }
    )

    flash("Yes I have walked this hill")
    return render_template(
        "areas.html", hills=hills, areas=areas, area=area, groups=groups, hill=hill)


@app.route("/user_comment/<hill_name>", methods=["GET", "POST"])
def user_comment(hill_name):
    areas = list(mongo.db.areas.find())
    walk = mongo.db.walks.find_one({"hill_name": hill_name})
    comments = list(mongo.db.comments.find())
    timestamp = datetime.now().strftime("%d/%m/%Y")
    user = mongo.db.users.find({"username": session["user"]})
    
    if request.method == "POST":
        comment = {
            "hill": hill_name,
            "posted": timestamp,
            "author": session["user"],
            "comment_text": request.form.get("user_comment")
        }
        mongo.db.comments.insert_one(comment)

        flash("Comment Posted")
        return render_template("walk.html", walk=walk,
         areas=areas, comments=comments, user=user)

    return render_template("walk.html", walk=walk,
     areas=areas, comments=comments, user=user)


@app.route("/delete_comment/<hill_name>/<comment_id>", methods=["GET", "POST"])
def delete_comment(hill_name, comment_id):
    areas = list(mongo.db.areas.find())
    walk = mongo.db.walks.find_one({"hill_name": hill_name})
    comments = list(mongo.db.comments.find())

    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    flash("Comment Deleted")

    return render_template("walk.html", walk=walk, areas=areas, comments=comments)


@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search_results.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    areas = list(mongo.db.areas.find())
    user = mongo.db.users.find_one({"username": username})

    # gab session users username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username, areas=areas, user=user)
    
    return redirect(url_for('login'))


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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # Make sure this set to false when deployed!
