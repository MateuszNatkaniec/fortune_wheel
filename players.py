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


def next_player():
    active_player = get_active_player()
    active_player_idx = players.index(active_player)

    next_player_idx = (active_player_idx + 1) % len(players)

    active_player["is_active"] = False
    players[next_player_idx]["is_active"] = True


def get_winner():
    hight_score = max([player["score"] for player in players])
    return [player for player in players if player["score"] == hight_score]



next_player()
print(players)
update_score(0)
next_player()
print(players)
next_player()
print(players)
print((get_winner()))