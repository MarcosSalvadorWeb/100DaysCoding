print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child Tickets are $5")
        bill += 5
    elif age <= 18:
        print("Youth Tickets are $10")
        bill += 10
    else:
        print("Adults Tickets are $15")
        bill += 15

    photo = input("Do you want some photos? ")
    if photo == "Yes":
        print("Photos are $10")
        bill += 10

    print(f"Your Total Bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

