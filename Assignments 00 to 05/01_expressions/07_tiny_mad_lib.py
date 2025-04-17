def main():
    print("📝 Welcome to Python Mad Libs!")
    print("Fill in the blanks to create your own silly story!\n")

    # Collect words from the user
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (present tense): ")
    adverb = input("Enter an adverb (e.g. quickly, slowly): ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    emotion = input("Enter an emotion: ")

    # Build the Mad Libs story
    story = f"""
    One {adjective} day, I went to the {place} with my pet {animal}.
    Suddenly, my {animal} started to {verb} {adverb} in front of everyone!
    I was so {emotion}, I dropped my {food} all over the ground.
    Everyone laughed and said, "That was the best {noun} we've ever seen!"
    """

    # Print the final story
    print("\n🎉 Here's your story:")
    print(story.strip())

# Run the program
if __name__ == '__main__':
    main()
