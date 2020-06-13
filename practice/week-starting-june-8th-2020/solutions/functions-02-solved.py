import pprint
# TOP 20 GOAL LEADERS OF FIFA WOMEN'S WORLD CUP 2019

player_stats = [
    {
        "name": "Ellen White",
        "team": "ENG",
        "games_played": 6,
        "minutes_played": 514,
        "goals": 6,
        "assists": 0,
    },
    {
        "name": "Megan Rapinoe",
        "team": "USA",
        "games_played": 5,
        "minutes_played": 429,
        "goals": 6,
        "assists": 2,
    },
    {
        "name": "Alex Morgan",
        "team": "USA",
        "games_played": 6,
        "minutes_played": 491,
        "goals": 6,
        "assists": 3,
    },
    {
        "name": "Sam Kerr",
        "team": "AUS",
        "games_played": 4,
        "minutes_played": 360,
        "goals": 5,
        "assists": 0,
    },
    {
        "name": "Wendie Renard",
        "team": "FRA",
        "games_played": 5,
        "minutes_played": 450,
        "goals": 4,
        "assists": 0,
    },
    {
        "name": "Cristiane",
        "team": "BRA",
        "games_played": 4,
        "minutes_played": 301,
        "goals": 4,
        "assists": 0,
    },
    {
        "name": "Sara Daebritz",
        "team": "GER",
        "games_played": 5,
        "minutes_played": 450,
        "goals": 3,
        "assists": 1,
    },
    {
        "name": "Kosovare Asllani",
        "team": "SWE",
        "games_played": 7,
        "minutes_played": 575,
        "goals": 3,
        "assists": 1,
    },
    {
        "name": "Carli Lloyd",
        "team": "USA",
        "games_played": 7,
        "minutes_played": 193,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Rose Lavelle",
        "team": "USA",
        "games_played": 6,
        "minutes_played": 427,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Jennifer Hermoso",
        "team": "ESP",
        "games_played": 4,
        "minutes_played": 360,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Vivianne Miedema",
        "team": "NED",
        "games_played": 7,
        "minutes_played": 627,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Aurora Galli",
        "team": "ITA",
        "games_played": 5,
        "minutes_played": 302,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Cristiana Girelli",
        "team": "ITA",
        "games_played": 4,
        "minutes_played": 279,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Amandine Henry",
        "team": "FRA",
        "games_played": 5,
        "minutes_played": 450,
        "goals": 2,
        "assists": 1,
    },
    {
        "name": "Eugenie Le Sommer",
        "team": "FRA",
        "games_played": 5,
        "minutes_played": 380,
        "goals": 2,
        "assists": 1,
    },
    {
        "name": "Valerie Gauvin",
        "team": "FRA",
        "games_played": 5,
        "minutes_played": 333,
        "goals": 2,
        "assists": 0,
    },
    {
        "name": "Alexandra Popp",
        "team": "GER",
        "games_played": 5,
        "minutes_played": 450,
        "goals": 2,
        "assists": 0,
    },
    {
        "name": "Lina Magull",
        "team": "GER",
        "games_played": 5,
        "minutes_played": 301,
        "goals": 2,
        "assists": 1,
    },
    {
        "name": "Sofia Jakobsson",
        "team": "SWE",
        "games_played": 6,
        "minutes_played": 540,
        "goals": 2,
        "assists": 0,
    },
]

# 1) Write a function called array_length that takes an array as an argument and returns the length of that array.


def array_length(arr):
    return len(arr)

# 2) Write a function called find_player that takes an array and a name as arguments and returns that player's stat sheet.


def find_player(arr, name):
    for player in arr:
        if player["name"] == name:
            return player

# 3) Write a function called player_names that takes an array as an argument and returns a new array containing only the names of each player.


def player_names(arr):
    new_arr = []
    for player in arr:
        new_arr.append(player["name"])
    return new_arr

# 4) Write a function called find_players_by_goal_count that takes an array and a number as arguments and returns a new array of the player names with goals to match the given number.


def find_players_by_goal_count(arr, goals):
    new_arr = []

    for player in arr:
        if player["goals"] == goals:
            new_arr.append(player["name"])
    return new_arr


# 5) Write a function called find_players_by_team that takes an array and a team's name as an argument and returns a new array of the player names who belong to the given team.

def find_players_by_team(arr, team):
    new_arr = []

    for player in arr:
        if player["team"] == team:
            new_arr.append(player["name"])
    return new_arr

# 6) Write a function called most_minutes_per_game that takes an array as an argument. Find the player who played the most minutes per game. Then return a string in the following format:

# '{player_name} played {minutes_per_game} minutes per game during the 2019 WORLD CUP'


def most_minutes_per_game(arr):
    mpg = 0
    player_name = ''
    for player in arr:
        player_mpg = player["minutes_played"] / player["games_played"]
        if player_mpg > mpg:
            mpg = player_mpg
            player_name = player["name"]
    return '{player_name} played {mpg} minutes per game during the 2019 WORLD CUP'.format(player_name=player_name, mpg=mpg)


# 7) Write a function called most_goals_per_game that takes an array as an argument. Find the player with the most goals per game. Return a string stating the player name the player's goals per game of the player with the most goals per game.

# Format of the response: '{player_name} scored {gpg} goals per game during the 2019 WORLD CUP'


def most_goals_per_game(arr):
    gpg = 0
    player_names = []
    for player in arr:
        player_gpg = player["goals"] / player["games_played"]
        if player_gpg > gpg:
            gpg = player_gpg
            player_names = [player["name"]]
        elif player_gpg == gpg:
            player_names.append(player["name"])
    return '{player_names} scored {gpg} goals per game during the 2019 WORLD CUP'.format(player_names=player_names, gpg=gpg)


# 8) Write a function called most_assists_per_game that takes an array as an argument and returns the player with the most assists per game.

def most_assists_per_game(arr):
    apg = 0


# pprint.pprint(array_length(player_stats))

# pprint.pprint(find_player(player_stats, "Alex Morgan"))

# pprint.pprint(player_names(player_stats))

# pprint.pprint(find_players_by_goal_count(player_stats, 3))

pprint.pprint(most_minutes_per_game(player_stats))
