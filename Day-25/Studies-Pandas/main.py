import pandas as pd
import numpy as np

# file = open("./weather_data.csv", "r")
# file_content = file.readlines()
# print(file_content)

# import csv
# with open("./weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     print(data)
#     for row in data:
#         temperatures.append(row[1])
#
#     print(temperatures)

# data = pd.read_csv("./weather_data.csv")
# print(type(data))
# print(type(data["day"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Getting Collumns
# print(data["temp"])
# print(data.temp)
#
# # Getting Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# Monday = data[data.day == "Monday"]
# temp = Monday.temp
# print(1.8*temp + 32)
#
# # Creating a Data Frame from Scratch
# data_dict = {
#     "Estudantes": ["Marcos","Sanches","Kadu"],
#     "Notas": [5,3,2]
# }
#
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data.columns) # Visualizando o nome das colunas
print(data["Primary Fur Color"].unique())# Visualizando todas as cores
colors = data["Primary Fur Color"].dropna()
print(set(colors)) # Pegando Valores Únicos

gray = colors[colors == "Gray"].count()
cinnamon = colors[colors == "Cinnamon"].count()
black = colors[colors == "Black"].count()

Squirrel_Count = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black],
}

data_new = pd.DataFrame(Squirrel_Count)
data_new.to_csv("./Squirrel_Count.csv")