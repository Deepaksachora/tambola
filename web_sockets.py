import random
import string

from flask import Flask, render_template, render_template_string, redirect, make_response
from flask_socketio import SocketIO, join_room, send, emit

from game import Game

app = Flask(__name__, template_folder="file")
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, logger=True)
socketio.init_app(app, cors_allowed_origins="*")

games = {}


@socketio.on('get_game_state')
def get_game_state(data):
    if 'id' not in data:
        return

    game_id = data["id"]
    cookie = data["cookie"]

    join_room(game_id)

    g = games[int(game_id)]
    usr = g.create_user()
    ticket = g.generate_board(usr)

    response = {
        "type": "game",
        "data": {
            "user_id": usr,
            "ticket": ticket.tolist(),
            "isAdmin": g.is_admin(cookie)
        }
    }

    send(response, room=game_id)


@socketio.on("generate_number")
def generate_number(data):
    if 'id' not in data:
        return

    game_id = data["id"]
    cookie = data["cookie"]

    game = games[int(game_id)]
    if not game.is_admin(cookie):
        return

    game.start_game()

    response = {
        "type": "number",
        "data": {
            "num": data["number"]
        }
    }

    send(response, room=game_id)


@app.route('/game/<int:game_id>', methods=["GET"])
def game_page(game_id):
    if game_id not in games:
        return render_template_string("Game {{game}} not found", game=game_id)

    game = games[game_id]
    if game.is_active():
        return render_template_string("This game is already running")

    return render_template('game.html')


@app.route('/create', methods=["GET", "POST"])
def create_game():
    random_id = ''.join(random.choice(string.ascii_lowercase) for i in range(5))

    g = Game(admin_ip=random_id)
    games[g.get_id()] = g

    resp = make_response(redirect(f'/game/{g.get_id()}'))
    resp.set_cookie('game_cookie', random_id)

    return resp
