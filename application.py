import flask
import os
import time
import threading

from flask import render_template
from flask import request
from flask import Flask
from flask import redirect
from flask import url_for
from flask import abort
from flask import session
from flask import send_from_directory

 
application = flask.Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
application.debug=True

from flask import Flask
application = Flask(__name__)  # Change assignment here

@application.route("/")        # Change your route statements
def hello():         
    return "Hello World!"

if __name__ == "__main__":         
    application.run() 
 
# if __name__ == '__main__':
#     application.run(host='0.0.0.0', debug=True)