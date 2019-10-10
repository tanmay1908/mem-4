# About the code

## Classes <br>
The code for the game is divided into 3 classes:
1. Player <br/>
  Stores information about the Players' names, and their hands (the set of cards dealt to them from the deck)
2. deck <br/>
  Stores the card deck. Has functions that shuffle the deck, deal cards to the players, shows the cards, shows the instructions and others. This is the class that handles the inner working of the gameplay
3. Game<br>
  Manages the overall game. The deck is initialized in this class, and it keeps calling the play turn method from the deck until a player has won
  
## External Libraries used
Two external libraries were used in the code:

1. random<br>
   This library includes functions that allow for the generation of random numbers between a lower and upper limit. This method was used to shuffle the class and assign a card to a random position in the deck
2. time<br>
  This library includes the time.sleep() method that was used to add delays to the code. This was mainly used to give players time to remember their revealed cards and create a better game experience

## Data Structures employed

1. Dictionaries <br>
 <b> Key - value pairs for relating keyboard input to a list index </b> <br>A lot of the implementations in the code use dictionaries, specifically because of their key - value pair structures. Dictionaries allow for quick and easy retrieval of data when given a key. This was particularly helpful when the user's input from the keyboard was correlated to a particular index in the list of cards.
 <br><b> As a function dispatcher </b><br> A dictionary was also used as a function dispatcher in assesing which of the three play operations the user wanted to perform. Again, because of the key-value pairs structure of dictionaries, it is very easy to relate a user's input on the keyboard to a function defined within the class. This allo0ws the code to be much shorter than multiple if elif statements and is easier to read.
2. Lists<br>
  Lists were used to store the deck of cards and the hands of each player because they are mutable and their data can be easily accessed through their indices. Therefore, shuffling the card was the same as reassigning indexes to the card and these indices could be easily referenced nthrough the key-value pairs in dictionaries as described above.
