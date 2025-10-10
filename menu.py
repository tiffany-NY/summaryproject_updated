import os

import text

HP = 100
power = 5
name = ""

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def save_game():
    """
    saves the file in the txt
    """
    try:
        with open("load.txt", "w") as file:
            file.write(f"{name}\n{HP}\n{power}\n")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game():
    """
    load the game data from the txt
    """
    global name, HP, power
    try:
        with open("load.txt", "r") as file:
            loaded = file.readlines()
            name = loaded[0].strip()
            HP = int(loaded[1].strip())
            power = int(loaded[2].strip())
        return True
    except FileNotFoundError:
        print("No saved game found.")
        return False
    except Exception as e:
        print(f"Error loading game: {e}")
        return False

def show_intro():
    """
    introduction of game
    """
    text.print_lines(
        text.DIVIDER,
        text.GAME_TITLE,
        text.DIVIDER,
        text.BACKSTORY,
        text.DIVIDER,
        continue_prompt="> click enter to move on "
    )


def main_menu_prompt() -> None:
    """
    the menu panel in which player can choose to create a new game, load previous game, read th rules or quit the game
    """
    while True:
        text.clear_screen()
        choice = text.prompt_numbered_choice(
            preamble="",
            options=[
                "New Game",
                "Load Previous Game",
                "Rules",
                "Quit"
            ],
            prompt="> "
        )        
        if choice == "New Game":
            text.clear_screen()
            name = input("> what's your name: ")
            print(f"Welcome, {name}!")
            return

        elif choice == "Load Previous Game":
            if load_game():
                text.clear_screen()
                print(f"Welcome back, {name}!!")
                return
            else:
                input("> click enter to return to menu...")

        elif choice == "Rules":
            text.clear_screen()
            print(text.RULES)
            text.linebreak()
            input("> click enter to return to menu...")
            return

        elif choice == "Quit":
            quit()