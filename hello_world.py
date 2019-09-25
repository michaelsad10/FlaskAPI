from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/hello') 
def print_hello(): 
    return 'Hello'

@app.route('/user/<username>')
def show_user(username):
    return render_template('hello.html', username=username)

@app.route('/about')
def show_about():
    return 'This is the about page'


# with app.test_request_context():
#     print(url_for('hello_world'))
#     print(url_for('print_hello'))
#     print(url_for('show_user', username = 'bofa'))
#     print(url_for('show_about'))