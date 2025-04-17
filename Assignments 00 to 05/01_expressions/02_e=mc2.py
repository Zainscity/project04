def main():
    # Define the speed of light constant
    C = 299_792_458  # meters per second

    while True:
        # Prompt the user for input
        user_input = input("Enter kilos of mass (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        try:
            mass = float(user_input)

            # Calculate energy using E = m * c^2
            energy = mass * C**2

            # Output results
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"\n{energy} joules of energy!\n")
        except ValueError:
            print("Please enter a valid number for mass or 'q' to quit.\n")

# Call the main function
if __name__ == '__main__':
    main()
