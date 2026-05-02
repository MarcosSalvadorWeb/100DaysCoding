# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

df = pd.read_csv("./nato_phonetic_alphabet.csv")

NATO_DICT = {row.letter: row.code for (index,row) in df.iterrows()}

name = input("Enter your name: ").upper()

lst = [NATO_DICT[letter] for letter in name]

print(lst)