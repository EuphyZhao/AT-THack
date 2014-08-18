import flask
# import os
# import time
# import threading

from flask import render_template
from flask import request
from flask import Flask
from flask import redirect
from flask import url_for
from flask import abort
from flask import session
from flask import send_from_directory

# from werkzeug import secure_filename

# from flask_oauth import OAuth
 
application = flask.Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
application.debug=True

# @application.route('/')
# def hello_world():
#     return "Hello world!"
    
@application.errorhandler(404)
def page_not_found(error):
	return 'This page does not exist', 404

@application.route('/test')
def testTranscoder():
	return "test"

@application.route('/home')
def home_page():
    return render_template('index.html')

@application.route('/childprofile')
def child_profile():
    return render_template('child_profile.html')

@application.route('/')
def landing_page():
    return render_template('landingpage.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)