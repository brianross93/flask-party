"""
Initialize your Flask app. This is what will run your server.

Don't forget to install your dependencies from requirements.txt!
This is a doc string! It's a special kind of comment that is expected
in Python files. Usually, you use this at the top of your code and in
every function & class to explain what the code does.
"""
from flask import Flask, request, render_template, url_for
from guest import Guest
from datetime import datetime, date
from pprint import PrettyPrinter
import requests

app = Flask(__name__)

# Define global variables (stored here for now)
pp = PrettyPrinter(indent=4)
guest_list = []

today = date.today()
month = today.strftime('%m')
year = today.strftime("%Y")

@app.route('/')
def homepage():
    """Return template for home."""
    return render_template('index.html')

@app.route('/about')
def about_page():
    """Show user party information."""
    # Sometimes, a cleaner way to pass variables to templates is to create a
    # context dictionary, and then pass the data in by dictionary key

    # TODO: your request code goes HERE

    # TODO: access name, date, and description for all holidays this month. 
    # HINT: you likely need to loop through the holidays in the data

    holidays = []
    # HINT: in holidays, we'll probably need a way to store key-value pairs.
    # Think about the format we receive the response in
    dates = # TODO: access data from your response
    descriptions = # TODO: access data from your response

    #  TODO: access the data we need from holidays, and make sure we can loop through this information in our template

    context = {
        "holidays": holidays,
        "date": dates,
        "description": descriptions
    }

    return render_template('about.html', **context)


@app.route('/guests', methods=['GET', 'POST'])
def show_guests():
    """
    Show guests that have RSVP'd.

    Add guests to RSVP list if method is POST.
    """
    if request.method == "GET":
        return render_template("guests.html", guests=guest_list)
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        plus_one = request.form.get("plus-one")
        phone = request.form.get("phone")
        costume = request.form.get("costume")
        guest_list.append(Guest(name, email, plus_one, phone,costume))
        return render_template("guests.html", guests=guest_list)


@app.route('/rsvp')
def rsvp_guest():
    """Show form for guests to RSVP for events."""
    return render_template('rsvp.html')


if __name__ == "__main__":
    app.run(debug=True)