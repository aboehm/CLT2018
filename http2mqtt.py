# A HTTP MQTT proxy
# Alexander Böhm <alexander.boehm <AT> malbolge.net> (2018)
#
# HOWTO:
#
# * connect to local Mosquito-Server
#
#   curl http://localhost:5000/connect/localhost
#
# * publish under the topic 'my/topic' the value '123'
#
#   curl http://localhost:5000/publish/my/topic/123
#
# * disconnect
#
#   curl http://localhost:5000/disconnect
#

from flask import Flask
import paho.mqtt.client as mqtt

app = Flask(__name__)
app.client = mqtt.Client()
app.default_server = 'localhost'
app.default_port = 1883
app.default_timeout = 60


@app.route('/')
def index():
    return 'A stupid simple HTTP MQTT proxy'


@app.route('/connect')
def connect():
    connect_with_host_port_timeout(
        app.default_server,
        app.default_port,
        app.default_timeout
    )
    return 'ok\n'


@app.route('/connect/<string:host>')
def connect_with_host(host):
    connect_with_host_port_timeout(
        host,
        app.default_port,
        app.default_timeout
    )
    return 'ok\n'


@app.route('/connect/<string:host>/<int:port>')
def connect_with_host_port(host, port):
    connect_with_host_port_timeout(
        host,
        port,
        app.default_timeout
    )
    return 'ok\n'


@app.route('/connect/<string:host>/<int:port>/<int:timeout>')
def connect_with_host_port_timeout(host, port, timeout):
    app.client.loop_stop()
    app.client.disconnect()

    app.client.connect("localhost", 1883, 60)
    app.client.loop_start()
    return 'ok\n'


@app.route('/disconnect')
def disconnect():
    app.client.loop_stop()
    app.client.disconnect()
    return 'ok\n'


@app.route('/publish/<path:topic>/<string:value>')
def publish(topic, value):
    print('Got message for topic \'%s\' with value \'%s\'' % (topic, value))
    app.client.publish("/%s" % (topic), value)
    return 'ok\n'


if __name__ == '__main__':
    app.run()
