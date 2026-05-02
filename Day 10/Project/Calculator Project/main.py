import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print(art.logo)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    continuar = True
    numb1 = int(input("Enter your first number: "))
    while continuar:
        operation = str(input("Enter your operation: "))
        numb2 = int(input("Enter your second number: "))
        answer = operations[operation](numb1, numb2)
        print(f"{numb1} {operation} {numb2} = {answer}")
        continuar = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continuar == "y":
            numb1 = answer
            continuar = True
        else:
            continuar = False
            print("\n" * 20)
            calculator()
calculator()


