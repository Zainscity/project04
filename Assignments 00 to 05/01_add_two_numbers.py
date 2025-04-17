
def main():
    print("This program adds two numbers.")

    # Prompt and read the first number
    num1 = int(input("Enter first number: "))

    # Prompt and read the second number
    num2 = int(input("Enter second number: "))

    # Calculate the total
    total = num1 + num2

    # Display the result
    print("The total is " + str(total) + ".")

# Required line to call the main function
if __name__ == '__main__':
    main()
