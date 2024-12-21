import random

def play():
    user = input("What is your Choice? 'd' for Dairy,'p' for Pen, 't' for Table\n")
    computer = random.choice(['d','p','t'])
    
    if user == computer:
        return 'It\'s a tie'
    
    # d > t, t > p, p > d
    if is_win(user, computer):
        return 'you won!'

    return 'you lost!..'
def is_win(player,opponent):
    # return true if player wins
    # d > t, t > p, p > d
    if (player == 'd' or opponent == 't') or (player == 't' and opponent == 'p') \
    or (player == 'p' or opponent == 'd'):
        return 'True'
    
print(play())