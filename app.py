from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO, send



app = Flask(__name__, template_folder="file")
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)


@app.route("/")

@app.route("/index.html")

def home():
    return render_template('index.html')

@app.route("/login.html")
def login():
    return render_template('login.html')

@app.route("/join.html")
def join():
    return render_template('join.html')

@socketio.on('game_no')
def handle_my_custom_event(data):
    send(data, broadcast=True)

@socketio.on('message')
def handleMessage(msg):
    print('Message:' + msg)
    send(msg, broadcast=True)


if (__name__ == "__main__"):
    socketio.run(app)