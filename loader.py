# Fantasy Good Time
# Name: Eric + Sean
# Time spent: 1 hour
import numpy 
import json

player_detail_active = "https://api.sportsdata.io/v3/nba/scores/json/Players"#/free/player-details-by-active

headers = {
    "Ocp-Apim-Subscription-Key": "dde6763b7c62427fbf71100cf230f8aa"
}

response = requests.get(url=player_detail_active, headers=headers)

player_detail_active_json = json.loads(response.text)

def num_players():
    # print an int number of players in the NBA in current year
    num_players = len(player_detail_active_json)
    print("num_players:", num_players)
    
calls_dict = {
    AllStars
}    

def get_player_stats(player_id,) 
    
def get_data(url, params_dict):
    # request data from sportsdata.io 
    
    
    

