MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dimes": 0.1,
    "nickels": 0.05,
    "pennies": 0.01,
}

def payment(order,profit):
    price =MENU[order]["cost"]
    dick = {}
    dick["quarter"] = int(input("How many quarters?"))
    dick["dimes"] = int(input("How many dimes?"))
    dick["nickels"] = int(input("How many nickels?"))
    dick["pennies"] = int(input("How many pennies?"))
    pay = 0
    for key in dick:
        pay += dick[key] * coins[key]

    change = pay - price
    if change >= 0:
        profit += price
        print(f"Here is your change {round(change, 2)}")
        return True, profit
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False, profit


def report():
    print(resources)

def check_resources(order):
    ingredients = MENU[order]["ingredients"]
    lock = True
    for key in ingredients:
        lock = (resources[key] >= ingredients[key])
        if lock != True:
            print(f"Sorry, there is not enough {key}")
            return False
    return lock

def do_order(order):
    ingredients = MENU[order]["ingredients"]
    for key in ingredients:
        resources[key] -= ingredients[key]

def refill():
    ingredient = str(input("Would you like to refill?"))
    much = int(input("How much?"))
    resources[ingredient] += much


def coffee_machine():
    profit = 0
    machine_on = True
    print("Welcome to the coffee machine")
    print(f"Options:{MENU.keys()}")
    while machine_on:
        order = str(input("What would you like?"))
        if order == "OFF":
            print("Turning the machine off...")
            machine_on = False
        elif order == "report":
            report()
        elif order == "options":
            print(f"Options:{MENU.keys()}")
        elif order == "refill":
            refill()
        elif order in MENU:
            check = check_resources(order)
            if check:
                pay,profit = payment(order,profit)
                if pay:
                    do_order(order)
                    print("Here is your coffee!")
                    print("Thank you for your time")
                    print("\n" * 5)
        else:
            print("Invalid option")
coffee_machine()