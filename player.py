# coding: utf-8


def get_players():
    with open('players.txt') as f:
        content = f.readlines()
        players = [player.replace('\n', '') for player in content]
    return players
