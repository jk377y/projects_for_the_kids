import random

# Objective for this project is to build a simplified version of the classic game Battleship. 
# Students will draw a grid layout on a piece of paper and keep track of the positions they tried to attack and mark those locations according to 'hit' or 'miss' status. 
# The first student to successfully complete the game wins.

# Lesson Plan: 
# This code demonstrates key programming concepts like variables, lists, loops, conditional statements, and randomization. 
# The game we’re creating is a simplified version of Battleship where students can guess coordinates to find and "sink" a hidden ship.
# Below, I’ll explain what each block of code does so you can share these ideas with students.

# Setting up the game board and rules
# Here, we define some important variables to determine the size of the game board, the length of the ship, and how many guesses the player has.
grid_size = 10  # The board is a 5x5 grid.
ship_length = 5  # The ship takes up 3 consecutive spaces.
attempts = 35  # Players have 15 guesses to find and sink the ship.

# Placing the ship randomly on the board
# This block decides whether the ship will be placed horizontally or vertically, and then calculates its starting position.
ship_orientation = random.choice(["horizontal", "vertical"])  # Randomly choose the ship's orientation.

if ship_orientation == "horizontal":
    # If the ship is horizontal, we pick a random row and a starting column that ensures the ship fits on the grid.
    ship_row = random.randint(0, grid_size - 1)
    ship_col_start = random.randint(0, grid_size - ship_length)
    # Create a list of all the grid positions the ship occupies.
    ship_positions = [(ship_row, ship_col_start + i) for i in range(ship_length)]
else:
    # If the ship is vertical, we do the same but for a column and starting row.
    ship_col = random.randint(0, grid_size - 1)
    ship_row_start = random.randint(0, grid_size - ship_length)
    # Create a list of all the grid positions the ship occupies.
    ship_positions = [(ship_row_start + i, ship_col) for i in range(ship_length)]

# Introducing the game to the player
# We print instructions so the player knows how to play the game. This is an important part of making the program user-friendly.
print("Welcome to Battleship!")
print(f"The grid is {grid_size} x {grid_size}.")
print("Rows and Columns are numbered from 0 to {grid_size - 1}.")
print(f"You have {attempts} attempts to sink the ship!")
print("Guess a target area by entering the Row and Column numbers, e.g., '2 3'.")

# Keeping track of the player's progress
# The `hits` variable counts how many parts of the ship the player has hit.
hits = 0

# Starting the game loop
# This `while` loop keeps the game running until the player runs out of attempts or sinks the ship.
while attempts > 0:
    try:
        # Display the number of remaining attempts and hits so far.
        print(f"\nAttempts remaining: {attempts}")
        print(f"Hits: {hits}/{ship_length}")
        
        # Ask the player for their guess and process the input.
        guess = input("Enter your guess (row and column separated by a space): ").strip().split()
        if len(guess) != 2:
            print("Please enter two numbers separated by a space.")
            continue
        
        # Convert the input to integers representing the row and column guessed.
        row_guess, col_guess = int(guess[0]), int(guess[1])
        
        # Check if the guess is valid (within the bounds of the grid).
        if 0 <= row_guess < grid_size and 0 <= col_guess < grid_size:
            # Check if the guess is a hit.
            if (row_guess, col_guess) in ship_positions:
                print("🎯 Hit!")
                # Remove the hit part of the ship from the list of positions.
                ship_positions.remove((row_guess, col_guess))
                hits += 1  # Increase the hit count.
                # If the player hits all parts of the ship, they win.
                if hits == ship_length:
                    print("\n🚢 You sank the ship! Congratulations! 🏆")
                    break
            else:
                print("💦 Miss!")
        else:
            # If the guess is out of bounds, remind the player of the valid range.
            print(f"Please guess numbers between 0 and {grid_size - 1}.")
        
        # Reduce the number of remaining attempts by 1.
        attempts -= 1
    except ValueError:
        # Handle the case where the player's input can't be converted to integers.
        print("Invalid input. Please enter two numbers separated by a space.")

# Check if the player ran out of attempts without sinking the ship.
if attempts == 0 and hits < ship_length:
    print("\nYou ran out of attempts! The ship was at these positions:")
    print(ship_positions)