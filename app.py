from flask import Flask, request, flash, render_template, redirect 
# from flask_debugtoolbar import DebugToolbarExtension
# from surveys import satisfaction_survey as survey

app = Flask(__name__)
# app.config['SECRET_KEY'] = "chickens"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

RESPONSES = []

@app.route('/')
def homepage():
    """Show home page of the survey"""
    return render_template("base.html")

