import random
import time

class Player:

    def __init__(self,Name):
        self.name = Name
        self.hand = []

class deck:
    def __init__(self):
        self.__cards = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J']
        j = 16
        num = 10
        while j < 52:
            self.__cards.append(str(num))
            j = j + 1
            if j % 4 == 0:
                num = num - 1

        i = 0
        self.__occupied = {}
        while i < 52:
            self.__occupied[i] = False
            i = i+1

        #### Set Player Names ####
        self.__p1 = Player(raw_input("Enter Name for Player 1:"))
        self.__p2 = Player(raw_input("Enter Name for Player 2:"))
        print("Thank you!")

        self.__turn = True #True when its Player 1's turn, False for Player 2
        self.__cardCounter = 8
        self.didWin = False

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

        print("It's %s \'s turn now" % p.name)
        print(self.__cards[self.__cardCounter])
        print()
        self.showInstructions()
        print()
        self.showHand(p)
        correct_input = False
        dispatcher = {'c':replace, 'v':combine, 'b':discard}

        while(not correct_input):
            play = raw_input("What do you want to do?")

            if play in dispatcher:
                correct_input = True
                dispatcher[play](p)
            else:
                continue

        self.__cardCounter = self.__cardCounter +1
        self.__turn = not self.__turn

        if self.win(p):
            self.didWin = True
        else:
            self.didWin = False

    def replace(self,p):
        card_in_hand = {'q':0,'w':1, 'a':2, 's':3}
        correct_in = False
        while not correct_in:
            input = raw_input("Which card would you like to replace this card with?")
            self.showHand(p)
            if input in card_in_hand:
                self.clearScreen()
                print(p.hand[card_in_hand[input]])
                p.hand[card_in_hand[input]] = self.__cards[self.__cardCounter]
                self.showDeck("Card Replaced!")
                self.__cardCounter = self.__cardCounter + 1
                correct_in = True
            else:
                print("Invalid Input, please try again")

    def combine(self,p):
        card_in_hand = {'q':0,'w':1, 'a':2, 's':3}
        correct_in = False
        while not correct_in:
            input = raw_input("Which card do you think is the same as this card?")
            self.showHand(p)
            if input in card_in_hand:
                self.clearScreen()
                print(p.hand[card_in_hand[input]])
                if p.hand[card_in_hand[input]] == self.__cards[self.__cardCounter]:
                    print("You guessed right! You now have one less card to worry about!")
                    print("This empty space will now appear as an O")
                    p.hand[card_in_hand[input]] = 'O'
                else:
                    print("Oops, wrong card! Now you get to keep this card too")
                    p.hand.append(self.__cards[self.__cardCounter])

                self.__cardCounter = self.__cardCounter + 1
                correct_in = True
            else:
                print("Invalid Input, please try again")

    def discard(self):
        print("Discarded! Better Luck next time!")
        self.__cardCounter = self.__cardCounter + 1

    def showHand(self,p):
        i = 0
        while i <  len(p.hand):
            if p.hand[i] == 'O':
                print('O   ')
            else:
                print('X   ')
            i = i + 1
            if i % 2 == 0:
                print("\n")
            #print("X  X    (q)  (w)")
            #print("X  X    (a)  (s)")
    def reveal(self):
        i = 0
        print("%s \'s cards:" % self._p1.name)
        while i <  len(self.__p1.hand):
            print("%s   " % self.__p1.hand[i])
            i = i + 1
            if i % 2 == 0:
                print()

        i = 0
        print("%s \'s cards:" % self._p2.name)
        while i <  len(self.__p2.hand):
            print("%s   " % self.__p2.hand[i])
            i = i + 1
            if i % 2 == 0:
                print()

    def win(self,p):
        all_empty = True
        i = 0
        while i <  len(p.hand):
            if p.hand[i]!='O':
                all_empty = False
                break;
        if all_empty:
            print("%s has won the Game!" % p.name)
            return True

        elif self.__cardCounter == 52:
            self.reveal()
            if getSum(self.__p1) > getSum(self.__p2):
                print("%s has won the Game!" % self.__p1.name)
            elif getSum(self.__p1) < getSum(self.__p2):
                print("%s has won the Game!" % self.__p2.name)
            else:
                print("The game is a draw!")

            return True

        else:
            print("No one has won yet")
            return False

    def getSum(self,p):
        i = 0
        sum = 0
        val_dict = {'A':1, 'K':12, 'Q':11, 'J':10}
        while i <  len(p.hand):
            if p.hand[i] in val_dict:
                sum = sum + val_dict[p.hand[i]]
            else:
                sum = sum + int(p.hand[i])

            return sum

    def showDeck(self):
        print(self.__cards)

    def clearScreen(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def showInstructions(self):
        print("You have 4 options:")
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
        input = raw_input("Do you want to quit (q) or play another game (p)?")
        if input == 'q':
            new_game = False
            correct_key = True
            print("Thank you for playing!")
        elif input == 'p':
            new_game == True
            correct_key = True
            print("Beginning new game")
        else:
            print("Invalid Entry")
