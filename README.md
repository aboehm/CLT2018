# Webservices mit Python Flask (CLT2018)

Folien und Beispiel für die Chemnitzer Linux-Tage 2018

## Beschreibung

Flask ist ein Framework zur Entwicklung von Webservices mit Python. Zusätzliche Werkzeuge oder eine lange Kette von Abhängigkeiten benötigt es dafür nicht, zudem zeichnet es sich durch seine einfache und unkomplizierte Handhabung aus. Im Vortrag werden die grundlegenden Konzepte hinter Flask vorgestellt, um Webservices zu erstellen und sie sinnvoll zu strukturieren.

## Beispiele

* hello_world.py: Hello World
* hello_world_json.py: Hello World mit JSON-Rückgabe
* only_post_allowed.py: Einschränkung von Methodenaufrufen
* param_route.py: Parametrisierte Routen
* template.py: Nutzung von Templates
* blueprint.py: Nutzung von Blueprints
* error_handling.py: Handhabung von Fehlern
* http2mqtt.py: Ein HTTP-Mosquitto-Proxy

## Ausführung

### Direkt

* Flask über pip installieren

```bash
pip install flask
```

* Hello world ausführen

```bash
FLASK_RUN=hello_world.py flask run
```

### Mit pipenv

* Environment vorbereiten

```bash
pipenv install
```
    
* Anwendung ausführen

```bash
pipenv run python hello_world.py
```
