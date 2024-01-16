#alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#user input
user_input = input("Please input the word to encode\n")
shift_number = int(input("Type the shift number\n"))

#make user input from string to list
list_user_input = list(user_input)

#encoding function
def encoding():
    for num in range(len(user_input)):
        word_index = alphabet.index(list_user_input[num])
        if word_index + shift_number + 1 > len(alphabet):
            encrypted_letter = alphabet[(word_index+shift_number)%len(alphabet)]
        else:
            encrypted_letter = alphabet[(word_index+shift_number)]
        list_user_input[num] = encrypted_letter

def decoding():
    for num in range(len(user_input)):
        word_index = alphabet.index(list_user_input[num])
        if word_index - shift_number < 0:
            encrypted_letter = alphabet[(word_index-shift_number)+26]
        else:
            encrypted_letter = alphabet[(word_index-shift_number)]
        list_user_input[num] = encrypted_letter

decoding()
print(list_user_input)