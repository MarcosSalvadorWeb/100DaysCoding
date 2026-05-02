# TODO-1: Ask the user for input

print("WELCOME TO THE BLINDER AUCTION PROJECT")
#Inicializando Dicionário
prices = {}

#Fazendo um lance
def bid():
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    prices[name] = bid

#Fazendo o leilão
answer = True

#Condição de restart
while answer:
    bid()
    print("\n"*100)
    temp = input("Are there more people? (y/n): ")
    if temp == "n":
        answer = False
    elif temp == "y":
        answer = True
"""
price = 0
for key in prices:
    if prices[key] > price:
        winner = key
        price = prices[key]
"""
#Forma mais fácil de pegar o máximo
big = max(prices, key=prices.get)


print(f"The Winner is {big} with a price of ${prices[big]}")


# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


