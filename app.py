from flask import Flask, request, flash, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "ssd3fg3465dfg"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

RESPONSES = 'responses'

@app.route('/')
def homepage():
    """Show home page of the survey"""
    session[RESPONSES] = []
    
    return render_template("home.html", survey=survey)

@app.route('/begin', methods=["POST"])
def start_survey():

    session[RESPONSES] = []
    return redirect('/questions/0')

@app.route('/answer', methods=["POST"])
def answer():
    
    choice = request.form["answer"]
    responses = session[RESPONSES]
    responses.append(choice)
    session[RESPONSES] = responses
    return redirect(f'questions/{len(responses)}')

@app.route('/questions/<int:qid>')
def answer_questions(qid):

    responses = session.get(RESPONSES)

    if (responses is None):
        return redirect ('/')
    
    if (len(responses) == len(survey.questions)):
        return redirect ('/complete')
    
    if (len(responses) != qid):
        flash("Question accessed out of order")
        return redirect(f'/questions/{len(responses)}')
    
    question = survey.questions[qid]
    return render_template('questions.html',question=question, question_num=qid)

@app.route('/complete')
def complete():
    return render_template('complete.html')
