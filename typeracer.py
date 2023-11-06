import time


def type_racer(source_text, time_limit=60):
    print("Welcome to Type Racer!")
    print("Type the following text as fast as you can:")
    print(source_text)
    input("Press Enter to start...")

    start_time = time.time()
    player_input = input("Type here: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    total_characters = len(source_text)
    correct_characters = sum(a == b for a, b in zip(source_text, player_input))

    typing_speed = (correct_characters / 5) / (
        elapsed_time / 60
    )  # Assuming an average word length of 5 characters
    accuracy = (correct_characters / total_characters) * 100

    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Typing speed: {typing_speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Total errors: {total_characters - correct_characters}")


if __name__ == "__main__":
    source_text = "This is a simple Type Racer game. Test your typing skills!"
    type_racer(source_text)
