from flask import Flask, request
app = Flask(__name__)


# Nur POST-Anfragen erlauben
@app.route('/', methods=['POST'])
def only_post_allowed():
    # Parameter auslesen
    param1 = request.args.get('param1')

    return 'It\'s a POST with arg1 set to %s' % (param1)
