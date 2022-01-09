from player import Player
from deck import Deck

def display_deck(p):
    if p.id == 0:
        print("Your deck is: ")
    elif p.id == 1:
        print("Player 1's deck: ") # For testing purposes
    else:
        print("AI's deck: ")

    for i in range(0, len(p.deck)):
        print(f"{i}: {p.deck[i].colour} - {p.deck[i].value}")
    print("\n", end="")


def display_pile(pile):
    print(f"The card at the top of the Discard pile: \n{pile[-1].colour} - {pile[-1].value}")
    print("")


def change_direction(direction):
    if direction == "clockwise":
        new_direction = "anticlockwise"
    else:
        new_direction = "clockwise"
    return new_direction


def next_turn(turn, direction):
    """ Increments or decrements the turn variable to determine whose turn is next """
    if direction == "clockwise":
        turn = (turn + 1) % 3   # Becomes 0 if it reaches 3, becomes 1 if it's 4 etc to stop index errors
    else:
        turn -= 1
        if turn == -1:   # Prevents index errors
            turn = 2    # So it goes back to the AI (turn 2) after P1 has their turn (0)

    return turn

def three_player():
    dk = Deck()
    dk.create_deck()
    dk.shuffle()

    player_list = [Player(0), Player(1), Player(2)]    # Create the players
    for player in player_list:
        player.deck = dk.deal_cards(player.deck)    # Give the players 7 cards

    discard_pile = []
    for i in range(0, len(dk.deck)): # So the game doesn't start with a wild card
        if dk.deck[i].colour != "None":
            discard_pile.append(dk.deck[i]) # Card at the top of the deck is placed down first (index 0)
            break

    turn = 0  # My turn is 0, P2 is 1 and 2 is the AI's turn
    finished = False
    direction = "clockwise"

    while not finished:
        current_player = player_list[turn]
        next_player = player_list[next_turn(turn, direction)] # next_turn called so the index's incremented/decremented

        print(f"\nCurrent player: {current_player.id}")
        print(f"The current direction: {direction}")

        display_pile(discard_pile)
        display_deck(current_player)

        discard_pile_length = len(discard_pile)
        discard_pile = current_player.choose_card(discard_pile)     # Player selects a card

        if len(current_player.deck) == 1:
            print(f"Player {current_player.id} said UNO!")

        if len(discard_pile) == discard_pile_length:  # If they chose to draw a card (length didn't change)
            current_player.deck = dk.draw_card(current_player.deck)  # Draw 1 card from main deck
            # If the card you drew is valid you can place it down immediately
            if current_player.deck[-1].colour == discard_pile[-1].colour or current_player.deck[-1].value == \
                    discard_pile[-1].value:
                if current_player.id == 0 or current_player.id == 1:
                    ask = input(f"The {current_player.deck[-1].colour} - {current_player.deck[-1].value}"
                                f" card you picked up is valid, do you want to place it down? Type 'y' or 'n': ")
                    if ask == "y":
                        # print("\n", end = "")
                        discard_pile.append(current_player.deck[-1])
                        current_player.deck.pop(-1)
                    else:
                        turn = next_turn(turn, direction)   # They don't place the card down
                        continue    # So the card at the top of the discard pile doesn't get compared again

                else: # AI picked up a card - They place it down without needing to be asked
                    discard_pile.append(current_player.deck[-1])
                    current_player.deck.pop(-1)
                    print("The AI picked up a card and placed it down.")
            else:   # If they card they drew cannot be placed down, it moves on
                turn = next_turn(turn, direction)
                continue

        if discard_pile[-1].value == "draw 2":
            # Next player draws 2 and their turn is skipped
            for i in range(2):
                next_player.deck = dk.draw_card(next_player.deck)
            print(f"Player {next_player.id}'s turn is skipped.")
            for i in range(2): # Turn increments twice so it skips the next player
                turn = next_turn(turn, direction)

        elif discard_pile[-1].value == "skip":
            print(f"Player {next_player.id}'s turn is skipped.")
            for i in range(2):
                turn = next_turn(turn, direction)

        elif discard_pile[-1].value == "reverse":
            direction = change_direction(direction)
            print(f"\nPlayer {next_player.id}'s turn is skipped.") # Printed before the reverse
            turn = next_turn(turn, direction)

        elif discard_pile[-1].value == "wild 4":
            for i in range(4):  # Next player draws 4 cards
                next_player.deck = dk.draw_card(next_player.deck)
            print(f"Player {next_player.id}'s turn is skipped.")
            for i in range(2):
                turn = next_turn(turn, direction)

        else:  # Normal numbered card placed down
            turn = next_turn(turn, direction)

        if len(current_player.deck) == 0:
            print(f"Player {current_player.id} has won! The game has completed.")
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
