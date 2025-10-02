import random
import time

def number_guessing():
    high_score = {"easy": None, "medium": None, "difficult": None}

    while True:
        print("Welcome to the Number Guessing Game!\n")
        print("I'm thinking of a number between 1 and 100.\n")
        print("Please select the difficulty level:\n")
        print("1. Easy (10 chances)\n")
        print("2. Medium (5 chances)\n")
        print("3. Hard (3 chances)\n")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            chances = 10
            difficulty = "easy"
        elif choice == "2":
            chances = 5
            difficulty = "medium"
        elif choice == "3":
            chances = 3
            difficulty = "difficult"
        else:
            print("Invalid choice, please enter 1, 2, or 3.")
            continue

        number_to_guess = random.randint(1, 100)
        attempts = 0
        start_time = time.time()

        print(f"\nYou chose {difficulty} difficulty.")
        print(f"You have {chances} chances.")
        print("Type 'hint' if you want a hint (costs 1 attempt).\n")

        while chances > 0:
            guess = input("Enter a number: ")

            if guess.lower() == 'hint':
                chances -= 1
                print(f"Hint: The number is around {number_to_guess + random.choice([-10, 10])}")
                continue

            if not guess.isdigit():
                print("❌ Please enter an integer value.")
                continue

            guess = int(guess)
            attempts += 1
            chances -= 1

            if guess == number_to_guess:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)

                print(f"🎉 Congratulations! You guessed the correct number in {attempts} attempts.")
                print(f"⏱ Time taken: {time_taken} seconds")

                if high_score[difficulty] is None or attempts < high_score[difficulty]:
                    high_score[difficulty] = attempts
                    print(f"🏆 New high score for {difficulty}: {high_score[difficulty]} attempts!")
                break

            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

            print(f"Remaining chances: {chances}\n")

        else:
            print(f"💀 Game Over! The correct number was {number_to_guess}")

        print("\n📊 High Scores:")
        for level, score in high_score.items():
            if score is None:
                print(f"{level.capitalize()}: No score yet")
            else:
                print(f"{level.capitalize()}: {score} attempts")

        try_again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if try_again != "y":
            print("👋 Goodbye! Thank you for playing.")
            break

if __name__ == "__main__":
    number_guessing()