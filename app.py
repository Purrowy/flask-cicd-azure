from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    return f'Hello {name}, you are {age} years old!'



if __name__ == '__main__':
    app.run(debug=True)