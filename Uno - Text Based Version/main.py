from card import Card
from player import Player
from deck import Deck

def two_player():
    dk = Deck()
    dk.create_deck()
    dk.shuffle()

    ai = Player()
    ai.deck = dk.deal_cards(ai.deck)

    me = Player()
    me.deck = dk.deal_cards(me.deck)

    discard_pile = []
    discard_pile.append(dk.deck[0])  # Card at the top of the deck is placed down first

    turn = 1  # My turn (2 is the AI's turn)
    finished = False
    while not finished:
        if turn == 1:
            display_pile(discard_pile)
            display_deck(me.deck, 1)

            discard_pile, dk = me.choose_card(discard_pile, dk)

            if me.drew_card == True:
                turn = 2  # Moves onto opponent after I drew a card

            elif discard_pile[-1].value == "skip" or discard_pile[-1] == "reverse":
                turn = 1  # So the opponent's turn is skipped
                print("The opponent's turn is skipped")

            elif discard_pile[-1].value == "wild 4":
                print("The opponent's turn is skipped \n")
                for i in range(4):
                    ai.deck = dk.draw_card(ai.deck)
                turn = 1

            elif discard_pile[-1].value == "draw 2":
                for i in range(2):
                    ai.deck = dk.draw_card(ai.deck)

            else:
                turn = 2



        else:
            display_deck(ai.deck, 2)
            display_pile(discard_pile)
            print("\nIt is the opponent's turn. \nThey have performed an action. \n")

            discard_pile, dk = ai.select_card(discard_pile, dk)

            if discard_pile[-1].value == "wild 4":
                turn = 2  # My turn is skipped and I draw 4 cards
                for i in range(4):
                    me.deck = dk.draw_card(me.deck)
                    print("Your turn is skipped")

            elif discard_pile[-1].value == "draw 2":
                for i in range(2):
                    me.deck = dk.draw_card(me.deck)
                turn = 2
                print("Your turn is skipped")

            elif discard_pile[-1].value == "skip" or discard_pile[-1].value == "reverse":
                turn = 2
                print("Your turn is skipped")

            else:
                turn = 1  # My turn

        if len(me.deck) == 0:
            finished = True
            print("You won!")
        elif len(ai.deck) == 0:
            print("You lost!")
        elif len(ai.deck) == 1:
            print("Your opponent said: 'UNO!'")

def display_deck(deck, turn):
    if turn == 1:
        print("Your deck is: ")
    elif turn == 2:
        print("\nAI's deck: ")
    else:
        print("\nPlayer 2's deck: ") # For testing purposes

    for i in range(0, len(deck)):
        print(f"{i}: {deck[i].colour} - {deck[i].value}")
    print("\n", end="")


def display_pile(pile):
    print(f"The card at the top of the Discard pile: \n{pile[-1].colour} - {pile[-1].value}")
    # for card in pile:
    # print(f"{card.colour} - {card.value}")
    print("\n", end="")

#def perform_action():

def three_player():
    dk = Deck()
    dk.create_deck()
    dk.shuffle()

    ai = Player()
    ai.deck = dk.deal_cards(ai.deck)

    me = Player()
    me.deck = dk.deal_cards(me.deck)

    player_2 = Player()
    player_2.deck = dk.deal_cards(player_2.deck)

    discard_pile = []
    for i in range(0, len(dk.deck)): # So the game doesn't start with a wild card
        if dk.deck[i].colour != "None":
            discard_pile.append(dk.deck[i]) # Card at the top of the deck is placed down first (index 0)
            break

    turn = 1  # My turn (2 is the AI's turn)
    finished = False
    direction = "clockwise"

    while not finished:
        if turn == 1:
            print("\nCurrent player: p1")
            display_pile(discard_pile)
            display_deck(me.deck, 1)

            discard_pile_length = len(discard_pile)
            discard_pile = me.choose_card(discard_pile)

            if len(discard_pile) == discard_pile_length:  # If they chose to draw a card (length didn't change):
                me.deck = dk.draw_card(me.deck)  # Draw 1 card from main deck

                # If the card you drew is valid you can place it down immediately
                if me.deck[-1].colour == discard_pile[-1].colour or me.deck[-1].value == discard_pile[-1].value:
                    ask = input(f"The {me.deck[-1].colour} - {me.deck[-1].value} card you picked up is valid"
                                f", do you want to place it down? Type 'y' or 'n': ")
                    if ask == "y":
                        # print("\n", end = "")
                        discard_pile.append(me.deck[-1])
                        me.deck.pop(-1)

                if direction == "clockwise":
                    turn = 2  # Moves onto opponent after I drew a card
                else:  # Moves onto player 3 instead
                    turn = 3


            elif discard_pile[-1].value == "draw 2" or discard_pile[-1].value == "skip":
               # Opponent draws 2 and their turn is skipped
                if direction == "clockwise":
                    if discard_pile[-1] == "draw 2":
                        for i in range(2):
                            ai.deck = dk.draw_card(ai.deck)
                    turn = 3 # Moves onto player 2
                    print("AI's turn is skipped")
                else:
                    if discard_pile[-1] == "draw 2":
                        for i in range(2):
                            player_2.deck = dk.draw_card(player_2.deck)
                    turn = 2 # AI's turn now
                    print("Player 2's turn is skipped")

            elif discard_pile[-1].value == "reverse":
                if direction == "clockwise":
                    turn = 3
                    print("AI's turn is skipped")
                    direction = "anticlockwise"
                else:
                    turn = 2  # My turn
                    print("Player 2's turn is skipped\n")
                    direction = "clockwise"

            elif discard_pile[-1].value == "wild 4":
                if direction == "clockwise":
                    for i in range(4):  # Pick up 4 cards and skip their turn
                        ai.deck = dk.draw_card(ai.deck)
                    turn = 3
                    print("AI's turn is skipped \n")
                else:
                    for i in range(4):
                        player_2.deck = dk.draw_card(player_2.deck)
                    turn = 2
                    print("Player 2's turn is skipped \n")

            else:  # Normal numbered card placed down
                if direction == "clockwise":
                    turn = 2
                else:
                    turn = 3


        elif turn == 2:  # AI's turn
            display_deck(ai.deck, 2)
            display_pile(discard_pile)
            print("Current player: AI")

            if len(ai.deck) == 1:
                print("UNO!")

            discard_pile_length = len(discard_pile)
            discard_pile = ai.select_card(discard_pile)
            if len(discard_pile) == discard_pile_length: # If no matching cards are found in any cases (length is same)
                ai.deck = dk.draw_card(ai.deck) # Draw a card instead
                if ai.deck[-1].colour == discard_pile[-1].colour or ai.deck[-1].value == discard_pile[-1].value:
                    discard_pile.append(ai.deck[-1]) # Place that card down immediately if it's valid
                    ai.deck.pop(-1)
                    print("The AI picked up a card and placed it down.")
                if direction == "clockwise":
                    turn = 3
                else:
                    turn = 1

            elif discard_pile[-1].value == "wild 4":
                # Turn is skipped and they draw 4 cards
                if direction == "clockwise": # Use for loop on a list of the players and find the corresponding self.turn later?
                    for i in range(4):
                        player_2.deck = dk.draw_card(player_2.deck)
                    print("Player 2's turn is skipped")
                    turn = 1
                else:
                    for i in range(4):
                        ai.deck = dk.draw_card(ai.deck)
                    print("Your turn is skipped")
                    turn = 3

            elif discard_pile[-1].value == "draw 2" or discard_pile[-1].value == "skip":
                if direction == "clockwise":
                    if discard_pile[-1].value == "draw 2":
                        for i in range(2):
                            player_2.deck = dk.draw_card(player_2.deck)
                    turn = 1
                    print("Player 2's turn is skipped")

                else:
                    if discard_pile[-1].value == "draw 2":
                        for i in range(2):
                            me.deck = dk.draw_card(me.deck)
                    turn = 3
                    print("My turn is skipped")


            elif discard_pile[-1].value == "reverse":
                if direction == "clockwise":
                    turn = 1
                    print("Your turn is skipped")
                    direction = "anticlockwise"

                else:
                    turn = 3  # My turn
                    direction = "clockwise"

            else:  # Normal numbered card placed down
                if direction == "clockwise":
                    turn = 3
                else:
                    turn = 1

        elif turn == 3: # Player 2's turn

            print("\nCurrent player: p2")
            display_pile(discard_pile)
            display_deck(player_2.deck, 3)

            discard_pile_length = len(discard_pile)
            discard_pile = player_2.choose_card(discard_pile)

            if len(discard_pile) == discard_pile_length:  # If they chose to draw a card (length didn't change):
                player_2.deck = dk.draw_card(player_2.deck)  # Draw 1 card from main deck

                # If the card you drew is valid you can place it down immediately
                if player_2.deck[-1].value == discard_pile[-1].value or player_2.deck[-1].colour == discard_pile[-1].value:
                    ask = input("That card is valid, do you want to place it down? Type 'y' or 'n': ")
                    if ask == "y":
                        # print("\n", end = "")
                        discard_pile.append(player_2.deck[-1])
                        player_2.deck.pop(-1)

                if direction == "clockwise": # Happens regardless of the option they chose
                    turn = 1  # Moves onto opponent after I drew a card
                else:
                    turn = 2


            elif discard_pile[-1].value == "draw 2" or discard_pile[-1].value == "skip":
                # Opponent draws 2 and their turn is skipped
                if direction == "clockwise":
                    if discard_pile[-1].value == "draw 2":
                        for i in range(2):
                            me.deck = dk.draw_card(me.deck)
                    turn = 2 # Moves onto AI
                    print("My turn is skipped")
                else:
                    if discard_pile[-1].value == "draw 2":
                        for i in range(2):
                            ai.deck = dk.draw_card(ai.deck)
                    turn = 1
                    print("AI's turn is skipped")

            elif discard_pile[-1].value == "reverse":
                if direction == "clockwise":
                    turn = 2
                    print("My turn is skipped")
                    direction = "anticlockwise"
                else:
                    turn = 1
                    print("AI's turn is skipped")
                    direction = "clockwise"

            elif discard_pile[-1].value == "wild 4":
                if direction == "clockwise":
                    for i in range(4):  # Pick up 4 cards and skip their turn
                        me.deck = dk.draw_card(me.deck)
                    turn = 2
                    print("P2's turn is skipped and I pick up 4 cards \n")
                else:
                    for i in range(4):
                        ai.deck = dk.draw_card(ai.deck)
                    turn = 1
                    print("AI's turn is skipped and they pick up 4 cards \n")

            else:  # Normal numbered card placed down
                if direction == "clockwise":
                    turn = 1
                else:
                    turn = 2

        if len(me.deck) == 0:
            finished = True
            print("You won!")
        elif len(ai.deck) == 0:
            print("The AI won!")
            finished = True
        elif len(player_2.deck) == 0:
            print("Player 2 won!")
            finished = True


def play_game():
    z = False
    while not z:
        game_mode = int(input("Choose a game mode by typing either '2' or '3': "))
        print("\n", end="")

        if game_mode == 2:
            two_player()
            z = True
        elif game_mode == 3:
            three_player()
            z = True
        else:
            print("That is not a valid game mode, please type it in correctly")


play_game()
