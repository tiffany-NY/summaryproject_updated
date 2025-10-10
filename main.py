from . import castle, menu, text

HP = 100
power = 5
name = ""


def main() -> None:
    game = castle.Game()
    menu.show_intro()
    menu.main_menu_prompt()

    while not game.is_game_over():
        menu.save_game()
        input("> click enter to move on ")
        text.clear_screen()
        movement_options = game.get_movement_options()
        movement_options.append("Exit Game")
        choice = text.prompt_numbered_choice(
            preamble=f"You are now in the {game.get_current_room().name}",
            options=movement_options
        )
        if choice == "Exit Game":
            print("thanks for playing!!")
            quit()
        game.move(choice)
        game.visit_current_room()
    if game.is_player_victorious():
        print(text.DIVIDER)
        print(text.VICTORY)
        quit() 

#left: data validation for all inputs and actually implement save feature properly

if __name__ == "__main__":
    main()