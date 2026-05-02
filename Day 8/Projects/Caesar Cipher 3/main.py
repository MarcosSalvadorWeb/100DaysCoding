from art import logo

print(logo)
print("WELCOME TO THE ENCODER AND DECODER MACHINE")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(text, shift, direction):
    result = ""

    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)

            if direction == "encode":
                new_idx = (idx + shift) % len(alphabet)
            else:
                new_idx = (idx - shift) % len(alphabet)

            result += alphabet[new_idx]
        else:
            result += char  # mantém números, espaços e símbolos

    print(f"Here is the {direction}d result: {result}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(text=text, shift=shift, direction=direction)

    restart = input("Do you want to restart? Y/N\n").lower()
    if restart != "y":
        should_continue = False
        print("Goodbye 👋")
