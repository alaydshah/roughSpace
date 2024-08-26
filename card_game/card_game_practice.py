import random
from enum import Enum, auto


class Suit(Enum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SUITS = auto()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


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

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if self.suit.value == other.suit.value:
            return self.rank.value > other.rank.value
        return self.suit.value > other.suit.value

    def points(self):
        return self.suit.value * self.rank.value


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
        self.points = 0

    def receive_card(self, card):
        self.hand.append(card)

    def sort_hand(self):
        self.hand.sort()
        print(f"Player {self.name} has {len(self.hand)} cards. Hand: {self.hand}")

    def play_random(self):
        # random_card_index = random.randrange(0, len(self.hand))
        # return self.hand.pop(random_card_index)
        random_card = random.choice(self.hand)
        for index, card in enumerate(self.hand):
            if card.suit == random_card.suit:
                return self.hand.pop(index)

    def play_suit(self, suit):
        for index, card in enumerate(self.hand):
            if card.suit == suit:
                return self.hand.pop(index)
        return self.play_random()

    def add_points(self, points):
        self.points += points

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.points < other.points


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    players = [Player("Sheshu"), Player("Sammy"), Player("Chota"), Player("Mickado")]

    for i in range(52):
        index = i % 4
        player = players[index]
        player.receive_card(deck.draw())

    for player in players:
        player.sort_hand()

    index = random.randrange(0, 4)
    rounds = 13
    num_players = len(players)
    for round in range(rounds):
        winner_index, winner_points, suit = None, None, None
        for _ in range(num_players):
            index = int(index % 4)
            player = players[index]
            if not suit:
                card = player.play_random()
                points = card.points()
                winner_index = index
                winner_points = card.points()
                suit = card.suit
            else:
                card = player.play_suit(suit)
                points = card.points()
                if points > winner_points:
                    winner_points = points
                    winner_index = index
            index += 1
            print(f"[Round {round}] Player {player} played card {card} gaining points {points}")

        print(f"Winner of Round {round} is Player {players[winner_index]} with points {winner_points}")
        index = winner_index
        players[winner_index].add_points(winner_points)

    players.sort()
    for player in players:
        print(f"Player {player} accumulated points {player.points}")
    player_of_the_series = players[len(players)-1]
    print(f"Winner of the series is player {player_of_the_series} with total points {player_of_the_series.points}")