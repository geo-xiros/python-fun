'''
Rock - Scissors - Paper PvsAI
Player chooses between rock / scissors / paper and the same is done by the computer in a random way. 
If someone wins the round he gets 1 point. 
The game is finished when someone gets 3 points.
'''

from random import randint

items = ('rock',
         'scissors',
         'paper',
         'pen')
loosingItems = (('scissors','pen'),
                ('paper','pen'),
                ('rock'),
                ('paper'))

# get winner
# if players2 choice is in loosingitems of player1 choice then player1 wins
def who_wins(p1,p2):
    if p1==p2:        
        return 'tie'
    elif items[p2] in loosingItems[p1]:
        return 'p1'
    else:
        return 'p2'

# Player choice
def get_player_choice():
	itemsToChoose = len(items)
	
	for i in range(itemsToChoose):
		print (str(i+1) + ') ' + items[i])

	playerChoice = input('Select between 1 and ' + str(itemsToChoose) + ' : ')

	while not (playerChoice >='1' and playerChoice <= str(itemsToChoose)):
		playerChoice = input('Please insert an number between 1 and ' + str(itemsToChoose) + ' : ')
	
	return int(playerChoice)-1

# Game
def play_game():
    playerScore = 0 
    computerScore = 0 

    while playerScore<3 and computerScore < 3:

        playerChoice = get_player_choice()
        computerChoice = randint(1, len(items))-1

        print ('Your choice is ' + items[playerChoice] + ', Computer choice is ' + items[computerChoice])
        
        winner = who_wins(playerChoice, computerChoice)
        
        if winner == 'p1':
            playerScore = playerScore + 1
            print (items[playerChoice],'wins',items[computerChoice], 'You win.')
        elif winner == 'p2':    
            computerScore = computerScore + 1
            print (items[playerChoice], 'loses from', items[computerChoice], 'Computer wins.')
        else:
            print ('It Is a tie.')
		
        print ('Your score : ' + str(playerScore) + ', Coputer score : ' + str(computerScore))

    if playerScore == 3:
        return 'You'
    else:
        return 'Computer'

print(play_game() + ' WON !!!')
