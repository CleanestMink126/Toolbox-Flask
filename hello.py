"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/return',  methods=['POST', 'GET'])
def hello_world():
    print('in method')
    error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # if request.method == 'GET':
    name = request.args.get('Name', '')
    age = request.args.get('Age', '')
    print(name)
    print(age)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('return.html', name=name, age=age)

@app.route('/')
def hello(name=None):
    return render_template('index.html',name = name)



if __name__ == '__main__':
    app.run(debug = True)
