
from argparse import ArgumentParser
import time
from time import *
from time import sleep
import datetime
import random 
from random import choice 
import re
import sys
emptydict={}
LEN_GUESSES = 3

def read_riddle(filename):
        """This takes a text file and reads the text file, then converts the 
    lines of the text file which will return the riddle given
    Args: 
        textfile
    Returns:
            Prints read riddle statement"""
        
        with open(filename,"r",encoding="utf-8") as f:
            lines=[line for line in f.readlines()]
        return lines 
                

class Riddler:
    """The Riddler Class represents how the game will played and the game it self
    this class will provide funtions that display the rules, starts the game and
    reads text files.
    """
    def __init__(self,filename):
            """This displays the players name.

            Args:
                player (str): Player name
            Side effects:
                displays an instance of the variable."""
            self.riddle_dict={}
            expr = r"""(?xm)
            ^
            (?:(?P<question_number>\d(?:\d)?\.)\s)
            (?P<question>[^?\n]+.\s)
            (?:(?P<answer>.+))
            """
            riddle_list=read_riddle(filename)
            for riddle in riddle_list:
                searchtxt=re.search(expr,riddle)
                self.question_number=searchtxt.group("question_number")
                self.question=searchtxt.group("question")
                self.answer=searchtxt.group("answer")
                self.riddle_dict[self.question.strip()]=self.answer
                

            #add guesses to the init method and good guesses and bad guesses to be stored as a set
            #make a dictionary of the riddle and then complies them 
            #dictionary may have easier functionality 
            #need to be stored somewhere, maybe list of tuples
        
        #add guesses to the init method and good guesses and bad guesses to be stored as a set
   
    def game_rules(self):
        """This function displays the instruction to the player so they
            understand what tasks need to be done and the rules.
        """
        rules = f"""Welcome Player. 
        Are you ready to play The Riddler Game?
            Here are the Rules:
            
            1. You will be given a riddle, that they have to answer 
                with a  timer that goes down every second you take .
                
            2.  If you make one mistake the time goes 10 to 20 to 30 seconds 
                faster and then this will continue until the BOMB goes off or you answer the riddle correctly.
                
            3. This will happen 5 times until the user saves the city and there will be times for each bomb upcoming and there will be
                    significantly lower or harder as a riddle compared to the last one.
            
            4.The user or “Batman” if failed will have the city destroyed and
                a statement would be printed that they lose.
                Unless you win then a statement that you win will be diplayed
                """
        print(rules)
    
    def guess(self):
            """Holds user answers and questions and give it to them, """
            self.userguess=input("Make your guess")
            turns=3
            while turns > 0:
                print(self.question)
                self.userguess=input("Make your guess")
                if self.userguess is not self.answer:
                    turns=turns-1
                    print("You got it wrong try again.")
                    
                else:
                    print(f"{self.answer} is the correct answer good job Batman!")
                    return self.answer
                    
class Time(Riddler):
    """ This Time class will keep track of time and create any time deductions
    that may be taken as the user answers the riddles"""
    
    def countdown(self):
            m = input("Enter the time in minutes:")
            m=int(m)
            total_seconds = m * 60
            while total_seconds > 0:
                timer = datetime.timedelta(seconds = total_seconds)
                print(timer, end="\r")
                if m > 3:
                    print("I told you only 3 minutes! NO MORE THAN THAT")
                    break
                sleep(1)
                total_seconds-=1
            print("Oh No! It looks like you've ran out of time.\
                    You set off the bomb Batman, lets see how you'll save Gotham now")

    def play_game(self):
        """ This function will allow the player to guess the riddle through 
        amount of guesses. This will call the deduction method and for each bad.
            guess the deduction would be taken off. 
        Args: 
            str()s which may be the user input and holds that in until called for.
            
        Side effects: 
            displays information in the terminal.
        """
        #play_round method in class
        Riddler.game_rules()
        time_left= Time.countdown()
        #change this as well
        Riddler.riddle_dictx
        guesses = input(" ")
        #while guesses <3 and Time.countdown():
        #change this all of it, 
        word = choice(self.guesses)
        for riddle in word:
            if riddle in LEN_GUESSES:
                    break
            else:
                guess = guess + riddle
                break
        return guess 
        
        if guess == self.answer:
            
            print("Well Done Batman, onto the next riddle. Let's see if you\
                 can answer this one correctly")
            #elif guess != self.answer:
                #print("Good Try! But your answer was WRONG... Try Again >:) ")
     
                
    def game_over(self):
        """stops game if the player answers the game correclty or the \
            time runs out."""
         
                

            
    def play_again(self):
        """ This fuction will provide the player to either continue the game
        or end the game if they get the riddle correct. If the player beats all 
        of the riddles they will recive a congratulatory message.
        Args:
        
        Side effects:
            Displays information of the winner in the terminal.
        """
        player= input("Would you like to play again <:^)")
         
        while player !="no":
            self.play_game()
        else: 
            print("Thank you for trying to save Gotham Batman you failed \
                though. ?<.,>???>?><?>?>?-Riddler")
            

        
                
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
        the parsed arguments.     
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing one address per line")
    return parser.parse_args(arglist)

if __name__ == "__main__": 
    args = parse_args(sys.argv[1:])
    game= Riddler(args.file)
    game.game_rules()
    game.guess()
    
    time = Time(args.file)
    
    
        # the !r tells the f-string to use the __repr__() method to generate
        # a string version of the address object
    
        #flow chart of how your code should flow and then structure the name block     
    

    
        #for guesses or like guess class
    #make a function that takes the guesses
    #a way to take off time from the counter when a bad guess is inputed
    #2 minutes for a guess, 1st guess takes off 10 seconds, 2nd takes off 20 seconds
    #3rd is 30 seconds. after 3rd guess every guess is 30 seconds
    

    #loop - would be inside the guessing and the time
    #loop - for the riddle (repeating the riddle)
    #if statement - if guess is correct, winner moves to next round
    #next round function - play game, rules, winner function
    #read txt file (1) - would read the file and take riddles
    #read txt file (2) - would read the file and take anwsers
    
#Time.countdown()