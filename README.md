# mem-4
A Card game coded in Python that tests your memory!
Maintained by: Tanmay Agarwal, agarw139@umn.edu

# Objective:
Have the lowest sum total of cards by the end of the game. Ace = 1, K = 13, Q = 12, J =11 and the numbers stand for their integer values. Suits don't matter in this game and are not included in the programming too, but the deck still consists of 52 cards.

# Game Play
In the current version, the game is two - player. The deck will be shuffled and each player will be dealt 4 cards, arranged ina 2x2 table. The program will then show you the cards in the lower row for 5 seconds. You must remember your cards, and do not peek at your partners cards!

You will be accessing your cards through keyboard keys corresponding to:
```
X X   q w
X X   a s
X X   z x (this row will only appear if you get extra cards from wrong guessing [see below])
```
The game begins after this and one card from the remaining deck (of the 52 cards that are not in the 8 dealt to the players) will be placed in the "main deck" every turn. Note that you will not be able to see any of your cards. They will appear as an X, or as an O if that card is removed (as you will see later). The program will indicate which Player's turn it is and that player can choose from 3 different operations:

   1. If you like the card and want to replace it with one of your cards, press c. This is a good play if you have a low point yielding card, such as A or 2, so you can replace a J with a 2 to get a lower sum total at the end
   
   2. If you think you have this card in your set of cards, you can keep both this card and the card from your deck into the discard pile. This is great for you since you have better chance at having a lower point total at the end! Press v if you want to do this, and instructions will follow. NOTE: If you think you have that card in your deck, but actually remember it wrong, you will have to keep both cards!
       
       Example:
       ```
       Main Deck: J
       Your deck:
       X X
       X X
       ```
       Let us say you remember that the lower left card is also a J. So you follow the inputs to assert that the lower left card is a J.
       
       But now it turns out that you remembered wrong and the card was actually an A!. Now you keep the J in your deck too.
       ```
       Your New Hand:
       X X
       X X
       X
       ```
   3. If you want to discard this card and do nothing with it, press b. This is helpful if you have a card with a high point yield and you cannot discard it as in option 2 above
       
# Winning
The play continues till:
1. Someone is able to discard all their cards through option 2 above, so that their sum total becomes zero
2. You run out of cards in the main deck. Whoever has the lowest point total wins
3. Someone incorrectly guesses their cards in option 2 above and ends up having more than 6 cards in their hand

Have fun!
