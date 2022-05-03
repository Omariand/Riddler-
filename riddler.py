from wsgiref.util import shift_path_info
from time import time
from time import sleep
import random 
import pandas as pd
import datetime 

class Riddler:
    """The Riddler Class represents how the game will played and the game it self
    this class will provide funtions that display the rules, starts the game and
    reads text files.
    """
    def __init__(self,player):
        """This displays the players name.

        Args:
            player (str): Player name
        Side effects:
            displays an instance of the variable."""
        self.player = player
        
        
    def game_rules(self):
        """This function displays the instruction to the player so they\
            understand what tasks need to be done and the rules.
        """
        print(f"Welcome Player. Are you ready to play The Riddler Game?\
            So here are the Rules\
            1. You will be given a riddle, that they have to answer \
                with a  timer that goes down every second you take \
            2.  If you make one mistake the time goes 10 to 20 to 30 seconds \
                faster and then this will continue until the BOMB goes off or  \
                you answer the riddle correctly\
            3. This will happen 5 times until the user saves the city and there \
                will be times for each bomb upcoming and there will be \
                significantly lower or harder as a riddle\
                compared to the last one.\
            4.The user or “Batman” if failed will have the city destroyed and\
                a statement would be printed that they lose.\
                Unless you win then a statement that you win will be diplayed ")

                #create seperate print statement for each line or triple quoted string.
                #if triple quoted string, create global variable at top.
    def read_riddle(self,r_file):
        """This takes a text file and reads the text file, then converts the 
        lines of the text file which will return the riddle given
        Args: 
            textfile
        Returns:
                Prints read riddle statement"""
        elist=[]
        with open(r_file,"r",encoding="utf-8") as f:
            for line in f:
                rlist=elist.append(line.strip("?"))  
                return rlist
        #capture the question including question mark with one capturing group 
        #capture the anwser with a capturing group

        #[^?] + 
    def read_answer(self, a_file):
        """This takes a text file reads the text file then converts the lines
        of the text file return the answer of the riddle
        Args: 
            self: an instance of the Riddler class
            param: textfile
        Returns:
                Prints Riddle answer"""
        elist=[]
        with open(a_file,"r",encoding="utf-8") as f:
            for line in f:
                alist=elist.append(line.strip("?",left))
                return alist    
    
    
        
class Time(Riddler):
    """ This Time class will keep track of time and create any time deductions
    that may be taken as the user answers the riddles"""
    
    def countdown(h, m, s):
        total_seconds = h * 3600 + m * 60 + s
        
        while total_seconds > 0:
            timer = datetime.timedelta(seconds = total_seconds)
            print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
 
    print(f"Oh No! It looks like you've ran out of time! You Lose")
    h = input("Enter the time in hours: ")
    m = input("Enter the time in minutes: ")
    s = input("Enter the time in seconds: ")
    countdown(int(h), int(m), int(s))   
   
    def play_game(self,player):
        """ This function will allow the player to guess the riddle through 
        amount of guesses. This will call the deduction method and for each\
            bad guess the deduction would be taken off. 
        Args: 
            str()s which may be the user input and holds that in until called for.
            
        Side effects: 
            displays information in the terminal.
        """
    
    words = []
    word = random.choice()
    
    guesses = ''
    turns = 12
    while turns > 0:
        failed = 0
        
        for ch in word:
            if ch in guesses:
                print(ch, end="")
                break
            else:
                guess = guess + ch

    def game_over(self):
        

            
    def winner(self,player):
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
            
        
    def time_deduction(self,player_time,game_time):
        """ For this method we will be using the import time to deduct time 
        as the player begins to answer the riddle. If the answer given the 
        timer will deduct 10 seconds for 1 wrong guess, 20 for 2 and 30 for 3. 
        If the play continously answers incorrectly the timer will keep deducting 
        30 seconds until the time is up
        Args:
        
        Side effects:
            modifies the value of the "game_time" variable. (mutable)
        Returns:
            (int): an updated variable "game_time" with the deducted \
                amount printed into the console.
         """     
        game_time = int(180("seconds remaining"))
            t1 = time()
            #input statement
            t2 = time()
            t2 - t1 = #seconds passed
            
            
        


        
            
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
    for riddle in textfile(args.file):
        # the !r tells the f-string to use the __repr__() method to generate
        # a string version of the address object
        return Riddler()          
            
    

    
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