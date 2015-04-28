# coding: utf-8
import config
import player
from random import shuffle
from slacker import Slacker

teams = [
    'Azul',
    'Laranja',
    'Verde'
]
players = player.get_players()

shuffle(teams)
shuffle(players)

message = 'De semana em semana o slack informa o resultado parcial da Tele Sena... Ops... Do futeboooooooool!\n\n'
for i in range(0, len(players), 5):
    if len(teams):
        team = teams.pop()
    else:
        team = 'Sem Uniforme'

    message = message + '{} -> {}\n'.format(team, players[i:i + 5])

slack = Slacker(config.SLACK_TOKEN)
slack.chat.post_message(
    channel='#luizafutebol',
    text=message,
    username='Lombardi',
    icon_url='http://f.cl.ly/items/2W2M3w2d0j3o2B0U1J1z/telesena.png'
)
