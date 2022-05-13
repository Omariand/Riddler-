from argparse import ArgumentParser
import random 
from random import choice 
import re
import sys
emptydict={}
LEN_GUESSES = 3

class Riddler:
    """The Riddler Class represents how the game will played and the game it self
    this class will provide funtions that display the rules, starts the game and
    reads text files.
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
    
    def read_riddle(r_file):
        """This takes a text file and reads the text file, then converts the 
    lines of the text file which will return the riddle given
    Args: 
        textfile
    Returns:
            Prints read riddle statement"""
        with open(r_file,"r",encoding="utf-8") as f:
            lines=[line for line in f.readlines()]
        return lines  

    def __init__(self,rtxt,read_riddle):
            """This displays the players name.

            Args:
                player (str): Player name
            Side effects:
                displays an instance of the variable."""
            self.riddle_dict={}
            expr = r"""
            (?xm)
            ^
            (?:(?P<question_number>\d(?:\d)?\.)\s)
            (?P<question>[^?\n]+.\s))
            """
            
            riddle_list = read_riddle(rtxt)
            for riddle in riddle_list:
                searchtxt=re.search(expr,riddle)
                self.question_number=searchtxt.group("question_number")
                self.question=searchtxt.group("question")
                self.answer=searchtxt.group("answer")
                self.riddle_dict[self.question.strip()]=self.answer
                
    def __repr__(self):
        "Return formal riddle of the code"
        return (
            f"question: {self.question}\n"    
            f"answer:   {self.answer}\n")


  
    
    def play_game(self):
        """ This function will allow the player to guess the riddle through 
        amount of guesses. This will call the deduction method and for each bad.
            guess the deduction would be taken off. 
        Args: 
            str()s which may be the user input and holds that in until called for.
            
        Side effects: 
            displays information in the terminal.
        """
    
    answers = ["Eggs","Sponge","The Future","Darkness","Teapot","A Stamp", \
        "A Clock","Age", "Silence","A Fire"]
    answer = random.choice(answers)
    guess = input(" ") 
    turns = 3
    while turns > 0:
        failed_attempts = 0 
        for ans in answer:
            if ans in answer:
                print(ans, end = " ")
            else:
                print(ans, end= " ")
                failed_attempts += 1
        if failed_attempts == 0:
            print("Good Job Batman")
            
            
    if guess == answer:
        print("Well Done Batman, onto the next riddle. Let's see if you can\
            answer this one correctly")
    elif guess != answer:
        print("Good Try! But your answer was WRONG... Try Again >:) ")

    def game_over():
        
    

                
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
    game.play_game()
    
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