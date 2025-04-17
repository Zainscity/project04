def main():
    # Ask the user for a number
    number = float(input("Type a number to see its square: "))

    # Calculate the square
    square = number * number

    # Print the result
    print(str(number) + " squared is " + str(square))

# Call the main function
if __name__ == '__main__':
    main()
