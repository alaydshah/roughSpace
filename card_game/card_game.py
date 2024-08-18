import random
from enum import Enum, auto
from typing import List


class Suit(Enum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ASCE = 14

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        if self.suit.value == other.suit.value:
            return self.rank.value > other.rank.value
        else:
            return self.suit.value < other.suit.value


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards: List[Card]):
        self.hand.extend(cards)
        self.sort_hand()
        print(f"Player {self.name} has hand {self.hand}")

    def sort_hand(self):
        self.hand.sort(key=lambda card: (card.suit.value, card.rank.value))

    # def has_suit(self, suit):
    #     return any(card.suit == suit for card in self.hand)

    def play_card(self, suit: Suit):
        for card in self.hand:
            if card.suit == suit:
                removed_card = card
                # print(f"[DEBUG] Num of cards before removal for player {self.name}: {len(self.hand)}")
                self.hand.remove(card)
                print(f"Player {self.name} played {removed_card}")
                # print(f"[DEBUG] {len(self.hand)} cards remaining for player {self.name}")
                return card
        return self.play_random_card()

    def play_random_card(self):
        card = random.choice(self.hand)
        # print(f"[DEBUG] Num of cards before removal for player {self.name}: {len(self.hand)}")
        self.hand.remove(card)
        print(f"Player {self.name} played {card}")
        # print(f"[DEBUG] {len(self.hand)} cards remaining for player {self.name}")
        return card

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    # Players
    players = [Player("Sheshu"), Player("Sammy"), Player("Chota"), Player("Mikado")]

    # Create Deck and Shuffle
    deck = Deck()
    deck.shuffle()

    # Deal Cards
    player_cards = [[] for _ in range(4)]
    for _ in range(13):
        for i in range(4):
            player_cards[i].append(deck.draw())

    for i in range(4):
        players[i].receive_cards(player_cards[i])

    # Let's play
    index = random.randrange(0, 4)

    for round in range(13):
        winner_rank, winner_index, suit = -1, -1, None
        for _ in range(4):
            if index == 4:
                index -= 4
            player = players[index]
            if not suit:
                card = player.play_random_card()
                suit = card.suit
            else:
                card = player.play_card(suit)
            if card.suit == suit and card.rank.value > winner_rank:
                winner_rank = card.rank.value
                winner_index = index
            index += 1
        print(f"Winner of round {round} is player {players[winner_index]}")
        index = winner_index
