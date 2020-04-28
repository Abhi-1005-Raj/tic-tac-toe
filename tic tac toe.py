#                      ------TIC TAC TOE------

# --Global Varialble--

# List to store 
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

game_still_going=True
winner = None
current_player="X"

# display board function
def display_board():
  print(board[0]+ " | "+board[1]+" | "+board[2]+"     1 | 2 | 3")
  print(board[3]+ " | "+board[4]+" | "+board[5]+"     4 | 5 | 6")
  print(board[6]+ " | "+board[7]+" | "+board[8]+"     7 | 8 | 9")




# ------MAIN GAME LOGIC------
"""First display board...
   Make loop to continue game..
   Handle turn between players "X" and "O"...
   Check if game is over or not...
   If game not over, FLIP PLAYER..."""
   
def play_game():

  display_board()                  

  while game_still_going:            
    
    handle_turn(current_player)      

    check_if_game_over()              

    flip_player()                     

# End of GAME

# Printing Winner.
  if winner == "X" or winner == "O":
    print(" ---- "+ winner + " won.---- ")
  elif winner == None:
    print("--Tie.--")

# ------END OF GAME LOGIC------


# To handle player,s turn
def handle_turn(player):
  print(player + "'s Turn.")
  position = input("Choose form 1-9 :")
# Loop if wrong input
  valid=False

  while not valid:
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Choose form 1-9 :")
 
    position = int(position) - 1
    if board[position] == "-":
     valid=True
    else:
      print("Wrong input. Go again")

  board[position]=player
  display_board()
  
  
# Conditions for game over
def check_if_game_over():
  check_if_win()
  check_if_tie()
  return



# Check fow win
def check_if_win():
    
  # Set global variable. 
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # If row, column or diagonal completed
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return


# To check for tie
def check_if_tie():
  """Taking global variable that is set to True and make it false""" 
  global game_still_going                                          
  if "-" not in board:               
    game_still_going = False
  return



# ---To check for row---
def check_rows():
  # Setting global variable
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_going = False
    
  # Return the winner "X or O"
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[7]
  else:
    return None



#--To check columns for win--
def check_columns():
    
  # Setting global variable
  global game_still_going
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  if column_1 or column_2 or column_3:
    game_still_going = False
    
  # Return the winner "X or O"
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return



#--To check diagonal--
def check_diagonals():
  # Setting global variable
  global game_still_going
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    game_still_going = False

  # Return the winner "X or O"
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return


# TO change player from "X" to "O" and vice versa
def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return

play_game()












# board
# display board
# loop
  # play game
  # player turn handle
  # check for winner or tie
    #check rows,column,diagonals
  # change player turn
# result

