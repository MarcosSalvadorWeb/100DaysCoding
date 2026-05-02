from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffe_machine():
    machine_on = True
    while machine_on == True:
        print("\n" * 3)
        print("=============================================================")
        print("Welcome to CoffeMaker")
        print("=============================================================")
        coffe = CoffeeMaker()
        menu = Menu()
        machine = MoneyMachine()
        print("Here are your options:")

        print(menu.get_items())
        print("=============================================================")
        order = input("What would you like?")

        if order == "report":
            coffe.report()
            machine.report()

        elif menu.find_drink(order) != None:
            order = menu.find_drink(order)
            if (coffe.is_resource_sufficient(order)):

                if machine.make_payment(order.cost):
                    coffe.make_coffee(order)
                else:
                    print("\n" * 4)
            else:
                print("\n"*4)


        elif order == "OFF":
            print("Turning off the machine...")
            machine_on = False




coffe_machine()