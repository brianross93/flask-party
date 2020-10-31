"""
This code is used to display a guest list of who is coming to 
my birthday party. This is a project to learn Flask
"""
from flask import Flask, render_template


# This code initializes a basic flask application.

app = Flask(__name__)

#Variables for all the functions to use to pass into HTML
my_name = 'Brian'
date = 'April 10'
time = '12:00 AM'
#Making Guest List a global variable so all the functions can access it if they want to
guest_friends = []
# Homepage function to display my name
@app.route('/')
def homepage():
    """Return template for home."""
    return render_template('index.html', name=my_name)

# Code for About Page
@app.route("/about")
def about():

    return render_template('about.html', time=time, date=date)

# Display Guests who are coming
@app.route("/guests")
def guests():
    return render_template("guests.html", posts=guest_friends)

# Display RSVP status
@app.route("/rsvp", methods=['GET', 'POST'])
def rsvp():
    if request is 'GET':
        return render_template("rsvp.html", guest_friends=guest_friends)
  else:
    add new guest to list
    then, show the updated list
    return render_template("rsvp.html", guest_friends=guest_friends)

# Runs code
if __name__ == "__main__":
    app.run(debug=True)
