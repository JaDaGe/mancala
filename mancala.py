"""

File:    mancala.py
Author:  Jacob D. George
Date:    April 9, 2021
Section: 21
E-mail:  jgeorge4@umbc.edu
Description:
  this program does its best to play a game of mancala.
	

"""

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
   
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    
    for p in range(len(board)): #vertical: happens 13 times
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])): #horizontal: happens ~52 times
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1): #midline: happens 43 times (or from spot 7 to spot 50)
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)): #6 #CODES FOR THE GRID OF *s THROUGHOUT THE BOARD
        for p in range(len(board)): #13
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)): #THIS MAKES THE SEVENTH COLUMN OF STARS AND THE FIRST LINE (FOR SOME REASON) CODES FOR THE FIRST COLUMN OF STARS TO MAKE THEM A COLUMN OF STARS AGAIN
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)): 
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)


    

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))
   


def draw_mancala(fore_or_aft, mancala_data, the_board):
 
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = (mancala_data[i][0: BLOCK_WIDTH]).rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]

    else:
        for i in range(len(mancala_data)):
            data = (mancala_data[i][0: BLOCK_WIDTH]).rjust(BLOCK_WIDTH)
            
            for j in range(len(mancala_data[0])):
                
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
 
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]


def get_player():
    #this function asks for the players names and returns it as a list
    player1 = input('Player 1, please enter your name: \n')
    player2 = input('Player 2, please enter your name: \n')
    players = [player1,player2]
    return(players)


def take_turn(player,  player_number, stones_list, repeat_condition, players):
    #cup_num_to_list_spot is used to determine which cup number corresponds to the spot on the list of stone values.
    # notice 6 and 13 are missing due to the fact that those are the spots of the mancalas
    cup_num_to_list_spot = {
            '1' : 0,
            '2' : 1,
            '3' : 2,
            '4' : 3,
            '5' : 4,
            '6' : 5,
            '8' : 7,
            '9' : 8,
            '10' : 9,
            '11' : 10,
            '12' : 11,
            '13' : 12
            }
    #following code determines if the player's selection was a valid one
    player_choice = str(input(str(player) + ' what cup number do you want to select? \n'))
    is_choice_valid = 0
    while is_choice_valid == 0:
        if (player_choice in cup_num_to_list_spot) and (stones_list[cup_num_to_list_spot[player_choice]] != 0): #if player choice is a valid cup options:
            is_choice_valid = 1
        else: # if player_choice is not a valid cup option:
            player_choice = str(input(str(player) +', please enter a valid cup number as an integer. Make sure the cup has stones in it and that you aren\'t selecting a mancala! \n'))
    
    repeat_condition_eval = empty_cup(player_choice,cup_num_to_list_spot,stones_list, repeat_condition, players)
    #repeat_condition (in empty_cup) and repeat_condition_eval is used to determine whether or not the player needs to play again (if their last stone landed in a mancala)
    return(repeat_condition_eval)

def super_subtle_subliminal_message():
    #if you're saw this. no you don't because you did. no you didnt <3
    print('thA+nks for plA+ying my mA+ncA+lA+ gA+me!!')


def empty_cup(cup_number,cup_num_to_list_spot, stones_list, repeat_condition, players):

        #the following code empties the selected cup of stones        
        selection = cup_num_to_list_spot[cup_number]
        cup_amount = stones_list[selection]
        stones_list[selection] = 0

        #this code redistributes the stones removed from the selected cup into the next cups
        #x,y, and z are variables which can correspond to spots on the stones_list list. therefore they are used to determine which cup
        #is being added to.
        x = 1
        y = 0
        z = 0
        last_cup = 0 #basically i wanna set this variable equal to the last cup that gets added to,
                    #and if it is equal to the spot of a mancala, then the repeat condition would be activated and the player would play again
        
        while x <= cup_amount:
            if selection+x <= (len(stones_list)-1):
                stones_list[(selection+x)] = stones_list[(selection+x)] + 1
                x += 1
                last_cup = selection+x
            elif y < 14: 
                stones_list[y] += 1
                last_cup = y
                y += 1
                x += 1
            else:
                stones_list[z] += 1
                last_cup = z
                z += 1
                x += 1

        mancala_a_position = 7
        mancala_b_position = 14
        if (last_cup == mancala_a_position) or (last_cup == mancala_b_position):
                repeat_condition += 1
                end_assesment = petty_function(players, stones_list)
                if end_assesment == 0:
                    print('You\'re last stone was placed in a mancala. Go again.')
           
        return(repeat_condition)

def select_winner(players, stones_list):
    #the first if statement determines if all of the cups in the top row are empty.
    #if that is the case, then it counts the stones in each mancala and declares a winnner based on that.
    #this function returns 0 if there is no winner, so that the end_condition in run_game is not fulfilled
    #or it returns 1 so that the end_condition is fulfilled, which would end the game when it chooses a winner.
    if (stones_list[0:6] == [0, 0, 0, 0, 0, 0]) or (stones_list[7:13] == [0, 0, 0, 0, 0, 0]):
        if stones_list[6] < stones_list[13]:
            print(players[0] + ' is the winner!')
        elif stones_list[13] < stones_list[6]:
            print(players[1] + ' is the winner!')
        elif stones_list[6] == stones_list[13]:
            print('There has been a tie. The player that has most recently showered will be delcared as the winner.')
            print('Sorry, losing player. Please take this as a learning opportunity and go bathe <3.')
        
        return(1)
    else:
        return(0)
    
def petty_function(players, stones_list):
    #petty_function was just added to fix a minor technical issue. it's not very important.
    #the minor issue was that when a player ended the game with a move that ended in a mancala, the code would
    #print 'You\'re last stone was placed in a mancala. Go again.' and then also print '(player) is the winner!'
    #I could have used the select_winner function to accomplish the same goal, but then the code would print
    #the line declaring the winner two times instead of once.
    if (stones_list[0:6] == [0, 0, 0, 0, 0, 0]) or (stones_list[7:13] == [0, 0, 0, 0, 0, 0]):
        return(1)
    else:
        return(0)

def set_board(players,stones_list):
    #this function defines the top_cups and the bottom_cups in the form of a 2d list(sorry, I accidentally renamed them to cup_1 and cup_2)
    #it also defines the mancalas in the form of a 1d list
    #these lists are then plugged into the built-in draw_board function to draw the board.
    
    cup_1 = [
        ['cup   ','     1','Stones',str(stones_list[0]),'      '],
        ['cup   ','     2','Stones',str(stones_list[1]),'      '],
        ['cup   ','     3','Stones',str(stones_list[2]),'      '],
        ['cup   ','     4','Stones',str(stones_list[3]),'      '],
        ['cup   ','     5','Stones',str(stones_list[4]),'      '],
        ['cup   ','     6','Stones',str(stones_list[5]),'      ']
        ]
    cup_2 = [
        ['cup   ','    13','Stones',str(stones_list[12]),'      '],
        ['cup   ','    12','Stones',str(stones_list[11]),'      '],
        ['cup   ','    11','Stones',str(stones_list[10]),'      '],
        ['cup   ','    10','Stones',str(stones_list[9]),'      '],
        ['cup   ','     9','Stones',str(stones_list[8]),'      '],
        ['cup   ','     8','Stones',str(stones_list[7]),'      ']
        ]
    mancala_a = [
        '      ',
        '      ',
        '      ',
        players[0].rjust(BLOCK_WIDTH),
        '      ',
        '      ',
        '      ',
        'stones'.rjust(BLOCK_WIDTH),
        str(stones_list[13]),
        '      ',
        '      ',
                ]
    mancala_b = [
        '      ',
        '      ',
        '      ',
        players[1].rjust(BLOCK_WIDTH),
        '      ',
        '      ',
        '      ',
        'stones'.rjust(BLOCK_WIDTH),
        str(stones_list[6]),
        '      ',
        '      ',
                ]
    
    draw_board(cup_1,cup_2,mancala_a,mancala_b)
        
    pass

def run_game():
    #following code is used to draw the board
    stones_list = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
    stones = str(stones_list)
    
    players = get_player()
    set_board(players,stones_list)

    
    #following code is used to take turns, set up the conditions for which players get multiple turns, set up the condition
    #for which the game ends, and determines the cups that the players can select.
    turn_condition = 0
    repeat_condition = 0
    end_condition = 0
    
    while end_condition == 0:
        
        repeat_condition = 0
        if (turn_condition % 2) == 0:
            repeat_condition_eval = take_turn(players[0],1, stones_list,repeat_condition, players)
            if repeat_condition_eval == 0:
                turn_condition += 1
                
        elif (turn_condition % 2) != 0:
            repeat_condition_eval = take_turn(players[1],2, stones_list, repeat_condition, players)
            if repeat_condition_eval == 0:
                turn_condition += 1
        
        set_board(players,stones_list)
        end_condition = select_winner(players,stones_list)
        

    super_subtle_subliminal_message()



      
if __name__ == "__main__":
    
    #the following code runs the game
    run_game()
    
    
