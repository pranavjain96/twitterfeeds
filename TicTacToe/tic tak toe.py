#!/usr/bin/env python
# coding: utf-8

# In[28]:


from IPython.display import clear_output


# In[29]:


def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[30]:


test_board=['#','X','X','X','O','O','X','O','X','O']
display_board(test_board)


# In[31]:


def player_input():
    marker=''
    
    while marker !='X' and marker !='O':
        marker=input('Player 1 :choose X or O ').upper()
    
    if marker=='X':
        return('X','O')
    else:
        return('O','X')


# In[32]:


def place_marker(board, marker, position):
    board[position]=marker


# In[33]:


def win(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    


# In[34]:


win(test_board,'X')


# In[ ]:


import random

def first():
    flip=random.randint(0,1)
    
    if flip==0:
        return 'player 2'
    else:
        return 'player 1'


# In[36]:


def space_avai(board,position):
    return board[position]==' '


# In[37]:


def full_check(board):
    for i in range(1,10):
        if space_avai(board,i):
            return False
    #board is full
    return True


# In[42]:


#ask player to select the board positon to place a marker
def choice(board):
    position=0
    
    while position not in range(1,10) or not space_avai(board,position):
        position=int(input('choose a position:(1-9)'))
        
    return position


# In[43]:


def replay():
    choice=input("play again? Enter Yes or No")
    
    return choice=='Yes'


# In[ ]:


print("welcome to tic tak toe")

while True:
    board_select=[' ']*10
    
    player1,player2=player_input()
    
    turn=first()
    print(turn+" will go first")
    
    play=input("Ready to play y or n ?")
    
    if play=='y':
        game_on=True
    else:
        game_on=False
    
    while game_on:
        if turn=='player 1':
            #show's board
            display_board(board_select)
            #choose a position
            position=choice(board_select)
            #place a marker
            place_marker(board_select,player1,position)
            #check if won
            if win(board_select,player1):
                display_board(board_select)
                print("Player 1 has won")
                game_on=False
            else:
                #check if no ie 
                if full_check(board_select):
                    display_board(board_select)
                    print("Tie Game")
                    game_on=False
            #of check its a tie or not
                else:
                    turn='player 2'
            #no tie no win i.e next player turn
        else:
            display_board(board_select)
            #choose a position
            position=choice(board_select)
            #place a marker
            place_marker(board_select,player2,position)
            #check if won
            if win(board_select,player1):
                display_board(board_select)
                print("Player 2 has won")
                game_on=False
            else:
                #check if no ie 
                if full_check(board_select):
                    display_board(board_select)
                    print("Tie Game")
                    game_on=False
            #of check its a tie or not
                else:
                    turn='player 1'
        
    if not replay():
        break


# In[ ]:




