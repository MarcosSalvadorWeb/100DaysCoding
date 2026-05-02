cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random as rnd

import art
print(art.logo)
print("WELCOME TO THE CASSINO !!!")

answer = str(input("Do you want to play a game of BlackJack? (y/n):"))

def counting_cards(lst):
    count = sum(lst)
    aces = lst.count(11)

    while count > 21 and aces > 0:
        count -= 10
        aces -= 1

    return count

while answer == "y":

    player_hand = rnd.choices(cards, k=2)
    print(f"Your hand is {player_hand}, current score: {counting_cards(player_hand)}")


    computers_hand = rnd.choices(cards, k=2)
    print(f"Computer's first card is {computers_hand[0]}")


    continue_game = input("Do you want another card?: (y/n)")

    while continue_game == "y":
        player_hand.append(rnd.choice(cards))
        print(f"Your hand is {player_hand}, current score: {counting_cards(player_hand)}")
        print(f"Computer's first card is {computers_hand[0]}")

        continue_game = input("Do you want another card?: (y/n)")

    #Computador
    while counting_cards(computers_hand) < 17:
        computers_hand.append(rnd.choice(cards))

    score_computer = counting_cards(computers_hand)
    score_player = counting_cards(player_hand)
    print(f"Your final hand {player_hand}, final score is {score_player}")
    print(f"Computer's final hand {computers_hand}, final score is {score_computer}")
    if score_player > 21:
        print("You lost!")
    elif score_player < 21 and score_computer > 21:
        print("You won!")
    elif score_player == 21 and score_computer != 21:
        print("You won!")
    elif score_player != 21 and score_computer == 21:
        print("You lost!")
    elif score_player == score_player:
        print("It's a tie!")

    print("Thanks for playing!")
    answer = str(input("Do you want to play another game of BlackJack? (y/n):"))
    print("\n" * 20)






