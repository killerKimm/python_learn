import json
# read from json file
with open("player_data.json", "r") as p:
    # variable with dictionary from json file
    player_info = json.load(p)
    print(player_info['player1']['wins'])
    print(player_info['player2']['losses'])


# edit player information
# for player in player_info['player1']:
#    player['name'] = ''
#    player['wins'] = '0'
#    player['losses'] = '0'
#    player['drows'] = '0'
# for player in player_info['player2']:
#    player['name'] = ''
#    player['wins'] = '0'
#    player['losses'] = '0'
#    player['drows'] = '0'

# write the player stats to a file
# with open("player_data.json", "w") as player:
#   json.dump(player_info, player, indent=2)
