# %% 
# run vscode as jupyter nbk using # %%

from enum import Enum
from typing import List

class Suit(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3

class Card:

    def __init__(self, face_value:int, suit:Suit):
        self.face_value = face_value
        self._suit = suit
        self._available = True


    # adding property decorator exposes a read-only `suit` attribute
    # card1.suit = Suit.SPADE is disallowed
    # property methods should not take arguments
    # If a method doesn't take any args, consider making it a property
    @property
    def suit(self):
        return self._suit

    # abstract methods are to be implemeted by child class
    # there is no default implementation
    @property
    def value(self):
        raise NotImplementedError()

    def is_available(self):
        return self._available
    
    def mark_available(self):
        self._available = True

    def mark_unavailable(self):
        self._available = False

class Deck:

    def __init__(self):
        self._dealt_index = 0
        # generate_Cards() - for now, all cards hardcoded to A spade (may be)
        self._cards = [Card(1, Suit.SPADE) for i in range(52)]

    def shuffle(self):
        from random import random
        random.shuffle(self._cards)

    def deal_card(self) -> Card:
        self._dealt_index += 1
        return self._cards[self._dealt_index]

    def deal_hand(self, count:int) -> List[Card]:
        pass

    @property
    def remaining_cards(self):
        return len(self._cards) - self._dealt_index

class Hand:
    
    def __init__(self):
        self._cards = []
    
    def score(self):
        score = 0
        for card in self._cards:
            score += card.value
        return score

    def add_card(self, card):
        self._cards.append(card)

class BlackJackHand(Hand):
    def __init__(self):
        super().__init__()

    def possible_scores(self):
        pass

    def score(self):
        #scores = self.possible_scores()
        scores = [1, 2, 21]
        for score in scores:
            if score>21 and score<float("inf"):
                min_over = score
            min_over = 0
        return min_over


    def busted(self):
        return self.score() > 21

    def is21(self):
        return self.score() == 21

    def is_black_jack(self):
        pass


class BlackJackCard(Card):
    def __init__(self, c, s) -> None:
        self.c = c
        self.s = s
        super().__init__(c, s)

    def is_ace(self):
        return self.c == 1

    def value(self):
        if self.is_ace():
            return 1
        else:
            return self.c



card1 = Card(1, Suit.HEART)
print(card1.suit)

# not available in base class
# print(card1.value)

deck = Deck()
print(deck.remaining_cards)

bjhand1 = BlackJackHand()
print(bjhand1)
#bjhand1.is_available()
bjhand1.is21()

bjcard1 = BlackJackCard(1, Suit.HEART)
bjcard1.is_ace()

# class Deck:


# print(Suit.CLUB)
# print(Suit.CLUB.value)
# print(Suit(0))
## %%

# %%
