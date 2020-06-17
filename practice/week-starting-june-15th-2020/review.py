import pprint

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

# print(len(player_stats))

# print(player_stats['name'])

# for i in player_stats:
#   print(i['name'])


# for i in player_stats:
#   if i["goals"] == 6:
#     print(i['name'])

# for i in player_stats:
#   if i["games_played"] == 7:
#     print(i['name'], i['team'])

# for i in player_stats:
#   if i['goals'] <= 3:
#     print(i['name'])
