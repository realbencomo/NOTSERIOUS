import random

def game_instruction():
    print("""Sweardle is a dirty version of the popular game Wordle by Josh Wardle. 
It follows the same rules as basic Wordle with a catch: the word will always be a dirty word. 
You have six attempts. Your Progress Guide "✔❌❌✔➕":
✔ - Correct letter in the correct position
➕ - Letter is in the word but in the wrong position
❌ - Letter is not in the word
    """)

def check_word():
    swear_words = [
    "bitch", "pussy", "dicks", "prick", "shite", "sluts", "twats", "cunts",
    "boobs", "balls", "wanks", "farts", "dildo", "hells", "boner", "whore",
    "skank", "jerks", "basts", "nutsy", "douch", "fanny", "wangs", "damns",
    "arsey", "shags", "spunk", "milfs", "cocks", "randy", "sodom", "slags",
    "moobs", "craps", "nutsy", "porns", "pikey", "queef", "dykes", "titty",
    "tards", "gspot", "kinky", "balls", "dicks", "hooch", "boink",
    "poofs", "crack", "whoop", "spazz", "nipsy", "prang", "rapey", "felch"
]

    hidden_word = random.choice(swear_words)
    attempt = 6

    while attempt > 0:
        guess = input("Guess the 5-letter dirty word: ").lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        if guess not in swear_words:
            print("That's not on the naughty list! Try again.")
            continue

        if guess == hidden_word:
            print("You guessed the word correctly! WIN 🕺🕺🕺")
            break
        else:
            feedback = ""
            for i in range(5):
                if guess[i] == hidden_word[i]:
                    feedback += "✔"
                elif guess[i] in hidden_word:
                    feedback += "➕"
                else:
                    feedback += "❌"
            print(f"{guess.upper()} -> {feedback}")
            attempt -= 1
            print(f"You have {attempt} attempt(s) left.\n")

    if attempt == 0:
        print(f"Game over! The word was: {hidden_word.upper()}")


game_instruction()
check_word()
