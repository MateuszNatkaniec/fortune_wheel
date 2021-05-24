players = [
    {
        "name": "Janusz",
        "score": 0,
        "is_active": True
    },
    {
        "name": "Ela",
        "score": 0,
        "is_active": False
    },
    {
        "name": "Brian",
        "score": 0,
        "is_active": False
    }
]


def get_active_player():
    for player in players:
        if player['is_active']:
            return player


def update_score(amount):
    active_player = get_active_player()


    if amount > 0:
        active_player["score"] += amount
    else:
        active_player["score"] = 0

update_score(400)
update_score(200)
update_score(0)

print(get_active_player())
