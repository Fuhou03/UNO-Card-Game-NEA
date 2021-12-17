from card import Card
import random


class Player:
    def __init__(self):
        self.deck = []
        colours = ["red", "blue", "yellow", "green"]

    def draw_card(self, main_deck):
        ''' When player chooses to draw a card '''

        self.deck.append(main_deck[0])
        main_deck.pop(0)
        return main_deck

    def select_card(self, pile, main_deck):
        ''' The opponent selects a card'''
        for i in range(0, len(self.deck)): # Select the first matching card and remove it from their hand
            if self.deck[i].colour == pile[-1].colour or self.deck[i].value == pile[-1].value:
                pile.append(self.deck[i])
                self.deck.pop(i)

                return pile, main_deck

        for i in range(0, len(self.deck)): # If no matching card was found:
            if self.deck[i].value == None: # If a wild card is chosen
                self.deck.pop(i)
                self.deck[i].colour = random.choice(colours) # Select a random colour for the next player
                pile.append(self.deck[i])

                return pile, main_deck

        main_deck = self.draw_card(main_deck) # If no matching cards are found in any cases
        return pile, main_deck




    def choose_card(self, pile, main_deck):
        valid = False

        try:
            choice = int(input("Choose a card by typing it's number at the front. \n"
                               "If you have no valid cards then type anything else to draw a card: "))
            print("\n", end="")
        except ValueError:  # If they entered something else
            main_deck = self.draw_card(main_deck)


        else:  # Executes after the try statement (If they entered a number)
            while not valid:
                if (self.deck[choice].colour == pile[-1].colour) or (
                        self.deck[choice].value == pile[-1].value):  # It matches
                    pile.append(self.deck[choice])  # Add the card to the discard pile
                    self.deck.pop(choice)  # Remove it from your deck
                    valid = True

                elif self.deck[choice].colour == None:  # If they chose a wild card
                    new_colour = input("Choose a colour for the next player: ")
                    self.deck[choice].colour = new_colour # The colour of the card at the top of the pile changes
                    pile.append(self.deck[choice])
                    self.deck.pop(choice)
                    valid = True

                else:
                    choice = int(input("That card cannot be chosen. Choose another: "))

        finally:  # happens regardless
            return pile, main_deck


