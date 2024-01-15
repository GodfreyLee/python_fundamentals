#Questionaire
team1 = input("Which team is Home court tonight's match up?\n")
team2 = input("Which team is Away tonight's match up?\n")
handicap = input(f"邊隊讓分?\n{team1} enter 1 or {team2} enter 2\n")
handicap_score = input("讓幾多分?\n")
ht_score = input("What is half time score?\n")
ft_score = input("What is full time score?\n")

#Handicap calculation
strong_team = ""
weak_team = ""

if handicap == 1:
    strong_team = team1
    weak_team = team2
else:
    strong_team = team2
    weak_team = team1

#player bet
number_of_player_bet = int(input("How many player bet you want to add?\n"))
gamble_player_bet_statement = ""

for num in range(1,number_of_player_bet+1):
    player_name = f"playername{num}"
    player_name = input(f"What is player{num} name?\n").upper()
    
    bet_type = int(input("Enter 1 for score only, Enter 2 for score + assist, Enter 3 for score + assist + rebound\n"))
    
    if bet_type == 1:
        score = input("What is the score?\n")
        gamble_player_bet_statement += f'''{player_name}

{score}
B
S

'''
    elif bet_type == 2:
        score = input("What is the score?\n")
        assist = input("What is the assist?\n")
        gamble_player_bet_statement += f'''{player_name}

{score}
B
S

Assist
{assist}
B
S

'''
    elif bet_type == 3:
        score = input("What is the score?\n")
        assist = input("What is the assist?\n")
        rebound = input("What is the rebound?\n")
        gamble_player_bet_statement += f'''{player_name}

{score}
B
S

Assist
{assist}
B
S

Rebound
{rebound}
B
S

'''
    else:
        print("Incorrect input")

#print statement
print(f'''
{team1} vs {team2}

Half time - {ht_score}
B
S

Full time - {ft_score}
B
S

{weak_team} + {handicap_score}
{strong_team} - {handicap_score}

{gamble_player_bet_statement}
''')
