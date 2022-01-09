from card import Card
import random


class Player:
    def __init__(self, id):
        self.deck = []
        self.id = id

    def choose_card(self, pile):
        """ To choose your own card """
        if self.id == 0 or self.id == 1:    # Player 0 or P1
            valid = False

            while not valid:
                try:  # They might enter a number that is higher/lower than the no. of cards u have (fix later)
                    choice = int(input("Choose a card by typing it's number at the front. \n"
                                       "If you have no valid cards then type any string to draw a card: "))
                    print("\n", end="")

                    if choice >= len(self.deck) or choice < 0:  # If they enter an invalid number
                        raise IndexError

                except ValueError:  # If they entered something else
                    return pile
                except IndexError:
                    print("That card is not possible. Please enter the number correctly. \n")
                    continue    # They will have to enter again

                else:  # Executes after the try statement (If they entered a number)
                    # If my choice matches correctly
                    if (self.deck[choice].colour == pile[-1].colour) or (self.deck[choice].value == pile[-1].value):
                        pile.append(self.deck[choice])  # Add the card to the discard pile
                        self.deck.pop(choice)  # Remove it from your deck
                        return pile
                    elif self.deck[choice].value == "wild" or self.deck[choice].value == "wild 4":
                        # If they chose a wild card
                        new_colour = input("Choose a colour for the next player: ")
                        self.deck[choice].colour = new_colour  # The colour of the card at the top of the pile changes
                        pile.append(self.deck[choice])
                        self.deck.pop(choice)
                        return pile
                    else:
                        print("That card cannot be chosen.")   # Loop continues again
                        continue

        elif self.id == 2:   # Program selects the card for P3 (AI)
            colours = ["red", "blue", "yellow", "green"]
            random.shuffle(self.deck)

            for i in range(0, len(self.deck)):  # Select the first matching card and remove it from their hand
                current_card = self.deck[i]

                if (current_card.colour == pile[-1].colour) or (current_card.value == pile[-1].value):
                    # If the current card matches with the card at the top of the discard pile
                    pile.append(current_card)
                    self.deck.pop(i)
                    return pile

                elif current_card.value == "wild" or current_card.value == "wild 4":  # If a wild card is chosen
                    random_colour = random.choice(colours)  # Select a random colour for the next player
                    current_card.colour = random_colour     # "None" property turns into the selected colour
                    pile.append(current_card)

                    print(f"A wildcard was selected and the colour chosen is {random_colour}")

                    self.deck.pop(i)
                    return pile

            return pile     # No matching card found

