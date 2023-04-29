from flask import Flask
from flask import render_template
#import email
import os
import time 
#import smtplib, ssl
from email.message import * 
from flask import request

# input feilds user_name ; pass_word

em = EmailMessage()
app = Flask(__name__)
 
 # fg
@app.route("/")
def index():
    return  render_template("html/login.html") 


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4000,debug=True)