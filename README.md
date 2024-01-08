# mastermind
Mastermind project

# How to run
- download as zip
- extract files
- install dependencies (numpy and pygame)
- run main.py

## Game abilities
Finished game meeting basic requirements.
- Use Pygame for your GUI
- Computer creates combination for user to guess
- Save game
- Load previous game
- Can choose colours, slots and guesses. 
- Can save 1 game, and load it.

## Rules
- Two game modes changers: duplicate mode and hard mode.
- Duplicate mode means that even if all of a certain colour is used up, if it is guessed in the wrong position it will still say it is in the colour code. Non-duplicate mode means the inverse.
- There is a hard mode which is actually just normal mastermind but is harder than the version i originally made so it's definitely harder! Instead of showing the results for each respective slot. It shows the highest value information (e.g. in the right spot) on the left down to the least valuable information (not in sequence).
- The answer colours are red, orange and green. The answer circle's positioning corresponds to the guesses positioning (in easy mode)
- Green signifies correct position and correct colour; orange means that the colour exists in the colour code and red means the colour is not in the code at all.
