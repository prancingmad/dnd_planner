import config

from functions.general import (
    load_json,
    save_json
)

class Monster:
    def __init__(self, name, challenge_rating, actions, count=0):
        self.name = name
        self.challenge_rating = challenge_rating
        self.actions = actions
        self.count = count

    def to_dict(self, destination):
        enemy_dict = {
            "name": self.name,
            "challenge_rating": self.challenge_rating,
            "actions": self.actions
        }
        if destination == "required":
            enemy_dict["count"] = self.count
        return enemy_dict

    def save_to_file(self, destination):
        monster_list = load_json(f"{destination}.json")
        monster_list.append(self.to_dict(destination))
        save_json(f"{destination}.json", monster_list)