from character import Character
import data

import character
import items
import text

NORTH = "North"
SOUTH = "South"
EAST = "East"
WEST = "West"

THRONE_ROOM = "Throne Room"
ELEMENTS_NEEDED = 6

location_data = data.load_game_data()['locations']
map_data = data.load_map_data()

details = location_data


def create_room(name: str):
    """ Creates a room object from the given name and data dictionary """
    if name not in location_data:
        raise ValueError(f"Room {name!r} does not exist.")
    data = location_data[name]
    return Room(name, data['enemy'], data['items'])


class Room:
    """ Represents a room in the game."""

    def __init__(self, name: str, enemy: str, items: list[str]) -> None:
        self.name = name
        self.enemy = enemy
        self.items = items


class Map:
    def __init__(self, data: list[list[str]]) -> None:
        self.map: list[list[Room]] = []
        for row in data:
            map_row = []
            for name in row:
                room = create_room(name)
                map_row.append(room)
            self.map.append(map_row)

    def display_map(self) -> str:
        """
        Displays the map
        """
        rows = []
        for row in self.map:
            names = [room.name for room in row]
            row_string = ' '.join(names)
            rows.append(row_string)
        map_representation = '\n'.join(rows)
        print(map_representation)
        return map_representation
    
    def get_room_at_coordinates(self, x: int, y: int) -> Room:
        """ Returns the room at the given coordinates (x, y). """
        if not self.is_valid_coordinate(x, y):
            raise ValueError(f"Coordinates ({x}, {y}) are out of bounds.")
        return self.map[y][x]

    def get_movement_options(self, x: int, y: int) -> list[str]:
        """ Returns a list of valid movement options from the current position
        (x, y).
        """
        options = []
        if self.is_valid_coordinate(x, y - 1):
            options.append(NORTH)
        if self.is_valid_coordinate(x, y + 1):
            options.append(SOUTH)
        if self.is_valid_coordinate(x + 1, y):
            options.append(EAST)
        if self.is_valid_coordinate(x - 1, y):
            options.append(WEST)
        return options

    def is_valid_coordinate(self, x: int, y: int) -> bool:
        """ Check if the given coordinates are within the map boundaries """
        return (
            0 <= x < len(self.map[0])
            and 0 <= y < len(self.map)
        )


class Game:
    """ Represents the game state."""

    def __init__(self):
        self.castle = Map(map_data)
        self.current_location: tuple[int, int] = (0, 0)
        self.player = character.create_player()
        self.throne_room_locked = True

    def get_current_room(self) -> Room:
        """ Returns the current room the player is in. """
        x, y = self.current_location
        return self.castle.get_room_at_coordinates(x, y)

    def get_movement_options(self) -> list[str]:
        """ Get valid movement options from the current location."""
        x, y = self.current_location
        return self.castle.get_movement_options(x, y)
    
    def is_game_over(self) -> bool:
        """ Check if the game is over (player defeated or victorious)."""
        return not self.player.is_alive() or self.is_player_victorious()

    def is_player_victorious(self) -> bool:
        """ Check if the player has collected all elements to win."""
        return self.player.inventory.count_elements() == ELEMENTS_NEEDED

    def show_current_location(self) -> None:
        """ Displays the current location of the player."""
        x, y = self.current_location
        room = self.castle.get_room_at_coordinates(x, y)
        print(f"You are now in the {room.name}.")
    
    def move(self, direction: str) -> None:
        """ Move the player in the specified direction if possible."""
        x, y = self.current_location
        if direction == NORTH and self.castle.is_valid_coordinate(x, y - 1):
            next_coordinate = (x, y - 1)
        elif direction == SOUTH and self.castle.is_valid_coordinate(x, y + 1):
            next_coordinate = (x, y + 1)
        elif direction == EAST and self.castle.is_valid_coordinate(x + 1, y):
            next_coordinate = (x + 1, y)
        elif direction == WEST and self.castle.is_valid_coordinate(x - 1, y):
            next_coordinate = (x - 1, y)
        else:
            print("You can't move in that direction.")
            return
        x, y = next_coordinate
        next_room = self.castle.get_room_at_coordinates(x, y)
        if self.throne_room_locked and next_room.name == THRONE_ROOM:
            print(f"You can't move {direction.lower()}. It's locked!")
            return
        self.current_location = next_coordinate

    def pre_battle(self) -> None:
        """Displays the stats and inventory of Twilight and
        prompts user to equip weapons or drink potions
        """
        print(text.DIVIDER)
        self.player.display_stats()
        print(text.DIVIDER)
        if not self.player.inventory.is_empty():
            self.player.display_inventory()
            print(text.DIVIDER)
            choice = text.prompt_inline_choice(
                prompt="Would you like to equip a weapon or drink a potion before starting your battle?",
                options=["yes", "no"],
                prefix="> "
            )
            while choice != "cancel":
                text.clear_screen()
                self.player.display_inventory()
                print(text.DIVIDER)
                options = self.player.inventory.list_items()
                options.append("cancel")
                choice = text.prompt_numbered_choice(
                    preamble="What would you like to use?",
                    options=options,
                )
                if choice != 'cancel':
                    self.player.use_item(choice)
                text.clear_screen()
                self.player.display_stats()
                print(text.DIVIDER)
            self.player.display_inventory()

    def battle(self, enemy: Character) -> bool:
        """Displays and updates stats and health of Twilight before the battle starts and after each attack and 
        Prompts user to attack
        """
        text.clear_screen()
        print(text.DIVIDER)
        self.player.display_stats()
        enemy.display_stats()
        print(text.DIVIDER)
        self.player.attack(enemy)
        enemy.attack(self.player)

        print(text.DIVIDER)
        self.player.health_bar.draw()
        enemy.health_bar.draw()
        print(text.DIVIDER)

        if self.player.is_alive() and enemy.is_alive():
            input(text.ATTACK_PROMPT)
            return True
        else:
            if self.player.is_alive():
                text.clear_screen()
                print(text.FIGHT_WON)
            
            else:
                text.clear_screen()
                print(text.FIGHT_LOST)
            return False

    def post_battle(self, enemy: Character) -> None:
        """Prompts user to pick up items (potions, elements and weapons) dropped by
        the enemy after a battle.
        If input == 'yes', updates and displays inventory, if input == 'no',
        continue the game.
        """
        current_room = self.castle.get_room_at_coordinates(
            *self.current_location
        )
        if not current_room.items:
            text.alert_no_loot(enemy.name)
            return
        text.prompt_loot(enemy.name)
        for item_name in current_room.items:
            item = items.create_item(item_name)
            print(text.DIVIDER)
            item.display_stats()
            item_type = type(item).__name__.lower()
            item_prompt = f"do u wanna pick up the {item_type}?"
            if isinstance(item, items.Element):
                print(text.alert_element_found(item.name))
                item_prompt += " (hint: u need it to win!!!!)"
            choice = text.prompt_inline_choice(
                prompt=item_prompt,
                options=["yes", "no"],
                prefix="> "
            )
            if choice == "yes":
                self.player.pick_up(item)

        print(text.DIVIDER)
        self.player.display_inventory()
        print(text.DIVIDER)
        input("> click enter to continue! ")
        text.clear_screen()
        print("you can continue to move around the map!")

    def visit_current_room(self) -> None:
        """Displays current location
        Define stats of enemy
        Conducts battle
        """
        self.show_current_location()
        current_room = self.castle.get_room_at_coordinates(*self.current_location)
        enemy = character.create_enemy(current_room.enemy)
        text.alert_enemy(enemy.name)
        self.pre_battle()
        input("> press enter to start your battle ")
        battling = True
        while battling:
            battling = self.battle(enemy)
        if self.player.is_alive():
            self.post_battle(enemy)