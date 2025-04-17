import random

def main():
    print("🎲 Dice Roll Simulator")
    print("----------------------")

    # Roll two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    # Print the results
    print(f"Die 1 rolled: {die1}")
    print(f"Die 2 rolled: {die2}")
    print(f"Total: {total}")

# Call the main function
if __name__ == '__main__':
    main()
