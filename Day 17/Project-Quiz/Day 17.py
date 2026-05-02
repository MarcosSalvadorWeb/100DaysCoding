# Ao criarmos uma classe, devemos incializar seus atributos através de uma função
from random import randint
class Razah:
    def __init__(self,time):
        # Caso definimos algo diretamente
        self.money = 1000000
        self.fala = "TOMA NA CHAPELETA!"
        # Caso algo seja definido pelo criador da instância
        self.time = time #Uso da variável

    def dar_uma_balinha(self):
        tentativa = randint(1,10)
        if tentativa >5:
            self.fala = "TOMEI NA CHAPELETA"
        else:
            self.fala = "TOMA NA CHAPELETA, BAGRÃO"


razinha = Razah("Faze Clan")

print(razinha.money)
print(razinha.time)
razinha.dar_uma_balinha()
print(razinha.fala)
razinha.dar_uma_balinha()
print(razinha.fala)


