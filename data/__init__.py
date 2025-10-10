"""This module provides functions for handling game data."""

import json
import csv


def load_game_data():
    with open('data/gamedata.json', 'r') as file:
        return json.load(file)


def load_map_data():
    map_data = []
    with open('data/map.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            map_data.append(row)
    return map_data
