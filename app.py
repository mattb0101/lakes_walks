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

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    """
    Starting route to bring back main index page. Areas variable added to all
    pages that have a navbar as this is there to control the
    dropdown menu on the Areas button.
    """
    areas = list(mongo.db.areas.find())
    return render_template("index.html", areas=areas)


@app.route("/area/<area_name>/<hill_name>")
def area(area_name, hill_name):
    """
    This is the route from clicking one of the areas that will
    bring you to a page with a collection involving areas, groups and hills.
    The same page is used when a single hill is pressed and will
    populate data so needs one hill bringing through as well
    """
    groups = list(mongo.db.groups.find({"area": area_name}))
    areas = list(mongo.db.areas.find())
    area = mongo.db.areas.find_one({"area": area_name})
    hills = list(mongo.db.hills.find({"area": area_name}))
    hill = mongo.db.hills.find_one({"name": hill_name})

    return render_template("areas.html", hills=hills, areas=areas,
                           area=area, groups=groups, hill=hill)


@app.route("/load_image/<filename>")
def load_image(filename):
    """
    Code used across the site to call images back from the database
    """
    return mongo.send_file(filename)


@app.route("/walks")
def walks():
    """
    This will display all the walks avaiable on the database
    """
    areas = list(mongo.db.areas.find())
    walks = list(mongo.db.walks.find())
    return render_template("walks.html", walks=walks, areas=areas)


@app.route("/walk/<walk_name>")
def walk(walk_name):
    """
    When a single walk is clicked on, this generates a new page
    with the details of that walk, also any comments that
    have been posted against this walk
    """
    areas = list(mongo.db.areas.find())
    walk = mongo.db.walks.find_one({"walk_name": walk_name})
    comments = list(mongo.db.comments.find())
    if walk:
        return render_template("walk.html", walk=walk,
                               areas=areas, comments=comments)

    # Not all the hills have walks, so a 404 error page was created
    # if that hill doesnt currently have a walk.
    else:
        return render_template("404.html")


@app.route("/publish_walk", methods=["GET", "POST"])
def publish_walk():
    """
    From the Walks page, a user can create their own walk.
    A modal will create this and push the data into the MongoDb
    along with an image if the user chooses one.
    """
    if request.method == "POST":
        if 'walk_image' in request.files:
            walk_image = request.files['walk_image']
            mongo.save_file(walk_image.filename, walk_image)

            walk = {
                "walk_name": request.form.get("walk_name"),
                "walk_header": request.form.get("overview"),
                "walk_main_text1": request.form.get("walk"),
                "walk_return": request.form.get("return"),
                "walk_difficulty": request.form.get("difficulty"),
                "user_created": session["user"],
                "walk_image_name": walk_image.filename
            }
            flash("Thanks for sharing your walk with us!")

            mongo.db.walks.insert_one(walk)
            return redirect(url_for('walks'))

        return redirect(url_for('walks'))


@app.route("/edit_walk/<walk_id>", methods=["GET", "POST"])
def edit_walk(walk_id):
    """
    Users can edit their own walks so this brings back
    and pushes the updated fields only back to the database.
    """
    if request.method == "POST":
        walk = {"$set": {
            "walk_name": request.form.get("walk_name"),
            "walk_header": request.form.get("overview"),
            "walk_main_text1": request.form.get("walk"),
            "walk_return": request.form.get("return"),
            "walk_difficulty": request.form.get("difficulty")
        }}
        flash("This walk has been updated")

        mongo.db.walks.update({"_id": ObjectId(walk_id)}, walk)
        return redirect(url_for('walk',
                                walk_name=request.form.get("walk_name")))


@app.route("/delete_walk/<walk_id>", methods=["GET", "POST"])
def delete_walk(walk_id):
    """
    Delting a walk if a user decides they dont want it anymore.
    """
    if request.method == "POST":
        mongo.db.walks.delete_one({"_id": ObjectId(walk_id)})
    return redirect(url_for('walks'))


@app.route("/hill_check/<area_name>/<hill_name>/<group_name>",
           methods=["GET", "POST"])
def hill_check(area_name, hill_name, group_name):
    """
    One of the main features of the site is to be
    able to check off the hills that a user has walked.
    From a walk page this will populate into the user
    table in an array that contains the new information.
    """
    groups = list(mongo.db.groups.find({"area": area_name}))
    areas = list(mongo.db.areas.find())
    area = mongo.db.areas.find_one({"area": area_name})
    hills = list(mongo.db.hills.find({"area": area_name}))
    hill = mongo.db.hills.find_one({"name": hill_name})

    already_checked = mongo.db.users.find_one(
        {"username": session["user"], "hills_walked.hill_name": hill_name,
         "hills_walked.group_name": group_name})

    # Check to see if the hill has already been checked,
    # to oppose creating multiple values
    if already_checked:
        flash("You have already checked this hill!")
        return render_template("areas.html", hills=hills, areas=areas,
                               area=area, groups=groups, hill=hill)

    mongo.db.users.update(
        {"username": session["user"]},
        {"$push": {"hills_walked": {"$each": [
                        {"hill_name": hill_name, "area_name": area_name,
                         "group_name": group_name}]}}})

    flash("Yes I have walked this hill")
    return render_template("areas.html", hills=hills, areas=areas,
                           area=area, groups=groups, hill=hill)


@app.route("/user_comment/<walk_name>", methods=["GET", "POST"])
def user_comment(walk_name):
    """
    On walks, users can post comments so this takes the information
    and pushes that into the database so that this can be recalled
    when users view that walk.
    """
    areas = list(mongo.db.areas.find())
    walk = mongo.db.walks.find_one({"walk_name": walk_name})
    comments = list(mongo.db.comments.find())

    # Date and time stamp used so that the latest comments
    # will appear at the top.
    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M")

    if request.method == "POST":
        comment = {
            "walk": walk_name,
            "posted": timestamp,
            "author": session["user"],
            "comment_text": request.form.get("user_comment")
        }
        mongo.db.comments.insert_one(comment)

        flash("Comment Posted")
        return redirect(url_for("walk", walk_name=walk_name))

    return render_template("walk.html", walk=walk,
                           areas=areas, comments=comments)


@app.route("/delete_comment/<walk_name>/<comment_id>", methods=["GET", "POST"])
def delete_comment(walk_name, comment_id):
    """
    Users able to delete comments that they have made.
    """
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    flash("Comment Deleted")

    return redirect(url_for("walk", walk_name=walk_name))


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search box in the navbar uses an index on the walks collection
    and will populate the walks sheet with only walks that
    match the search criteria. The index looks for walk name and hill name.
    """
    search = request.form.get("search")
    walks = list(mongo.db.walks.find({"$text": {"$search": search}}))
    return render_template("walks.html", walks=walks)


@app.route("/gallery")
def gallery():
    """
    Page that displays all the images that have been uploaded to the database
    """
    areas = list(mongo.db.areas.find())
    images = list(mongo.db.images.find())

    return render_template("gallery.html", images=images, areas=areas)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    """
    Users can upload an image that will display on their profile.
    """
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.update({"username": session["user"]}, {"$set": {
                                "profile_image_name": profile_image.filename}})

        flash("Image uploaded")
        return redirect(url_for('profile', username=session["user"]))


@app.route("/upload_many", methods=["GET", "POST"])
def upload_many():
    """
    On the gallery page, users can upload images,
    this allows them to be able to upload multiple images at the same time.
    """
    if request.method == "POST":
        if "gallery_images[]" in request.files:
            gallery_images = request.files.getlist('gallery_images[]')
            for gallery_image in gallery_images:
                mongo.save_file(gallery_image.filename, gallery_image)
                mongo.db.images.insert({"username":
                                       session["user"], "gallery_image_name":
                                       gallery_image.filename})

            flash("Images uploaded")
            return redirect(url_for('gallery'))

    return render_template("gallery.html")


@app.route("/delete_image/<image_id>")
def delete_image(image_id):
    """
    The user can delete images that they have posted
    """
    mongo.db.images.remove({"_id": ObjectId(image_id)})
    return redirect(url_for('gallery'))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    a page that only the user can see when logged on,
    this will show their information and a collection of walks
    they have uploaded, along with all the hills they have climbed.
    """
    areas = list(mongo.db.areas.find())
    user = mongo.db.users.find_one({"username": username})
    walks = list(mongo.db.walks.find())

    # Get the session users username to determine the result
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username,
                               areas=areas, user=user, walks=walks)

    return redirect(url_for('login'))


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Login page that asks for username and password,
    checks if the username exists, then uses Werkzeug to
    check the password hash for security.
    """
    areas = list(mongo.db.areas.find())

    if request.method == "POST":
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user:
            if check_password_hash(user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Successfully logged in, welcome back")
                return redirect(url_for("profile", username=session["user"],
                                areas=areas))

            # Lets the user know if their password is incorrect.
            else:
                flash("password wrong")
                return redirect(url_for("login"))

        # Lets the user know if their username doesnt exist.
        else:
            flash("username doesnt exist")
            return redirect(url_for("login"))

    return render_template("login.html", areas=areas)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    People have to have a user account to upload pictures
    and post comments. Users register here to create an account.
    """
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

        return redirect(url_for("profile"))

    return render_template("register.html", areas=areas)


@app.route("/logout")
def logout():
    """
    Code to remove the user from the session.
    """
    flash("Logged out. Happy Walking!")
    session.pop("user")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
