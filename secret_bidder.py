import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#print welcome statement
print("Welcome to the secret auction program")
other_bidder = "yes"
bid_summary = []
while other_bidder == "yes":
    #Ask name, the bid price and ask if there any other secret bidder
    bidder_name = input("What is your name? ")
    bid_price = input("What is your bid? ")
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    #Add the information into the dictionary
    bidding_information = {}
    bidding_information["bidder name"] = bidder_name
    bidding_information["bid price"] = bid_price
    bid_summary.append(bidding_information)
    clear_terminal()


#calculate who is the highest bidder
highest_person = ""
highest_bid = 0

def calculate_highest_score():
    global highest_person, highest_bid
    for num in range(len(bid_summary)):
        if int(bid_summary[num]["bid price"]) > highest_bid:
            highest_bid = int(bid_summary[num]["bid price"])
            highest_person = bid_summary[num]["bidder name"]
        

calculate_highest_score()
print(f"{highest_person} is the highest bidder")






