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

def player_wins(player, pos):
    
    for i in winTests[pos]:
        win = True
        for j in i:
            if board[j-1] != player:
                win = False
        if win == True:
            return True
            
    return False    
        
def print_board():
    for i in range(0,9,3):
        print('   |   |   ')
        print(' ' + board[i] + ' | ' + board[i+1] + ' | ' + board[i+2] + ' ')
        print('   |   |   ')
        if i<=3:
            print('---|---|---')

def player_choice(player):
    inp = input(player + ' select from 1 to 9: ')
    while len(inp)!=1 or not inp.isnumeric():
        inp = input(player + ' select from 1 to 9: ')
    return int(inp)-1
    
def play_game(players, playersLetter):

    player = 0
    print_board()
    
    for i in range(9):
        
        playerChoice = player_choice(players[player])
        board[playerChoice] = playersLetter[player]
        print_board()
        
        if player_wins(playersLetter[player],playerChoice):
            return players[player]

        if (player == 0):
            player = 1
        else:
            player = 0
    return 'No one'

print(play_game(['Player x','Player o'], ['x','o']) + ' Wins !!!')

