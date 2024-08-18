import random
from random import shuffle
from enum import Enum


class Suits(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


class Ranks(Enum):
    ACE = 1
    R2 = 2
    R3 = 3
    R4 = 4
    R5 = 5
    R6 = 6
    R7 = 7
    R8 = 8
    R9 = 9
    R10 = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:
    def __init__(self, suit: Suits, rank: Ranks):
        self._suit = suit
        self._rank = rank

    def __str__(self):
        return f"{self.get_rank()} of {self.get_suit()} ({self.get_points()})"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.get_points() < other.get_points()

    def get_rank_value(self):
        return self._rank.value

    def get_suit_value(self):
        return self._suit.value

    def get_rank(self):
        return self._rank.name if "R" not in self._rank.name else self._rank.name[1:]

    def get_suit(self):
        return self._suit.name

    def get_points(self):
        return self.get_rank_value() * self.get_suit_value()


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in list(Suits) for rank in list(Ranks)]

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        # Might have to handle edge case of list being empty
        return self.cards.pop()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def draw_cards(self, deck: Deck, num_cards: int = 1):
        for _ in range(num_cards):
            card = deck.draw()
            self.hand.append(card)
        self.hand.sort()
        print(f"Sorted hand of player {self.name}: {self.hand}")

    def play_card(self):
        return self.hand.pop()

    def __str__(self):
        return f"Player {self.name} has hand {self.hand}"


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    players = [Player("Sheshu"), Player("Sammy"), Player("Chota"), Player("Mickado")]

    # Num of rounds
    rounds = 13

    for player in players:
        player.draw_cards(deck, rounds)

    num_players = len(players)
    start_index = random.randrange(0, len(players))

    for round in range(rounds):
        winner_points, winner_index = float('-inf'), -1
        index = start_index
        for _ in range(num_players):
            if index == num_players:
                index -= num_players
            player = players[index]
            played_card = player.play_card()
            points = played_card.get_points()
            if points > winner_points:
                winner_points, winner_index = points, index
            index += 1
        winner_player = players[winner_index]
        print(f"Winner of round {round} is Player {winner_player.name}")
        start_index = winner_index
