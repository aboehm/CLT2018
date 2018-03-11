# Flask importieren
from flask import Flask

# Flask-Applikation initialisieren
app = Flask(__name__)

# Route zum Index festlegen
@app.route('/')

# Behandlungsmethode definieren
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    # Applikation starten
    app.run()
