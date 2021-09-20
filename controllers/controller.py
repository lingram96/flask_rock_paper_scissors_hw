from flask import render_template
from app import app
from models.player import Player
from models.game import Game

@app.route('/rps')
def index():
    return render_template('home.html', title = "Home -")

@app.route('/rps/rules')
def rules():
    return render_template('rules.html', title = "Rules -")

@app.route('/rps/game')
def game():
    return render_template('result.html', title = "Play!")

@app.route('/rps/game/<choice_1>/<choice_2>')
def play_the_game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game(player_1, player_2)
    game_winner = game.play_game(choice_1, choice_2)
    return render_template ("result.html", title= "Rock, Paper, Scissors", game_winner = game_winner)
