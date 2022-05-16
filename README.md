Orange Juice 
INST-326 
Aric Bills
5/15/22
For our project, we decided to make a rendition of the Batman (2022) featuring the Riddler, a villain that uses riddles to commit crimes and if you solve them their plan is stopped. Riddler.py is our main python file. It is used to play the riddler game that we created.  You will be given a riddle to solve within 3 tries to try and save the city. Riddles.txt is the txt file which the riddles/answers are drawn from. 
`The first run “python3 riddler.py riddles.txt/”python riddler.py riddles.txt(Windows/Linux users)” should be typed into the terminal. Secondly, A riddle will appear, you will have 3 guesses to answer the riddle. Each word in the answer starts with a capital letter. Some answers will start with “A” or “The”.Third, you will guess the riddle when prompted. If you answer the riddle correctly, the program will ask you to play again. If your answer is wrong, you will be told how many tries you have left before losing the game. The game will only let you generate 3 tries. 
For our code in Magic Methods (Michael) used a __repr__ function to print out object rules to the player when you run the code and also a regular expression which was used to read from the riddles.txt file and break it down into 3 different captured groups; question number, question, answer. For the with statement (Omar) used a with statement was implemented into our riddler game, inside of the “read_riddle” function. Read_riddle takes the “with” statement and opens the riddles.txt to return each line. He also did the “argument parser” class which runs the main code and allows the file to go through the terminal correctly. (Danielle) had 2 instances of f-strings implemented, the first being inside of the __repr__ for the rules and the other inside of guess to print the correct answer to the player after a wrong or correct guess. Furthermore, with Conditional Expressions, the play game function uses a conditional statement to ask players if they'd like to play again. 














                                Annotated Bibliography
Play_game function -  Instructor (Professor Aric Bills, Nurul) helped our group by allowing us to initiate the variable that would hold the answer from the text file to make it equal to the guess. He also helped move the items from parse args to the play again. This allowed us to loop and call the items. 
Read _riddle function - Instructor (Daniel) helped our group with the read riddle function, making sure it iterates.
Regular expression - Regular Expressions example part 4 (Professor Aric Bills)
Conditional Statements - “Python Fundamentals 1” (Professor Aric Bills) 

