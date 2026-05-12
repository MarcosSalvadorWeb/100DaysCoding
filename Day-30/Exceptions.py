# Catching Exceptions: We can use try and except to catch some cases of error

# try: # Tente isso
#     file = open("a_file.txt","r")
# except : # Caso não funcione
#     file = open("a_file.txt","w")
#     file.write("Alguma coisa")

# Casos em que especificamps o erro específico
try:
    file = open("data.txt", "r")
    a = {"key": "value"}
    print(a["Something"])
except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("Something")
except KeyError:
    print("Essa key não existe")
else: # Após os excepts isso roda
    content = file.read()
    print(content)
finally: # Isso roda independentemente do que aconteça
    file.close()
    raise KeyError("Aconteceu um erro com os dicionários reveja as keys")