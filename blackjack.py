import random

#Card List 
card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#User's and Computer's hands
user_hand = []
computer_hand = []

#User and Computer both Drawing two cards
user_hand = random.sample(card_list, 2)
computer_hand = random.sample(card_list, 2)

#Calculate the sum of hands
user_hand_sum = sum(user_hand)
computer_hand_sum = sum(computer_hand)

#Add card function, need to choose one of the hands to add 
def add_card(to_add_card):
    global user_hand_sum
    global computer_hand_sum
    new_card = random.choice(card_list)
    to_add_card.append(new_card)
    user_hand_sum = sum(user_hand)
    computer_hand_sum = sum(computer_hand)

#Compare function
def compare():
    if computer_hand_sum <= 16:
        add_card(computer_hand)
    elif computer_hand_sum > 16 and computer_hand_sum <= 21:
        if user_hand_sum > computer_hand_sum:
            print(f"Dealer hand's are " + str(computer_hand) + "and you win")
        elif user_hand_sum == computer_hand_sum:
            print(f"Dealer hand's are " + str(computer_hand) + "and draw")
        elif computer_hand_sum > user_hand_sum:
            print(f"Dealer hand's are " + str(computer_hand) + "and you lose")
    elif computer_hand_sum > 21:
        print(f"Dealer hand's are " + str(computer_hand) + "and you win")

#Ask user decision to add new card
user_choice_question = "Y"
def user_choice():
    global user_choice_question
    if user_hand_sum < 21:
        print(f"Your cards: {user_hand}, current score: {user_hand_sum}")
        user_choice_question = input("Type 'y' to get another card, type 'n' to pass:").capitalize()
        if user_choice_question == "Y":
            add_card(user_hand)
            user_choice()
        if user_choice_question == "N":
            return
    else:
        return

#Gameplay
def gameplay():
    if user_hand_sum == 21:
        compare()
    elif user_hand_sum < 21 and user_choice_question == "Y":
        print(f"Dealer hand's are " + str(computer_hand[0]))
        user_choice()
        compare()
        gameplay()
    elif user_hand_sum < 21:
        compare()
    else:
        print(f"Your cards: {user_hand}\n")
        print(f"Dealer hand's are " + str(computer_hand) + "and you win")
        print("Dealer win")


           



gameplay()