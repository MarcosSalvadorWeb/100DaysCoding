# with open("mytxt.txt") as file:
#     contents = file.read()
#     print(contents)

# Com mode = "w" reescrevemos o arquivo
# Com mode = "a" fazemos tipo um append de lista

with open("./Papitos.txt", mode= "w") as file:
    file.write("Receita Nova de Pizza: \n Pepperoni \n Salsa \n Cebola \n Sal \n Massa")
