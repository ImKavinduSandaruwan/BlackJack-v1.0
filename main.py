import random
#Kavindu Sandaruwan
def logo():
    print()                                                                                      
    print("""88          88                       88        88                       88""")         
    print("""88          88                       88        ""                       88  """)       
    print("""88          88                       88                                 88    """)     
    print("""88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8""")   
    print("""88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"   """) 
    print("""88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      """)
    print("""88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   """)
    print("""8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  """)
    print("""                                              ,88                                  """)
    print("""                                            888P"                                  """)
    print("_____________________________________________________Coded by Kavindu Sandaruwan_________")


#logo()
while True:
    deck_of_card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    #ace = 11 or 1 and j,q,k = 10
    
    print()
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n")
    if play_game != 'y':
        print("Thank you")
        break
    else:    
        if play_game == "y":
            card_list = []
            computer_card_list = []
            player_marks = computer_marks = 0
            computer_total = 0
            
            card1 = random.randint(1,10)
            card2 = random.randint(1,10)
            card_list = [card1,card2]

            computer_card1 = random.randint(1,10)

            print()            
            print("Your cards: ",card_list)
            print("Computer's first card: ",computer_card1)
            print()

            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                
                card3 = random.randint(1,10)
                card_list.append(card3)
                computer_card2 = random.randint(1,10)
                computer_card_list = [computer_card1, computer_card2]

                for i in computer_card_list:
                    
                    computer_total += i
                if computer_total < 17:
                    computer_card3 = random.randint(1,10)
                    computer_card_list = [computer_card1, computer_card2, computer_card3]
                
                print()
                print("Your final hand: ",card_list)
                print("Computer's final hand: ",computer_card_list)
                print()

                #player total
                for i in card_list:
                    player_marks += i
                #print("player marks",player_marks)

                #Computer total
                for i in computer_card_list:
                    computer_marks += i
                #print("Computer marks",computer_marks)

                if player_marks == computer_marks:
                    print("*** No one wins ***")
                    print("_____________________________________")
                    continue

                #Check is marks > 21
                if player_marks > 21 and computer_marks > 21:
                    print("*** No one wins ***")
                    print("_____________________________________")
                    continue
                elif player_marks > 21:
                    print("*** Dealer wins ***")
                    print("_____________________________________")
                    continue
                elif computer_marks > 21:
                    print("*** You win ***")
                    print("_____________________________________")
                    continue

                #Compare with 21
                player_marks_gap = 21 - player_marks
                computer_marks_gap = 21 - computer_marks

                if player_marks_gap < computer_marks_gap:
                    print("*** You win*** ")
                    print("_____________________________________")
                    continue
                elif player_marks_gap > computer_marks_gap:
                    print("*** Dealer wins ***")
                    print("_____________________________________")
                    continue

            
            elif another_card == "n":
                computer_card2 = random.randint(1,10)
                computer_card_list = [computer_card1, computer_card2]
                
                #Counting total marks and if marks are less than 17 it will generate another random card
                #if it is not this will totaly ignore and print card lists
                
                for i in computer_card_list:                    
                    computer_total += i
    
                if computer_total < 17:
                    computer_card3 = random.randint(1,10)
                    computer_card_list = [computer_card1, computer_card2, computer_card3]
                
                print()
                print("Your final hand: ",card_list)
                print("Computer's final hand: ",computer_card_list)
                print()

                #player total
                for i in card_list:
                    player_marks += i
                #print("player marks",player_marks)

                #Computer total
                for i in computer_card_list:
                    computer_marks += i
                #print("Computer marks",computer_marks)

                if player_marks == computer_marks:
                    print("*** No one wins ***")
                    print("_____________________________________")
                    continue

                #Check is marks > 21
                if player_marks > 21 and computer_marks > 21:
                    print("*** No one wins ***")
                    print("_____________________________________")
                    continue
                elif player_marks > 21:
                    print("*** Dealer wins ***")
                    print("_____________________________________")
                    continue
                elif computer_marks > 21:
                    print("*** You win ***")
                    print("_____________________________________")
                    continue

                #Compare with 21
                player_marks_gap = 21 - player_marks
                computer_marks_gap = 21 - computer_marks

                if player_marks_gap < computer_marks_gap:
                    print("*** You win ***")
                    print("_____________________________________")
                    continue
                elif player_marks_gap > computer_marks_gap:
                    print("*** Dealer wins ***")
                    print("_____________________________________")
                    continue
