from flask import render_template
from web_sockets import app, socketio


@app.route("/")
@app.route("/game.html")
def home():
    return render_template('game.html')

if (__name__ == "__main__"):
    socketio.run(app)
