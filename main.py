import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from model.nflteam import initNFLTeams

# setup APIs
from api.nflteam import nflteam_api # Blueprint import api definition

# register URIs
app.register_blueprint(nflteam_api) # register app pages

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/nflteams')  # connects /stub/ URL to stub() function
def nflteams():
    return render_template("nfllstat.html")

@app.before_first_request
def activate_job():
    initNFLTeams()

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volumes/sqlite.db'
    app.run(debug=True, host="0.0.0.0", port="8086")
    initNFLTeams()
