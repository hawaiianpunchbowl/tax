from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import random

app = Flask(__name__)

# Load the CSV file
df = pd.read_csv('tax.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Randomly select a question
        question = df.sample().iloc[0]
        return render_template('index.html', question=question)
    elif request.method == 'POST':
        answer = request.form['answer']
        correct_answer = df.loc[df['Question'] == request.form['question']]['Answer'].iloc[0]
        if answer.lower() == correct_answer.lower():
            return render_template('success.html')
        else:
            return render_template('failure.html', correct_answer=correct_answer)

if __name__ == '__main__':
    app.run(debug=True)
