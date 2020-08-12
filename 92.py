"""

Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game, one of the highest selling and addictive games of all time, and a classic of the arcade era. Your task is to write methods that return the highest score from the list, the last added score and the three highest scores.

"""
def highest(scores):
    return max(scores)

def last_added(scores):
    return scores[-1]

def top_three(scores):
    return sorted(scores, reverse=True)[:3]

scores = [45,62,12,78,4]
print(highest(scores))
print(last_added(scores))
print(top_three(scores))