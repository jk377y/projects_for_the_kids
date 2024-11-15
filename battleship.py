import random

# Game setup
grid_size = 5
ship_length = 3
attempts = 15

# Randomly place a horizontal or vertical ship
ship_orientation = random.choice(["horizontal", "vertical"])
if ship_orientation == "horizontal":
    ship_row = random.randint(0, grid_size - 1)
    ship_col_start = random.randint(0, grid_size - ship_length)
    ship_positions = [(ship_row, ship_col_start + i) for i in range(ship_length)]
else:
    ship_col = random.randint(0, grid_size - 1)
    ship_row_start = random.randint(0, grid_size - ship_length)
    ship_positions = [(ship_row_start + i, ship_col) for i in range(ship_length)]

# Print instructions
print("Welcome to Battleship!")
print(f"The grid is {grid_size}x{grid_size}. Rows and columns are numbered from 0 to {grid_size - 1}.")
print(f"You have {attempts} attempts to sink the ship!")
print("Guess by entering the row and column numbers, e.g., '2 3'.")

# Initialize hit tracking
hits = 0

# Game loop
while attempts > 0:
    try:
        # Show remaining attempts and hits
        print(f"\nAttempts remaining: {attempts}")
        print(f"Hits: {hits}/{ship_length}")
        
        # Get player's guess
        guess = input("Enter your guess (row and column separated by a space): ").strip().split()
        if len(guess) != 2:
            print("Please enter two numbers separated by a space.")
            continue
        
        row_guess, col_guess = int(guess[0]), int(guess[1])
        
        # Check if the guess is within bounds
        if 0 <= row_guess < grid_size and 0 <= col_guess < grid_size:
            # Check if it's a hit
            if (row_guess, col_guess) in ship_positions:
                print("🎯 Hit!")
                ship_positions.remove((row_guess, col_guess))  # Remove hit part of the ship
                hits += 1
                if hits == ship_length:
                    print("\n🚢 You sank the ship! Congratulations! 🏆")
                    break
            else:
                print("💦 Miss!")
        else:
            print(f"Please guess numbers between 0 and {grid_size - 1}.")
        
        attempts -= 1  # Reduce remaining attempts
    except ValueError:
        print("Invalid input. Please enter two numbers separated by a space.")

# If the player runs out of attempts
if attempts == 0 and hits < ship_length:
    print("\nYou ran out of attempts! The ship was at these positions:")
    print(ship_positions)