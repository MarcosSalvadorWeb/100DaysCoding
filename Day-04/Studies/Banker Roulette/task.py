import random as rnd
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Hard way
"""
dice = rnd.randint(1, 5)

if dice == 1:
    print(f"{friends[dice-1]} has to pay the bill!")
elif dice == 2 :
    print(f"{friends[dice-1]} has to pay the bill!")
elif dice == 3:
    print(f"{friends[dice-1]} has to pay the bill!")
elif dice == 4:
    print(f"{friends[dice-1]} has to pay the bill!")
else:
    print(f"{friends[dice-1]} has to pay the bill!")
"""
# Easy Way

choice = rnd.choice(friends)
print(f"{choice} has to pay the bill!")