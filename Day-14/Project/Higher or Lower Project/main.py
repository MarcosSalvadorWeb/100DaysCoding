from art import logo
from art import vs
print(logo)
from game_data import data
import random as rnd


def compare(A,B,data):

    print(f"Compare A: {A.get('name')}, a {A.get('description')} from {A.get('country')}")

    print(vs)

    print(f"Against B: {B.get('name')}, a {B.get('description')} from {B.get('country')}")

    if A.get('follower_count') > B.get('follower_count'):
        return("A")
    else:
        return("B")

def game(data):
    A , B = rnd.choices(data, k=2)
    game = True

    while game == True:

        Winner = compare(A,B,data)

        guess = str(input("Who has more followers? Type 'A' or 'B'"))

        if guess == Winner:
            if Winner == "A":
                B = rnd.choice(data)
            else:
                A = B
                B = rnd.choice(data)
        else:
            print("You Lost")
            if Winner == "A":
                print(f"{A.get('name')}, a {A.get('description')} from {A.get('country')} has f{A.get('follower_count') - B.get('follower_count')} more followers")
            else:
                print(
                    f"{B.get('name')}, a {B.get('description')} from {B.get('country')} has {B.get('follower_count') - A.get('follower_count')} more followers")
            game = False
game(data)









