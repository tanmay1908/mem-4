import random
import time
##########################################################################
# This code is divided into 3 classes: Player, deck and Game
# Player - holds the Player name & their hand
# deck - holds the shuffled card deck. Used to deal cards
#      - also used when performing different operations during each turn
# Game - Controls the overall flow of the program. 
#      - Creates a deck, shuffles it,manages turns and loops till a win
# FLOW - Game instantiates a deck in its contructor. 
#        deck instantiates two players in its constructor
# PLEASE READ THE README FILE FOR INSTRUCTIONS
###########################################################################


### PLAYER CLASS ###########
class Player:

    def __init__(self,Name):
        self.name = Name
        self.hand = []
#### deck CLASS ############
class deck:
    def __init__(self):
        # Create a deck
        self.__cards = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J']
        j = 16
        num = 10
        while j < 52:
            self.__cards.append(str(num)) # Add the numbered cards 10 - 2 to the deck
            j = j + 1
            if j % 4 == 0:
                num = num - 1

        i = 0
        self.__occupied = {} # This function is used in the shuffle function below 
                             # to keep track of which cards have been shuffled to which position
        while i < 52:
            self.__occupied[i] = False
            i = i + 1

        #### Set Player Names ####
        self.__p1 = Player(raw_input("Enter Name for Player 1:"))
        self.__p2 = Player(raw_input("Enter Name for Player 2:"))
        print("Thank you!")

        self.__turn = True # True when its Player 1's turn, False for Player 2
        self.__cardCounter = 8 # Starts at 8 because the first 8 cards are dealt to the players
        self.didWin = False # False when no one has won, True otherwise

        ### SHUFFLE FUNCTION ###
    def shuffle(self):
        shuffled = False
        new_deck = [None]*52
        i = 0
        while not shuffled :
                new_pos = random.randint(0,51)
                if self.__occupied[new_pos] == False:
                    new_deck[new_pos] = self.__cards[i]
                    self.__occupied[new_pos] = True
                    i = i+1
                    if i == 52:
                        shuffled = True
                        self.__cards = new_deck
                else:
                    continue
### Deal 4 cards to each player ###
    def deal(self):
        # Deal to Player 1
        print("%s, here are your cards!" % (self.__p1.name))
        self.__p1.hand.extend([self.__cards[0],self.__cards[1],self.__cards[2],self.__cards[3]])
        print("X  X")
        print("X  X")
        print("%s, look away! %s, I will now show you the bottom two cards for 5 seconds" % (self.__p2.name,self.__p1.name))
        print("\n %s  %s" % (self.__p1.hand[2],self.__p1.hand[3]))
        time.sleep(5)
        self.clearScreen()

        print("Alright, now %s \'s turn" % self.__p2.name)
        time.sleep(2)
        
        #Deal to Player 2
        print("%s, here are your cards!" % (self.__p2.name))
        self.__p2.hand.extend([self.__cards[4],self.__cards[5],self.__cards[6],self.__cards[7]])
        print("X  X")
        print("X  X")
        print("%s, look away! %s, I will now show you the bottom two cards for 5 seconds" % (self.__p1.name,self.__p2.name))
        print("\n %s  %s" % (self.__p2.hand[2],self.__p2.hand[3]))
        time.sleep(5)
        self.clearScreen()

    def playTurn(self):
        if self.__turn:
            p = self.__p1
        else:
            p = self.__p2

        print("It's %s \'s turn now. Card on the main deck is:" % p.name)
        print(self.__cards[self.__cardCounter])
        print("")
        self.showInstructions()
        print("")
        self.showHand(p)
        correct_input = False
        
        ### Dispatcher helps call the appropriate function corresponding to the user's input ###
        dispatcher = {'c':self.replace, 'v':self.combine, 'b':self.discard}

        while(not correct_input):
            play = raw_input("What do you want to do?")

            if play in dispatcher:
                correct_input = True
                dispatcher[play](p)
                
            else:
                print("Invalid entry, please try again")
                
        time.sleep(1)
        self.clearScreen()
        
        # Turn over next card from the main deck
        self.__cardCounter = self.__cardCounter +1
        
        # Pass the turn to the next player
        self.__turn = not self.__turn
     
        # Check if someone won
        if self.win(p):
            self.didWin = True
        else:
            self.didWin = False
            
            
#### Game Play functions corresponding to the three operations ####


    def replace(self,p):
        card_in_hand = {'q':0,'w':1, 'a':2, 's':3,'z':4, 'x':5}
        correct_in = False
        while not correct_in:
            input = raw_input("Which card would you like to replace this card with?")
            self.showHand(p)
            if input in card_in_hand and p.hand[card_in_hand[input]] != 'O':
                self.clearScreen()
                print("You replaced:")
                print(p.hand[card_in_hand[input]])
                p.hand[card_in_hand[input]] = self.__cards[self.__cardCounter]
                #print("Card Replaced!")
                #self.__cardCounter = self.__cardCounter + 1
                correct_in = True
            else:
                print("Invalid Input, please try again")

    def combine(self,p):
        card_in_hand = {'q':0,'w':1,'a':2, 's':3, 'z':4, 'x':5}
        correct_in = False
        while not correct_in:
            input = raw_input("Which card do you think is the same as this card?")
            self.showHand(p)
            if input in card_in_hand:
                self.clearScreen()
                print("You chose:")
                print(p.hand[card_in_hand[input]])
                if p.hand[card_in_hand[input]] == self.__cards[self.__cardCounter]:
                    print("You guessed right! You now have one less card to worry about!")
                    print("This empty space will now appear as an O")
                    p.hand[card_in_hand[input]] = 'O'
                else:
                    print("Oops, wrong card! Now you get to keep this card too")
                    p.hand.append(self.__cards[self.__cardCounter])
                    #print(p.hand)

                #self.__cardCounter = self.__cardCounter + 1
                correct_in = True
                #print("set true")
            else:
                print("Invalid Input, please try again")

    def discard(self,p):
        self.clearScreen()
        print("Discarded! Better Luck next time!")
        #self.__cardCounter = self.__cardCounter + 1


    def showHand(self,p):
        i = 0
        str = ""

        while i <  len(p.hand):
            if p.hand[i] == 'O':
                str = str + 'O   '
            else:
                str = str + 'X   '
            i = i + 1
            if i % 2 == 0 or i == len(p.hand):
                print(str)
                str = ""

    def reveal(self):
        i = 0
        strn = ""
        print("%s \'s cards:" % self.__p1.name)
        while i <  len(self.__p1.hand):
            strn = strn + str(self.__p1.hand[i]) + "  "
            i = i + 1
            if i % 2 == 0 or i == len(self.__p1.hand):
                print(strn)
                strn = ""

        i = 0
        print("%s \'s cards:" % self.__p2.name)
        while i <  len(self.__p2.hand):
            strn = strn + str(self.__p2.hand[i]) + "   "
            i = i + 1
            if i % 2 == 0 or i == len(self.__p2.hand):
                print(strn)
                strn = ""

    def win(self,p):
        all_empty = True
        i = 0
        while i < len(p.hand):
            if p.hand[i]!='O':
                all_empty = False
                break;
            i = i + 1
        if all_empty:
            print("%s has won the Game!" % p.name)
            return True

        elif self.__cardCounter == 52:
            self.reveal()
            #print(self.getSum(self.__p1))
            #print(self.getSum(self.__p2))
            if self.getSum(self.__p1) > self.getSum(self.__p2):
                print("%s has won the Game!" % self.__p2.name)
            elif self.getSum(self.__p1) < self.getSum(self.__p2):
                print("%s has won the Game!" % self.__p1.name)
            else:
                print("The game is a draw!")

            return True

        elif len(p.hand) > 6:
            print("Too many wrong guesses! You lost the game!")
            return True

        else:
            #print("No one has won yet")
            return False

    def getSum(self,p):
        i = 0
        sum = 0
        val_dict = {'A':1, 'K':12, 'Q':11, 'J':10, 'O':0}
        while i <  len(p.hand):
            if p.hand[i] in val_dict:
                sum = sum + val_dict[p.hand[i]]
            else:
                sum = sum + int(p.hand[i])
            i = i + 1
        return sum

    def showDeck(self):
        print(self.__cards)

    def clearScreen(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def showInstructions(self):
        print("You have 3 options:")
        print("If you like the card and want to replace it with one of your cards, press c")
        print("If you think you have this card in your hand and want to keep both of these cards into the central deck, press v")
        print("If you want to discard this card, press b")


class Game:

    def __init__(self):
        CardDeck = deck()
        CardDeck.shuffle()
        CardDeck.deal()
        print(CardDeck.didWin)
        while not CardDeck.didWin:
            CardDeck.playTurn()


#########################

#GAME PLAY#
new_game = True
while new_game:
    game = Game()
    correct_key  = False
    while not correct_key:
        input = raw_input("Do you want to exit (e) or play another game (p)?")
        if input == 'e':
            new_game = False
            correct_key = True
            print("Thank you for playing!")
        elif input == 'p':
            new_game == True
            correct_key = True
            print("Beginning new game")
        else:
            print("Invalid Entry")
