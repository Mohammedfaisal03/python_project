import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

is_game_over=False

def calculated_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "it's a draw "
    elif computer_score==0:
        return "lose, opponent has blackjack "
    elif user_score == 0:
        return " win with a blackjack "
    elif user_score >21 :
        return " you went over,you lose "
    elif computer_score > 21:
        return " opponent went over you win "
    elif computer_score>user_score:
        return "you lose "
    else:
        return "you win "





def dealcard():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

user_card=[]
computer_card=[]

for i in range(2):
    user_card.append(dealcard())
    computer_card.append(dealcard())

while not is_game_over:
    user_score=calculated_score(user_card)
    computer_score=calculated_score(computer_card)
    print(f"        your cards: {user_card}, current score {user_score} ")
    print(f"        computers first card: {computer_card [0]} ")

    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True

    else:
        user_should_deal=input("        type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal=='y':
            user_card.append(dealcard())
        else:
            is_game_over=True

while computer_score!=0 and computer_score<17:
    computer_card.append(dealcard())
    computer_score=calculated_score(computer_card)

print(compare(user_score,computer_score))







