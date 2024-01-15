import random, hangman_art, hangman_words, os

#Define clear temrinal function
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Intro Logo
print(hangman_art.logo)

#Select random word from list as answer
hangman_answer_list = hangman_words.word_list
answer= random.choice(hangman_answer_list)
length_of_word = len(answer)
list_correct_answer = list(answer)

#User answer variable
user_answer = ""

for num in range(length_of_word):
    user_answer += "_"
    list_answer = list(user_answer)

#Hangman logo
hangman_logo = int(0)

stages = hangman_art.stages

stages.reverse()

#User input checking
guessed_letter = []
def user_input_checking():
    global hangman_logo
    global guessed_letter
    user_input = input("Please provide a letter\n").lower()

    clear_terminal()
    #Check and update guess word
    for num in range(length_of_word):
        if user_input == answer[num]:
            list_answer[num] = user_input
        else:
            list_answer[num] == "_"
    

    if user_input in answer and user_input not in guessed_letter:
        print("You guess the right word")
    elif user_input in guessed_letter:
        print(f"You guessed {user_input} before, try another letter")
    else:
        print("You guess the wrong word")
        hangman_logo += 1

    #Record user guessed word
    guessed_letter += user_input

#User game play
status = False
while status == False:
    if hangman_logo < 5 and list_correct_answer == list_answer:
        print("You win!")
        status = True
    elif hangman_logo < 5:
        user_input_checking()
        print(list_answer)
    else:
        print("You lose")
        print(f"The answer is {answer}")
        status = True
    print(stages[hangman_logo+1])
