import random

def main():
    print("🎲 Dice Roll Simulator")
    print("----------------------")
    print("Rolling two dice, three times...\n")
    
    # Loop to simulate 3 rolls
    for round_num in range(1, 4):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        
        print(f"Round {round_num}:")
        print(f"  Die 1 rolled: {die1}")
        print(f"  Die 2 rolled: {die2}")
        print(f"  Total: {die1 + die2}\n")

# Call the main function
if __name__ == '__main__':
    main()
