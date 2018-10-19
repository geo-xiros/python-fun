import random

board = ['1','2','3',
         '4','5','6',
         '7','8','9']

winTests = (((2,3),(4,7),(5,9)),        #1
            ((1,3),(5,8)),              #2
            ((1,2),(5,7),(6,9)),        #3
            ((1,7),(5,6)),              #4
            ((1,9),(2,8),(3,7),(4,6)),  #5
            ((3,9),(4,5)),              #6
            ((1,4),(8,9),(5,3)),        #7
            ((7,9),(2,5)),              #8
            ((7,8),(3,6),(1,5)))        #9

RemainingChoices = ['1','2','3','4','5','6','7','8','9']

# Check if player (x or o) wins in position (pos)
def player_wins(player, pos):
    
    for i in winTests[pos]:
        win = True
        for j in i:
            if board[j-1] != player:
                win = False
        if win == True:
            return True
            
    return False    
        
# Print the board        
def print_board():
    for i in range(0,9,3):
        print('      |      |      ')
        print('  ' + board[i] + board[i] + '  |  ' + board[i+1] + board[i+1] + '  |  ' + board[i+2] + board[i+2] + '  ')
        print('  ' + board[i] + board[i] + '  |  ' + board[i+1] + board[i+1] + '  |  ' + board[i+2] + board[i+2] + '  ')
        print('      |      |      ')
        if i<=3:
            print('------|------|------')

# Ask for Player choice 
def player_choice(player):
    inp = input(player + ' select from 1 to 9: ')
    
    # choice must be one char, numeric and within remaining tiles
    while len(inp)!=1 or not inp.isnumeric() or not inp in RemainingChoices:
        inp = input(player + ' select from 1 to 9: ')
    
    # remove choice from available tiles
    RemainingChoices.remove(inp)

    return int(inp)-1

# Computer choose tile
def computer_choice(player):
    # Block other player
    rand = find_winning_move('o')

    # Find winning tile
    if rand == '0':
        rand = find_winning_move('x')
    
    # Random tile
    if rand == '0':
        rand = random.choice(RemainingChoices)
    
    # remove from available choices
    RemainingChoices.remove(rand)

    print (player + ' selection is ' + rand)
    return int(rand)-1

# Check all remaining tiles to find a winning move
def find_winning_move(playerLetter):
    for i in RemainingChoices:
        # return tile number if it wins
        if player_wins(playerLetter,int(i)-1):
            return i
        
    return '0'


# Play the game
def play_game(players, playersLetter, choiceFunc):
    
    player = 0
    print_board()
    
    while len(RemainingChoices) != 0:

        playerChoice = choiceFunc[player](players[player])
        
        board[playerChoice] = playersLetter[player]
        print_board()
        
        if player_wins(playersLetter[player],playerChoice):
            return players[player]

        if (player == 0):
            player = 1
        else:
            player = 0
    return 'No one'

#print(play_game(['Player x','Player o'], ['x','o'],[player_choice, player_choice]) + ' Wins !!!')
print(play_game(['Player x','Computer o'], ['x','o'],[player_choice, computer_choice]) + ' Wins !!!')

