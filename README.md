# Walking in the Lakes

The third Milestone project with the Code Institute to look at the hills and walking in the lake district.

ME and my family have always loved the lake district and enjoy walking. My parents have done a lot of hill climbs and have been trying to climb all the hills in the lake district. I wanted to make something that allowed people to be able to enjoy walking in the lake district, but also be able to monitor the hills they have climbed and which ones they still need to do.

This would be something where you create a profile and be able to monitor your progress but also share your walks, pictures and comments with the rest of the users.

# UX

## Project Goals

As this project is mainly focused around walking, there could be a very open ended age range of users. With this in mind I would like to make the site very easy to read and use for all age groups.

There are lots of walking sites around, showing walks and giving this option to people, so having the extra capability of being able to track the hills you have climbed would be a good thing for some users wanting an end goal. 

## User Stories

As a user of this site I would like:

1. To be able to easily view walks whether I have a profile on the site or not.
2. To be able to easily create a profile if I want to, and be able to change information on it if I needed to.
3. Be able to easily find hills that I am looking for and to be able to to see information and walks linked to those hills.
4. To be able to easily mark off the hills I have climbed and be easily able to see the results when I come back later.
5. Be able to share walks of my own with other users of the site, and be able to go back and edit these in the future.
6. Be able to comment on walks on the site to be able to give advice to other people using the site.
7. Add pictures to the walks I do or comment on to make this a much more eye catching site to enjoy visiting

As an admin of this site, I would like:

1. To be able to control content shared on the site.
2. To be able to edit or remove anything that I do not think is appropriate.
3. Monitor usage of the site. 
4. Be able to help with any issues that people are having with the site, or questions they have. 

## Design Choices

Even though this is mainly focused around the back-end database, I have still tried to make the site look appealing to people and be simple to view and use.

### Icons

* I have tried to use icons as much as possible throughout the site to give a clear understanding of things

### Colors

* I have stuck to a very green based colour scheme which has a very natural feel in relation to the walking in the lake district.
* I have used varying shades to try and give a good effect but keep colours from not able to show font colours.
* Font colours have mainly been white, grey and black, to correspond with certain things sticking out to users and things being visible on the background they appear on. 

### Styling and Background

* The site uses a background image that stays constant through the site and is relevant to the theme. The information sits over the top of this in cards so users can try find sections easily without having to scan through a big long screen full of text.


## Wireframes

With using Materialize and a mostly Databse driven project my layouts were fairly simple and easy to read and use, mainly focusing on card elements down the page.

I created a wireframe for the Home page as I wasnt sure how i wanted this to look.
![Main page Wireframe](/landing_page.png)

Also one for the Profile page as this one contained more information and something that would grow and be usable by the user.
![Profile page Wireframe](/profile.png)


# Features

- Not really a feature but i thought this should be mentioned somewhere. I have used the mongoimport function through the windows command line program to be able to import a csv file with the base information for all the hills. This saved a lot of time of manually inputting hundreds of hills and helped me learn a quick and efficient way to upload data to mongoDB.

Creating the CSV file from excel using headers as the key for the fields. Using the [mongoDB documentation](https://docs.mongodb.com/database-tools/mongoimport/) to set up my PC with the correct path file to allow the computer to communicate with the mongoDB server. In the windows command line, using the code:
 `<mongoimport --db=lakes_walks --collection=hills --type=csv --headerline --file=my_filename.csv>`
 should have worked, but it did not. I did more reading and needed to include the mongoDB URI at the start of this code, which I got and then put in which made the code work and the hundreds of hills had been successfully imported into the database. 


## Existing Features

#### Register
* Allows people to create a user profile for the site to be able to log on and post and monitor their progress.

#### Login / Logout
* Some features are not available if the user is not logged in, this looks in the database to find the user and then posting things will be attributed to this user.

#### Profile
* When a user is logged in they have a profile, which shows their information and then the hills they have climbed and any walks and images they have posted on the site. From here they can go directly to things they want to go back to.
* They can add a profile picture here aswell.

#### Areas, Groups & Hills
* This was the first main feature and has data stored in the database and starts as a dropdown of the areas in the lake district. This takes the used to a page that displays the groups of hills in that areas.
* From these the user can click on a certain hill which displays some information about the hill and an image. 
* There is a button that brings out a menu that allows the user to tick if they have climbed that hill. This will then be shown on their profile page.

#### Walks
* This shows all the walks on the site with a brief overview that allows the user to choose a walk they may want to look at, from here this will take them to a page for that walk.
* Users who are logged in to the site can also publish their own walks. Pressing on the button brings up a modal with fields for filling in and the possibilty to add an image. This walk then gets published to the website for other users to see.

#### Walk information
* This is not avaiable from the navbar, but is the page that is brought up from either the hill page, or walks page. The user sees an overview of the walk and an image, followed by the walk and the return itself.
* All walks can be commented on to allow users to share their experience of the walk or any tips and advice with other people looking at the walk.
* The user logged in can delete comments that they have posted. They can also edit the walk if this is one they have posted. Clicking the button bring up a modal similar to the create walk one that will allow things to be changed. 

#### Gallery
* This is a gallery of pictures that have been uploaded by users. This is just for fun and gives users the possibilty to show off some really nice lake district pictures from their walks.
* Users upload a picture, or multiple pictures from wherever they are by pressing the upload button. 

#### Search
* This displays on the navbar at the top and allows users to look for walks. In here they can type and if there are any walks with this in the walk name, or name of the hill they are about, will show the walks page and filter the walks. 

## Features left to Implenment

#### Pagination
* On both comments and the display of walks I would like to be able to paginate the results show it doesnt show all of them, but havent been able to find the correct methods and code that works with the technologies I havent learnt.

#### Counts
* One of the features is looking at all the hills in the lake district and being able to tick them off if you have climbed them to monitor your progress. I would like to be able to be able to put on a counter that showed how many they had climbed out of however many there is in the area. Did not have time to learn and get this in before deadline.

#### Hill Search
* The search bar only currenrly works for walks. This is ok when a hill has a walk, but not if they dont. However, mongoDB will not allow indexes on different collections to able to search against, or not that I have found yet. There should be a way and I would like to look at this in the future.

#### Data
* Not really a feature, but there are hundreds of hills in the lake district and lots of different walks. Putting all this data in whilst testing and building would not have been able to be done. Also, because of COVID, I have not had chance to travel to the lake district to do any walking or take pictures.

#### Users posting pictures related to a walk
* To be able to have a gallery per walk as people go and try these walks would be nice. Its a nice to have as people can post pictures to the main gallery, but this would be something to link pictures to a walk in the future. 

#### Google Maps API
* This was a nice to have from the start to show a map and have all the hills as points on the map to be able to find them easily. Would be really good to get this included.

#### Ordanance Survery Maps
* For each walk, being able to put down an Ordanance Survey Map that users can download and use for the route would be really useful, but being able to do this is not something I have been able to look at yet. It is a very strong contendar for something I would like to get involved soon, so that users can post these with their walks too.

#### Admin control
* There is an admin user that can delete and edit any data on the site, but this has to be done from the site, it would be nice to have a tool to manage the databse without having to log on and easily monitor and manage the mongoDB aswell. I will also get a way of contacting the admin user built in in the future.

#### Bullet points on walk
* Right now the user can only enter into a text area for the description of the walk, in the future I will put in something that allows them to build a step by step guide but this is not something learnt yet and didnt have time to get it in now. 


# Technologies Used

#### [HTML (Hypertext Markup Language)](https://www.w3schools.com/html/)
- HTML is the standard markup language for programmers to use to display content on a webpage.

#### [CSS (Cascading Style Sheets)](https://www.w3schools.com/css/)
- CSS works alongside HTML to add style and effects to the website.

#### [JavaScript](https://www.w3schools.com/js/default.asp)
- JavaScript enables Interactive web pages and is an essential part of web applications.

#### [jQuery](https://jquery.com/)
- jQuery is a framework that enables easier manipulation of the DOM and i have used this to simplifiy the code from standard JavaScript.

#### [Python](https://www.python.org/)
- Python is a programming language similar to javascript but trying to make code more readble and trying to help programmers with clear and logical code. 

#### [flask](https://flask.palletsprojects.com/en/1.1.x/)
- Flask is a python web framework, sometimes classed as a microframework as there are no particular tools or libraries required. Flask supports extensions to add things to your site and not its own library.

#### [MongoDB](https://www.mongodb.com/)
- MongoDB is a NoSQL database program that use JSON like documents. A document oriented database has no set links between documents but allows for easy storage and retrival of data. 

#### [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- PyMongo is a python tool used for joining python and MongoDb easily and allows easy access to a MongoDB without a python based webpage. 

#### [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
- Werkzeug is a WSGI (Web Server Gateway Interface) web application library that communicates with web applications through Python. I have used this for password hashing and generating

#### [Github](https://github.com/)
- A software development sharing platform used for hosting and sharing projects for open source, or team based projects. I was using github so other people can see, its easily hostable and can deploy easily.

#### [Gitpod](https://www.gitpod.io/)
- An IDE (Integrated Development Environment) for GitHub that lets you quickly launch your projects in a ready-to-code environment.

#### [Git](https://git-scm.com/)
- A free and open source version control system that handles all projects and keeps version history in check.

#### [Font Awesome](https://fontawesome.com/)
- A font and icon based toolkit based on CSS - Wikipedia. I used font awesome icons to give a more visual appearance to the Happiness and Followers, it also gave the user a quick viewing of what was being affected.

#### [Materialize](https://materializecss.com/)
- Materialize is a front-end framework that ocmbines the principles of design, along with new technologies to give a great user experience and help coders create a functional responsive site. I have used this for the basic layout and a lot of the different CSS design elements to make sure this is clear and visible for all users on all devices. 

#### [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
 - A set of Web developer tools built into Google Chrome that allows you to make changes to a website on the fly for testing purposes and be able to diagnose issues. I used this for the console, to be able to view results as changes were made during gameplay. This also allowed me to issue commands to the game to carry on if there was a bug while testing rather than having to start the whole game again. 


# Testing

Testing the User Stories that were previsouly defined in the UX section of the README:

Key: 
- E - Expected
- T - Testing
- R - Results
- F - Fixes 

1. To be able to easily view walks whether I have a profile on the site or not.

    - E. To go to the site as a non user and view the walks on the site at all screen sizes.
    - T. I went to the site from a fresh start and clicked the walks tab on the nav, then clicked on one of the walks on this page. I did this on phone, tablet, laptop and computer size screens with Google Chrome Dev Tools device toolbar.
    - R. The site responded as expcted at all device sizes and the screen layout changed with no issues. Was able to see all the walks and look into an individual walk.

2. To be able to easily create a profile if I want to, and be able to change information on it if I needed to.

    - E. To be able to register easily a new user and view their profile.
    - T. On all devices sizes again, clicked the register button at the top and created 4 new users, using usernames i knew existed and trying to bypass all checks.
    - R. Trying a username I knew existed blocked and sent a flash message. When filling in everything, it was successful and the profile button appeared in the navbar, i clicked it and it took me to a profile showing the users information. I was able to add a profile image to the profile too. This all worked on all device sizes

3. Be able to easily find hills that I am looking for and to be able to to see information and walks linked to those hills.

    - E. Able to search for a hill or walk and get results that can help me navigate to a walk or hill.
    - T. Typing in the search bar a name of a walk I know is on the system or the name of a hill in the lake district.
    - R. Site didnt respond as expected and was only able to show walks.
    - F. No Fix avaiable at the moment. MongoDB does not allow indexes on different collections. this will become a feature to implement and to find out if its possible.

4. To be able to easily mark off the hills I have climbed and be easily able to see the results when I come back later.

    - E. On a hill, pressing the plus and tick button will add this to the list on the users profile page.
    - T. I went to a random hill, pressing the plus and tick button to add this walk to my walks climbed, then going to the profile page to see if it has populated
    - R. Site did not behave as it should have. The group was added to the Easten Fells on the profile and not the Central Fells, I was then reidrected to the Eastern Fells page. Looking in the database, there are two hills called 'Brown Rigg' in different areas. When going to multiple other Hills the site worked exactly as expected.
    - F. There are 3 occurances of hills with the same name, I could not figure out a way to pull the right one through before deadline. So 99% of these work as expected and the few outliers will go into the bugs and features to implement section. 


5. Be able to share walks of my own with other users of the site, and be able to go back and edit these in the future.

    - E. From the walks page, click to add a walk, fill in all the details and then the walk appear on the walks page. Go to this walk, press edit and change a few details, save then check they have changed.
    - T. I went to the walks page, and added a walk, taking  walk from where2walk and pasted the information into the form. Adding a picture to the walk as well then clicking publish to see if the walk appears. Going to this walks page and clicking edit at the top, changing some information and then saving it.
    - R. Adding the walk brought back no errors and it has populated on the walks page. Clicking on the walk takes me to the page for this walk. Edited this walk and the information has changed. Site behaving exactly as expected.


6. Be able to comment on walks on the site to be able to give advice to other people using the site.
     
     - E. Being able to go to a walk and post a comment about this walk, not being able to post if not logged in. Users are able to delete their own comments.
     - T. I went to a walk as a logged in user and wrote a test comment in. I then logged out and tried to post a comment when not logged in.  
     - R. Site responded as expected when logged in, flash message saying the message had been posted and comment posted at the top of the list. Was able to delete comment. When not logged in, got a jinja error as the comment expected a session.user value to post to the database. 
     - F. I added an `<{% if session.user %}>` to the code and under the `<{% else %}>` i disabled the button and added a link to the log in page. Tried to post again and this worked.

7. Add pictures to the walks I do or comment on to make this a much more eye catching site to enjoy visiting.

    - Function not built yet so will go into the features to implement. Users can add pictrues to the gallery and the creater of the walk can upload images, but this isnt available through comments right now. 

## Admin User Testing

- I created an admin user account that overrides the users accounts and has the option to edit and delete comments, walks and gallery images. 

- Right now the admin user can not to contacted with issues, so this becomes a feature to implement.

## Code Checking

I ran all my code through validators to check for errors and apply fixes to them. 

- [HTML validator](https://validator.w3.org/) - ran through, couple of issues, Jinja erors but not sure if validator is capable of seeing these? fixed and re-ran eith no errors (except jinja).
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - No Errors
- [JavaScript Validator](https://jshint.com/) - Few missed Semicolons - Fixed and re-ran with no errors
- [Python Validator](http://pep8online.com/) - Fixed all the line breaks, white spaces and under and over indents - Re-Ran and no errors.

# Bugs Discovered

When on the Gallery or Walks page, the dropdown list for the Areas page did not show any results. The Areas dropdown was on the base document so was not sure why it was only happening on these two pages.
After some searching, the functions that controlled these pages did not have the variable in the render_templates code to populate this list. I added the following bits into these functions.
`<areas = list(mongo.db.areas.find())>`

`<return render_template("gallery.html", images=images, areas=areas)>`

A lot of the time during working and testing the comments, I had issues with comments posting multiple times and them not showing up until the page was refreshed. A long time going through and trying to figure out if there were bugs somewhere, all lead me to see that I had typed `<retun render_templates>` and not `<return redirect>` which seemed to be causing issues and resending forms. Changing the code fixed the issue.

When I was looking to edit walks and I updated them, the page brought back a blank page with no information and sometimes deleted fields. After some testing and reading of the [mongoDB documentation](https://docs.mongodb.com/manual/reference/operator/update/set/), the route needed to include a `<{"$set">` before the array so that it only set the fields in this list and left other exisitng ones alone.

There are 3 sets of hills,(as far as i could see), where there are different hills with the same name, this causes an issue with adding the correct hill to the users profile, sometimes it adds the one from the wrong area. I have tried to sort this before deadline but to no avail so will be something to sort ASAP. The issues is noted but will only happen on those few hills. 


# Deployment

I have depolyed this to heroku taking the following steps:

1. On the [Heroku Wesbite](https://dashboard.heroku.com), clikcing on "New" on the dashboard. Name the app and select the Europe region.

2. When the app has been created, click on the "Deploy" tab, and under the section for "Deployment method", click GitHub.

3. Confirm this link to GitHub, which will update the app based on commits and pushes to GitHub.

4. In the code for the project in Gitpod (or your IDE), create a `<requirements.txt>` file, which stores all the things we are using on the site. Do this by typing `<pip3 freeze --local > requirements.txt>` into your CLI.

5. As well as a requirments files, a `<Procfile>` is also needed to deploy. Create this by typing `<echo web: python app.py>` into your CLI. (`app.py` can be exchanged for the name of your python file, if you have named it `run.py` for example.)

6. Make sure to `<git add .>` and `<git commit -m "...">` these files, then `<git push>`. This will push everything to GitHub which will sync up with heroku. 

7. Back in Heroku under the "Settings" tab, there is a section called "Config Vars", click to reveal these and set the following vars:

Key | Value
----| ----
I.P | 0.0.0.0
MONGO_DBNAME | lakes_walks
MONGO_URI | mongodb+srv://<your_username>:<your_password>@myfirstcluster.0i01h.mongodb.net/<your_db_name>?retryWrites=true&w=majority"
PORT | 5000
SECRET_KEY | <your_secret_key>

8. From your app dahsboard, under "Deploy", make sure Automatic deploys are Enabled, and under "Manual Deploys", the correct branch you want to deploy is selected i.e. master.

9. The site is now successfully deployed. 


# Credits

### ***Content***
- HTML
- CSS
- Javascript
- [jQuery](https://jquery.com/) used this for a lot of my javascript, lots of use of the documentation on there to use it properly.
- [Font Awesome](https://fontawesome.com/) used for logos and icons across the site.
- [Materialize](https://materializecss.com/) I used this as the main layout builder for the website. This provided lots of really useful tools to build a responsive layout as I mainly focused on the database.
- [Code Institute Full Stack Course](https://codeinstitute.net/) - I used the lessons a lot, re-watching videos and going over things again. Some things are based on the task master mini project so there is a lot of similar code.
- [A Codepen piece](https://codepen.io/riki-ar/pen/PLxZxP) That helped me getting the search bar into the nav bar along with all the other elements. 
- [Programiz](https://www.programiz.com/python-programming/function-argument) - Think this should be available somewhere else and was maybe covered on the course, but I found it here for setting default values or null values for fucntion parameters.
- [Where2Walk](https://where2walk.co.uk/) was a really helpful site for inspiration and as I couldnt visit the lake district because of COVID, I took all the walks content from here to be able to push things to the site for submission (These will be removed and one written by myself or others will be put in).
- [Picture Uploads](https://www.youtube.com/watch?v=DsgAuceHha4) - This youtube video was immensley helpful to learn how to upload to MongoDB and then return images to the website.
- [Multiple Picture Uploads](https://tutorial101.blogspot.com/2020/02/python-flask-multiple-files-upload.html) - This was something I wanted to make possible so this tutorial video and code was really good at helping me understand how it worked.
- [Stack Overflow](https://stackoverflow.com/questions/9578348/best-way-to-execute-js-only-on-specific-page) helped me get rid of an error that was occuring with everypage trying to run some JavaScript on textarea that didnt exist. This helped make it so that code only ran on the one page.
 - [MongoDB syntax](https://stackoverflow.com/questions/49658679/eq-invalid-syntax-mongo-db) - From reading the mongoDB documents things were not working, but this article helped me note the differences.
 - [Nested Collapsibles](https://stackoverflow.com/questions/32506226/nested-collapsibles-with-materialize) and [Group By](https://jbmoelker.github.io/jinja-compat-tests/filters/groupby/) - These two things helped with calling the list of walks people had done onto their profile as this was coming from a nested array and  would need to bring back values into a Materialize collapsible with 3 layers not just 2.

### ***Media***
- Haweswater reservoir image taken from [country living website](https://www.countryliving.com/uk/wildlife/countryside/a22099046/lost-cumbrian-village-mardale-green-heatwave-dries-haweswater-reservoir/)
- [High Street](https://en.wikipedia.org/wiki/High_Street_(Lake_District)) picture came from Wikipedia.
- [Blencathra](https://www.sallyscottages.co.uk/blog/blencathra-easy-way) picture came from Sally Cottages website.
- [Causey Pike](https://en.wikipedia.org/wiki/Causey_Pike) picture came from wikipedia.
- [St Sunday Crag](https://en.wikipedia.org/wiki/St_Sunday_Crag) picture came from wikipedia.
- [Derwentwater](https://en.wikipedia.org/wiki/Derwentwater) picture came from wikipedia. 
- [Ullswater](https://en.wikipedia.org/wiki/Ullswater) picture came from wikipedia.
- All other pictures on the site were taken by myself. 

### ***Acknowledgements***
- My parents for dragging me up hills and taking me to the lake district a lot growing up to help me build a love for it to inspire this project. 
- My girlfriend Steph for putting up with me through all this but being really positive and supportive of my work. Obviously my cat Kyra....who decides to steal my mouse and re-write the code, but keeping me company most of the day too.
- Other students and tutors on th course, helping and happy to share their projects and support for inspiration and keeping me sane. 
- My mentor Gerry McBride for the support, staying calm which helped me and even through all this current worldwide mess, being really helpful and there when needed even with his own work.





issue on updating and only updating fields there were noted

