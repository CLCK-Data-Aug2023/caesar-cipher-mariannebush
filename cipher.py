alphabet = "abcdefghijklmnopqrstuvwxyz"
caesar_text = ""

shift = 5
sentence = input("Please enter a sentence: ")
sentence = sentence.lower()

for letter in sentence:
    if letter in alphabet:
        index = alphabet.find(letter)
        index = (index + shift) % 26
        letter = alphabet[index]
    caesar_text += letter

print("The encrypted sentence is:",caesar_text)
