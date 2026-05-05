import random as rnd
print("Welcome to Rock Paper Scissors!")
play = int(input("Select your choice (0: Rock, 1: Paper, 2: Scissors): "))

#Alternativas
alt = [0,1,2]

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if play == 0:
    print("You choose: \n ")
    print(rock)
elif play == 1:
    print("You choose: \n ")
    print(paper)
elif play == 2:
    print("You choose: \n ")
    print(scissors)
else:
    print("Wrong choice! ")

print()

seed = rnd.randint(0,100)
rnd.seed(seed)
computer_choice = rnd.choice(alt)

if computer_choice == 0:
    print("Computer chooses: \n ")
    print(rock)
elif computer_choice == 1:
    print("Computer chooses: \n ")
    print(paper)
else:
    print("Computer chooses: \n ")
    print(scissors)

print()

if play == computer_choice:
    print("It's a draw!")
elif play == 0 and computer_choice == 1:
    print("You lost!")
elif play == 1 and computer_choice == 0:
    print("You won!")
elif play == 2 and computer_choice == 1:
    print("You won!")
elif play == 2 and computer_choice == 0:
    print("You lost!")
elif play == 0 and computer_choice == 2:
    print("You won!")
else:
    print("You lost!")
