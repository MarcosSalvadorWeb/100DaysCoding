# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

df = pd.read_csv("./nato_phonetic_alphabet.csv")

NATO_DICT = {row.letter: row.code for (index,row) in df.iterrows()}

name = input("Enter your name: ").upper()
try:
    lst = [NATO_DICT[letter] for letter in name]
except KeyError:
    print("Sorry, only letters allowed.")
else:
    print(lst)