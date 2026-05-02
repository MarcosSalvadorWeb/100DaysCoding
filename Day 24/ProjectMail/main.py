#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = open("./Input/Names/invited_names.txt", "r")
names_string = names.readlines()
letter = open("./Input/Letters/starting_letter.txt", "r")
letter_content = letter.read()

for name in names_string:
    name = name.strip("\n")
    new_letter = letter_content.replace("[name]", name)
    file_name = "./Output/ReadyToSend/" + name + ".txt"
    with open(file_name, "w") as complete_letter:
        complete_letter.write(new_letter)