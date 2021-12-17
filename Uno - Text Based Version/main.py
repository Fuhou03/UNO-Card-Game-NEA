from card import Card
from player import Player
from deck import Deck


def display_deck(deck):
    print("Your deck is: ")
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
    for i in range(6):
        if turn == 1:
            display_pile(discard_pile)
            display_deck(me.deck)
            discard_pile, dk.deck = me.choose_card(discard_pile, dk.deck)
            turn = 2
        else:
            print("\nIt is the opponent's turn. \nThey have performed an action")

            discard_pile, dk.deck = ai.select_card(discard_pile, dk.deck)
            turn = 1


play_game()

