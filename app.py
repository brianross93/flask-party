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
yes_rsvp = 'Yes'
no_rsvp = 'No'
#Making Guest List a global variable so all the functions can access it if they want to
guest_friends = [
        {
            'name': "Benny",
            'rsvp': "Yes",
            'plus_one': "Karen",
            'meal': "Chicken"
        },
        {
            'name': "Jose",
            'rsvp': "Yes",
            'plus_one': "Tara",
            'meal': "Vegetarian"
        },
        {
            'name': "Barney",
            'rsvp': "Yes",
            'plus_one': "Taylor",
            'meal': "Chicken"
        }
    ]
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
@app.route("/rsvp")
def rsvp():
    
    return render_template("rsvp.html", coming=yes_rsvp, busy=no_rsvp)

# Runs code
if __name__ == "__main__":
    app.run(debug=True)
