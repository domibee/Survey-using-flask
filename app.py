from flask import Flask, request, flash, render_template, redirect 
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickens"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

RESPONSES = []

@app.route('/')
def homepage():
    """Show home page of the survey"""

    return render_template("home.html", survey=survey)

@app.route('/begin', methods=["POST"])
def start_survey():
    return redirect('/questions/0')

@app.route('/questions/<int:qid>')
def answer_questions(qid):

    if (RESPONSES is None):
        return redirect ('/')
    
    if (len(RESPONSES) == len(survey.questions)):
        return redirect ('/complete')
    
    if (len(RESPONSES) != qid):
        flash("Question accessed out of order")
        return redirect(f'questions/{len(RESPONSES)}')
    
    question = survey.questions[qid]
    return render_template('questions.html',question=question, question_num=qid)

@app.route('/answer', methods=["POST"])
def answer():
    choice = request.form["answer"]
    RESPONSES.append(choice)
    return redirect(f'questions/{len(RESPONSES)}')

@app.route('/complete')
def complete():
    return render_template('complete.html')
