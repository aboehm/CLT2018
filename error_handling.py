from flask import Flask, abort, redirect, url_for
app = Flask(__name__)

# Behandlung des Statuscodes 404
@app.errorhandler(404)
def error_not_allowed(e):
    return redirect(url_for('index'))

# Die Indexseite
@app.route('/')
def index():
    return 'Hello world!'

# Zugriff auf diese Seite soll verboten sein
@app.route('/secret')
def not_allowed():
    abort(401)

if __name__ == '__main__':
    app.run()
