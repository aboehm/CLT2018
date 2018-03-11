from flask import Flask, request
app = Flask(__name__)

@app.route('/any/<arg>')
def no_cast(arg):
    return '%s is not casted' % (arg)

@app.route('/number/<int:arg>')
def a_number(arg):
    return '%i is a number' % (arg)

@app.route('/string/<string:arg>')
def a_any(arg):
    return '%s is a string' % (arg)

