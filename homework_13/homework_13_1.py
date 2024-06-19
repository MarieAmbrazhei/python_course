"""Homework_13_1: OOP_2. Writing and implementing programs."""


# Task_1 Cards deck

import random


class Card:
    """This class describes the playing card"""
    number_list = ['Joker', 'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen',
                   'King']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, mast, number):
        self.number = number
        self.mast = mast


class CardsDeck:
    """This class define cards deck"""

    def __init__(self, mast_list, number_list):
        """This method is used to create cards deck"""
        self.cards = []

        for mast in mast_list:
            for number in number_list:
                self.cards.append(Card(mast, number))
        self.cards.append(Card("Joker", None))
        self.cards.append(Card("Joker", None))

    def shuffle(self):
        """This method is used to shuffle cards deck"""
        random.shuffle(self.cards)
        return self.cards

    def get(self, index):
        """This method is used to get cards deck"""
        if 0 <= index < len(self.cards):
            return self.cards[index].number, self.cards[index].mast
        raise IndexError(
            "The card number is outside the permissible range.")


CONTINUE_GAME = 'yes'

while CONTINUE_GAME.lower() in ['y', 'yes']:
    deck = CardsDeck(Card.mast_list, Card.number_list)
    deck.shuffle()
    card_number = int(input('Выберите карту из колоды в 56 карт: '))
    card = deck.get(card_number)
    print(f'You card is: {card[0]} {card[1]}')
    continue_game = input('Continue game? Yes or No?: ')
