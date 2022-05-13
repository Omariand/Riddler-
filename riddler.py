from argparse import ArgumentParser
import random 
from random import choice 
import re
import sys




def read_riddle(filename):
        """This takes a text file and reads the text file, then converts the 
    lines of the text file which will return the riddle given
    Args: 
        textfile
    Returns:
            Prints read riddle statement"""
        
        with open(filename,"r",encoding="utf-8") as f:
            lines=  f.readlines()
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
                question_number=searchtxt.group("question_number")
                question=searchtxt.group("question")
                answer=searchtxt.group("answer")
                self.riddle_dict[question.strip()]=answer.strip()
            self.question_list=list(self.riddle_dict)
            #look up key inside the dictionary and have it be equal to answer
            self.example_question= " What has a ring but no finger? "
            self.example_answer = "A Phone"
    def __repr__(self):
        """This function displays the instruction to the player so they
            understand what tasks need to be done and the rules.
        """
        rules = f"""Welcome Player. 
        Are you ready to play The Riddler Game?
            Here are the Rules:
            
            1. You will be given a riddle, that they have to answer.
                
            2.  Either you make mistake or you answer the riddle correctly.
                
            3. This will happen 3 times until the user saves the city and there
                will be times for each bomb upcoming and there will be
                significantly lower or harder as a riddle compared to the last
                    one.
            
            4.The user or “Batman” if failed will have the city destroyed and
                a statement would be printed that they lose.
                Unless you win then a statement that you win will be diplayed
                
            "Here's an example question{self.example_question} and here's
            and example answer we're looking for:{self.example_answer}"
            """
        print(rules)
    
    def guess(self):
            """Holds user answers and questions and give it to them, """ 
            turns=3
            
            
            while turns > 0:
                randomq=random.choice(self.question_list)
                print(randomq)
                self.userguess=input("Make your guess:")
                answer= self.riddle_dict[randomq]
                if self.userguess != answer: 
                    turns=turns-1
                    if turns ==2:
                        print("You got two wires left Batman, you are CUTTING it close AHAHAHAHA.")
                    if turns ==1:
                        print("You got one more left I would be SHIVERING in my boots if I was you :\)")
                    if turns ==0:
                        print(f"Game over Batman you lost! The correct answer was {answer}")    
                else:
                    print(f"{answer} is the correct answer good job Batman! You saved the day")
                    return answer
            
                         
def play_game(filename):
    """ This fuction will provide the player to either continue the game
    or end the game if they get the riddle correct. If the player beats all 
    of the riddles they will recive a congratulatory message.
    Args:
    
    Side effects:
        Displays information of the winner in the terminal.
    """

        
    while True:
        game= Riddler(filename)
        game.__repr__()
        game.guess()
        new_round = input("Would you like to play again <:^)yes/no")
        if new_round.lower() == "no":
            print("Oh Well, See You Next Time.")
            break 
        else:
            new_round.lower() == "yes"
    
       
                
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
    play_game(args.file)

#Regex, - Mike
# With Statements, ArgumentParser - Omar
# Conditional Expression, F-String - Danielle