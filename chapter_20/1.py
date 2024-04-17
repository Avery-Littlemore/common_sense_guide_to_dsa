# You’re working on software that analyzes sports players.

# If you look carefully, you’ll see that there are some players who participate in more than one kind of sport. 
# Jill Huang and Wanda Vakulskas play both basketball *and* football.

# You are to write a function that accepts two arrays of players and returns an array of the players who play in 
# *both* sports. In this case, that would be the following:
# ["Jill Huang", "Wanda Vakulskas"]

# While there are players who share first names and players who share last names, we can assume there’s only one person 
# who has a particular *full* name (meaning first *and* last name).

# We can use a nested-loops approach, comparing each player from one array against each player from the other array, but
# this would have a runtime of O(N * M). Your job is to optimize the function so that it can run in just O(N + M).

def players_on_both_teams(array_1, array_2):
    hash_table = {}
    result = []

    for player in array_1:
        player_name = player['first_name'] + ' ' + player['last_name']
        hash_table[player_name] = True

    for player in array_2:
        player_name = player['first_name'] + ' ' + player['last_name']
        if hash_table.get(player_name):
            result.append(player_name)

    return result

basketball_players = [
    {'first_name': "Jill", 'last_name': "Huang", 'team': "Gators"},
    {'first_name': "Janko", 'last_name': "Barton", 'team': "Sharks"},
    {'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Sharks"},
    {'first_name': "Jill", 'last_name': "Moloney", 'team': "Gators"},
    {'first_name': "Luuk", 'last_name': "Watkins", 'team': "Gators"}
]

football_players = [
    {'first_name': "Hanzla", 'last_name': "Radosti", 'team': "32ers"},
    {'first_name': "Tina", 'last_name': "Watkins", 'team': "Barleycorns"},
    {'first_name': "Alex", 'last_name': "Patel", 'team': "32ers"},
    {'first_name': "Jill", 'last_name': "Huang", 'team': "Barleycorns"},
    {'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Barleycorns"}
]

print(players_on_both_teams(basketball_players, football_players))