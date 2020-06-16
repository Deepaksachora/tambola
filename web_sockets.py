import random

from flask import Flask, render_template, render_template_string, url_for, redirect
from flask_socketio import SocketIO, join_room, send
from game import games, Game


app = Flask(__name__, template_folder="file")
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, logger=True)
socketio.init_app(app, cors_allowed_origins="*")


@socketio.on('get_game_state')
def get_game_state(data):
    if 'id' not in data:
        return

    game_id = data["id"]
    join_room(game_id)


@socketio.on("generate_number")
def generate_number(data):
    if 'id' not in data:
        return

    game_id = data["id"]

    response = {
        "type": "number",
        "data": {
            "num": random.randint(1, 100)
        }
    }

    send(response, room=game_id)


@app.route('/game/<int:game_id>', methods=["GET"])
def game_page(game_id):
    if game_id not in games:
        return render_template_string("Game {{game}} not found", game=game_id)

    return render_template('game.html')


@app.route('/create', methods=["GET", "POST"])
def create_game():
    g = Game()
    games[g.get_id()] = g

    return redirect(f'/game/{g.get_id()}')
