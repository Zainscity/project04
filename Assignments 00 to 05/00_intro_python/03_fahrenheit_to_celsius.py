def main():
    # Ask the user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display the result
    print("Temperature: " + str(fahrenheit) + "F = " + str(celsius) + "C")

# Call the main function
if __name__ == '__main__':
    main()
