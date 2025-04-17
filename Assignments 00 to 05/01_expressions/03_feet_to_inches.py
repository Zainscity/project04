def main():
    # Prompt the user to enter a length in feet
    feet = float(input("Enter length in feet: "))

    # Convert feet to inches (1 foot = 12 inches)
    inches = feet * 12

    # Print the result
    print(f"{feet} feet is equal to {inches} inches.")

# Call the main function
if __name__ == '__main__':
    main()
