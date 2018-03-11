from flask import Flask, Blueprint, render_template
app = Flask(__name__)


page_blueprint = Blueprint('page', __name__,
                           template_folder='templates/page')


@page_blueprint.route('/show/<int:page>')
def page_show(page):
    #  Seite anzeigen
    return render_template('show.html', page=page)


@page_blueprint.route('/new/<string:name>')
def page_new(name):
    # Seite anlegen
    return render_template('new.html', name=name)


user_blueprint = Blueprint('user', __name__,
                           template_folder='templates/user')


@user_blueprint.route('/login')
def user_login():
    # Nutzer anmelden
    return render_template('login.html')


app.register_blueprint(page_blueprint,
                       url_prefix='/page')

app.register_blueprint(user_blueprint,
                       url_prefix='/user')


if __name__ == '__main__':
    # Applikation starten
    app.run()
