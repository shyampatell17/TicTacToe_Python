#!/usr/bin/env python
# coding: utf-8

# # Project : Tic Tac Toe

# **Step 1: A function that can print out a board. Setting the board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[53]:


from IPython.display import clear_output

def display_board(board):
    print('   |   |')
    print(' ' + board[7]+ ' | ' +board[8]+ ' | ' +board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4]+ ' | ' +board[5]+ ' | ' +board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1]+ ' | ' +board[2]+ ' | ' +board[3])
    print('   |   |')
    pass


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[54]:


test_board = ['X']*10
display_board(test_board)


# **Step 2: This is the function that can take in a player's input and assign their marker as 'X' or 'O'. Using *while* loops to continually ask until you we get a correct answer.**

# In[7]:


def player_input():
    
    marker = ''
    
    # Asking Player 1 to choose from X or O
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
        
     # Asking Player 2, the opposite marker
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
            
    return (player1, player2)


# **TEST Step 2:** run the function to make sure it returns the desired output

# In[8]:


player1_marker , player2_marker = player_input()


# In[9]:


player1_marker


# **Step 3: The following function takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[10]:


def place_marker(board, marker, position):
    
    board[position] = marker


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# In[11]:


place_marker(test_board,player2_marker,8)
display_board(test_board)


# **Step 4: This is the function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[12]:


def win_check(board, mark):
    
    # Checks all rows, to see all have the same marker
    return ((board[1] == board[2] == board[3] == mark) or 
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
    # Checks all column, to see all have the same marker
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
    # Checks 2 diagonals, to see all have the same marker
            (board[1] == board[5] == board[9] == mark) or
            (board[7] == board[5] == board[3] == mark)
           )
    
    pass


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[13]:


display_board(test_board)
win_check(test_board,'X')


# **Step 5: This is the function that uses the random module to randomly decide which player goes first. Using the function and random library to lookup random.randint() which returns a string of which player went first.**

# In[14]:


import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# **Step 6: This is the function that returns a boolean indicating whether a space on the board is freely available.**

# In[15]:


def space_check(board, position):
    
    return board[position] == ' '


# **Step 7: The following is the function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[16]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    
    # For if the table is full
    return True


# **Step 8: This is the function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[17]:


def player_choice(board):
    
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))
        
    return position


# **Step 9: This is the function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[18]:


def replay():
    
    choice = 'wrong'
    
    while choice not in ['Y', 'N']:
        
        choice = input("Keep playing (Y or N): ")
        
        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand please choose Y or N")
            
    if choice == 'Y':
        return True
    else:
        return False


# **Step 10: Using while loops and the functions you've made to run the game!**

# In[19]:


print('Welcome to Tic Tac Toe!')

while True:

    
    # PLAY THE GAME
    
    # Setting up everything (Board, Who is first, Choosing markers X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input("Ready to play? Y or N?")
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    # GAMEPLAY
    
    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            
            #Showimg the board
            display_board(the_board)
            
            #Choose a position
            position = player_choice(the_board)
            
            #Place the marker on the position
            place_marker(the_board, player1_marker, position)
            
            #Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                #Check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('THE GAME IS A TIEE!!')
                    break
                else:
                    turn = 'Player 2'
                    
        #Player 2 Turn
        else:
            #Showimg the board
            display_board(the_board)
            
            #Choose a position
            position = player_choice(the_board)
            
            #Place the marker on the position
            place_marker(the_board, player2_marker, position)
            
            #Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                #Check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('THE GAME IS A TIEE!!')
                    break
                else:
                    turn = 'Player 1'
        

    if not replay():
        break

