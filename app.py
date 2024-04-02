from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    "Как долго ты работаешь в компании?",
    "Используешь ли ты принципы SOLID?",
    "Что делает yield в генераторах?"
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    answers = []
    for question in questions:
        answer = request.form.get(question)
        answers.append(answer)
    return render_template('results.html', answers=answers)


if __name__ == '__main__':
    app.run(debug=True)
