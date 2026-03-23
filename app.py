from flask import Flask, render_template, request, url_for, redirect
from connections import session
from models import Todo

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']

        my_todo = Todo(title=title, description=description)
        session.add(my_todo)
        session.commit()

        return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)