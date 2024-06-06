import datetime
import json
import os

import requests

from database.models import Games


def writing_to_db():
    url = "https://odds.p.rapidapi.com/v4/sports/icehockey_nhl/odds"

    querystring = {
        "regions": "eu",
        "oddsFormat": "decimal",
        "markets": "h2h",
        "dateFormat": "iso",
    }

    headers = {
        "X-RapidAPI-Key": "ff58899001msh74a21aecad4795ep1c4d3fjsnbc4ae75a37dd",
        "X-RapidAPI-Host": "odds.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers, params=querystring)

    data_api = json.loads(response.text)

    path_json = os.path.abspath(
        "C:/Users/proni/PycharmProjects/python_basic_diploma/database/data.json"
    )

    with open(path_json, "w") as test_file:
        json.dump(data_api, test_file, indent=4)
    with open(path_json, "r") as file_r:
        json_data = json.load(file_r)
    for i_game in json_data:
        for i_bookmakers in i_game["bookmakers"]:
            for i_markets in i_bookmakers["markets"]:
                for i_outcomes in i_markets["outcomes"]:
                    Games.create(
                        game_id=i_game["id"],
                        time_req=datetime.datetime.now(),
                        home_team=i_game["home_team"],
                        away_team=i_game["away_team"],
                        title=i_bookmakers["title"],
                        name_team=i_outcomes["name"],
                        price=i_outcomes["price"],
                    )
