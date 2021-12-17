from card import Card
from player import Player
from deck import Deck


def display_deck(deck, player):
    if player == 1:
        print("Your deck is: ")
    else:
        print("\nThe opponent's deck: ") # For testing purposes
    for i in range(0, len(deck)):
        print(f"{i}: {deck[i].colour} - {deck[i].value}")
    print("\n", end="")


def display_pile(pile):
    print(f"The card at the top of the Discard pile: \n{pile[-1].colour} - {pile[-1].value}")
    # for card in pile:
    # print(f"{card.colour} - {card.value}")
    print("\n", end="")


def play_game():
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
                turn = 2 # Moves onto opponent after I drew a card

            elif discard_pile[-1].value == "skip" or discard_pile[-1] == "reverse":
                turn = 1 # So the opponent's turn is skipped
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
                turn = 1 # My turn

        if len(me.deck) == 0:
            finished = True
            print("You won!")
        elif len(ai.deck) == 0:
            print("You lost!")
        elif len(ai.deck) == 1:
            print("Your opponent said: 'UNO!'")


play_game()
