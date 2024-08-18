## Introduction:

You are tasked with implementing a card game similar to Bridge. The game is played with a standard deck of 52 cards divided into 4 suits (Clubs, Diamonds, Hearts, Spades) and 13 ranks (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A).

The classes for Card, Deck, and Player have been provided for you. The Deck class includes methods to shuffle and draw cards. The Player class holds a hand of cards.

Your task is to implement the game logic across three parts.

## Part 1: Dealing and Sorting

Implement the logic to deal cards to 4 players and then sort each player’s hand by suit.

### 1.	Deal the Deck:
- Distribute all 52 cards evenly among the 4 players. Each player should receive 13 cards.
### 2.	Sort the Hands:
- Sort each player’s hand so that cards are grouped by suit. Within each suit, the cards should be sorted in ascending order of rank.

## Part 2: Simulating the Game

Now that each player has their hand, simulate an entire game where players take turns playing cards according to specific rules:

### 1.	Starting the Game:
- Select one player to start the game randomly. 
- This player will play the first card from their hand (any card of their choosing).

### 2.	Playing a Trick:
- The suit of the first card played determines the suit for the current trick. 
- Each following player must play a card of the same suit if they have one. 
- If a player does not have a card of the same suit, they may play any card from their hand. 
- Print out each player and the card they played using the message "Player {X} played {Card}".

### 3.	Determining the Winner of a Trick:
- The winner of the trick is the player who played the highest-ranked card of the suit that started the trick. 
- Print the name of the winning player. 
- The winner of the current trick starts the next trick.

### 4.	Repeat for 13 Rounds:
- Continue this process until all players have no cards left in their hands. This will be a total of 13 rounds.

## Part 3: Implementing Scoring

Finally, modify the game to include a scoring system. The scoring rules are as follows:

### 1.	Scoring Points:
- Each round, the winning player earns points based on the cards played in that round:
- 5 is worth 5 points 
- 10 is worth 10 points 
- K is worth 10 points 
- All other cards are worth 0 points

### 2.	Track and Display Scores:
- At the end of each round, print the number of points the winner earned for that round. 
- After all 13 rounds, print each player’s total score. 
- Finally, print the name of the player with the highest score.

## Expectations
- The candidate should demonstrate strong understanding of object-oriented programming principles such as encapsulation, inheritance, and polymorphism. 
- The code should be well-structured and easy to follow. 
- The candidate should focus on handling edge cases, such as ensuring a player can play any card if they do not have a card of the same suit as the starter. 
- The final output should clearly indicate the flow of the game and the final results.
