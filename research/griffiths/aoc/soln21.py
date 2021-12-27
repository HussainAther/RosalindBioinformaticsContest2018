from collections import defaultdict

def play_game(games):
    """Play the game"""
    global wins
    wins = [0,0]        # number of universes won for player 1, 2
    while len(games) > 0:
        games_this_round = dict(games)
        games = defaultdict(int)    # reset, will get rebuilt
        for state, universes in games_this_round.iteritems():
            game_round(state, universes, games)
    return wins


def game_round(game, universes, games):
    """One round of the game"""
    global wins
    (p1_pos, p1_score), (p2_pos, p2_score) = game
    
    # Player 1
    for roll, univ_roll in dice_rolls.iteritems():
        # Universes for this roll are number of universes in this state * # of rolls with this value
        p1_universes = universes * univ_roll
        new_p1_pos = p1_pos + roll
        new_p1_pos = (new_p1_pos - 1) % 10 + 1
        new_p1_score = p1_score + new_p1_pos
        if new_p1_score >= 21:
            wins[0] += p1_universes   # Player 1 wins
        else:
            # Player 2
            for roll2, univ_roll2 in dice_rolls.iteritems():
                p2_universes = p1_universes * univ_roll2
                new_p2_pos = p2_pos + roll2
                new_p2_pos = (new_p2_pos - 1) % 10 + 1
                new_p2_score = p2_score + new_p2_pos
                if new_p2_score >= 21:
                    wins[1] += p2_universes   # Player 2 wins
                else:
                    new_state = ((new_p1_pos, new_p1_score), (new_p2_pos, new_p2_score))
                    games[new_state] += p2_universes
    return


def roll_dice():
    """Roll dice 3 times, returning universe count for each total"""
    
    dice_rolls = defaultdict(int)
    
    for d1 in range(1,4):
        for d2 in range (1,4):
            for d3 in range (1,4):
                roll_total = d1 + d2 + d3
                dice_rolls[roll_total] += 1
    
    return dice_rolls
    

#-----------------------------------------------------------------------------------------

position = [10, 2]      # my input
#position = [4, 8]       # sample input

dice_rolls = roll_dice()

# Games is number of games in each state.
# State key:
#    Player 1 position, score
#    Player 2 position, score

games = defaultdict(int)
state = ((position[0], 0), (position[1], 0))
games[state] = 1

wins = play_game(games)

print
print 'Player 1 won in', wins[0], 'universes'
print 'Player 2 won in', wins[1], 'universes'
print
print 'Most universes:', max(wins)

