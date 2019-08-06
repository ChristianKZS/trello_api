import os
import sys
import json
import requests
from trello import TrelloApi, Boards, Cards, Actions

#cards = Cards("2498ea4b49bbd6ba085cecd96c100d5b", "833215058ad88624223e33fdafbc3eba24f665cd1ddf771c8d0c3b94a60e9101")
#boards = Boards("2498ea4b49bbd6ba085cecd96c100d5b", "833215058ad88624223e33fdafbc3eba24f665cd1ddf771c8d0c3b94a60e9101")
#api = TrelloApi("2498ea4b49bbd6ba085cecd96c100d5b", "833215058ad88624223e33fdafbc3eba24f665cd1ddf771c8d0c3b94a60e9101")
#result = boards.get_card_idCard( "5cd9c435e54720731d1fc762")
# url = "https://api.trello.com/1/boards/d2EnEWSY/actions/?limit=2"
# result = requests.get(url)
#print(json.dumps(result))

def get_board(api_key, oauth_token):
    return Boards(api_key, oauth_token)

def get_card(api_key, oauth_token):
    return Cards(api_key, oauth_token)

def get_updated_cards(api_key, oauth_token):
    return (api_key, oauth_token)

def get_cards_from_board(id_board):
    with open(f"{os.getcwd()}/configs.json", "r") as file:
        config = json.load(file)
        board = get_board(config["api_key"], config["oauth_token"] )
        return board.get_card(id_board)

def filter_json(api_key, oauth_token, id_board):
    with open(f"{os.getcwd()}/configs.json", "r") as file:
        config = json.load(file)
        board = get_board(config["api_key"], config["oauth_token"] )
        return board.get_card(id_board)



if __name__ == "__main__":
    actions = filter_json("HIT0fzMC")
    print(actions)