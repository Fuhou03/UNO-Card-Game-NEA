from card import Card
import random


class Player:
    def __init__(self):
        self.deck = []

    def select_card(self, pile):
        """ The opponent selects a card """
        colours = ["red", "blue", "yellow", "green"]
        random.shuffle(self.deck)

        for i in range(0, len(self.deck)):  # Select the first matching card and remove it from their hand
            current_card = self.deck[i]

            if (current_card.colour == pile[-1].colour) or (current_card.value == pile[-1].value):
                #or (current_card.colour == pile[-1].colour and (current_card.value == pile[-1].value)):
                # If the current card matches with the card at the top of the discard pile
                pile.append(current_card)
                self.deck.pop(i)
                return pile

            elif current_card.value == "wild" or current_card.value == "wild 4":  # If a wild card is chosen
                random_colour = random.choice(colours)  # Select a random colour for the next player
                current_card.colour = random_colour
                pile.append(current_card)

                print(f"A wildcard was selected and the colour chosen is {random_colour}")
                if current_card.value == "wild 4":
                    print("Your turn is skipped and you pick up 4 cards")

                self.deck.pop(i)
                return pile

        return pile

    def choose_card(self, pile):
        """ To choose your own card """
        valid = False

        try:  # They might enter a number that is higher/lower than the no. of cards u have (fix later)
            choice = int(input("Choose a card by typing it's number at the front. \n"
                               "If you have no valid cards then type anything else to draw a card: "))
            print("\n", end="")

        except ValueError:  # If they entered something else
            return pile

        else:  # Executes after the try statement (If they entered a number)
            while not valid:

                # If my choice matches correctly
                if (self.deck[choice].colour == pile[-1].colour) or (self.deck[choice].value == pile[-1].value):
                    # or (self.deck[choice].colour == pile[-1].colour and self.deck[choice].value == pile[-1].value):
                    pile.append(self.deck[choice])  # Add the card to the discard pile
                    self.deck.pop(choice)  # Remove it from your deck
                    valid = True

                elif self.deck[choice].value == "wild" or self.deck[choice].value == "wild 4":
                    # If they chose a wild card
                    #if self.deck[choice].value == "wild":
                    new_colour = input("Choose a colour for your opponent: ")
                    # else: # 2 Player mode
                        # new_colour = input("Choose a colour for yourself: ")  # wild 4 skips the opponent

                    self.deck[choice].colour = new_colour  # The colour of the card at the top of the pile changes
                    pile.append(self.deck[choice])
                    self.deck.pop(choice)
                    valid = True

                else:
                    choice = int(input("That card cannot be chosen. Choose another: "))

        finally:  # happens regardless
            return pile
