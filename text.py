import os
from typing import Any, TypeVar

I = TypeVar("I", bound=Any)

GAME_TITLE = "\t𐙚⋆˚✿˖° Castle of the Two Sisters 𐙚⋆˚✿˖°"

BACKSTORY = """
Awaken, O wanderer, to the words etched in the stones of time.
When the world of Equestria lies fractured, and harmony is but a fading memory, the shadow of Nightmare Moon shall descend upon all.
Once she was Princess Luna, guardian of dreams, but envy and sorrow twisted her into darkness unending.
Yet the stars foretell: From the ashes shall rise a hero. 
One who dares to tread through ruins and forgotten halls.
One who seeks the Elements of Harmony, scattered and hidden by fate.
One who will brave monsters, traps, and secrets untold.

Know this, chosen one: Only by uniting the six Elements of Harmony—Loyalty, Honesty, Generosity, Kindness, Laughter, and Magic—shall Nightmare Moon be cast down,and Princess Luna restored to her true self.
Should you falter, the Elements shall fall from your grasp, and if Nightmare Moon seizes them all, eternal night shall claim Equestria.
"""

RULES = """
Your path begins in the vast castle, within lies the Garden, Kitchen, Tea Room, Drawing Room, Study, Chambers, Artillery, Crown Room, and Dungeon.
At the end, the Throne Room, where Nightmare Moon herself awaits.
Each chamber holds secrets and dangers so tread carefully, for every step binds your destiny.

In the castle rooms dwell mind-controlled ponies who have fallen prey to Nightmare Moon phonies. 
Each battle flows in turns, as in the old duels of balance: you strike back and forth until one falls.
Your choices in combat are these:
* Strike with weapon or spell.
* Shield against oncoming blows.
* Conjure Spells of great power, though some drain your life.
* Use Relics such as potions or healing elixirs.
Remember: every choice carves the story of your soul.
"""

ITEM_INFO = """
Potions & Elixirs
* Mrs Scower’s All-Purpose Maggi Mee More: Restores ×2 health.
* Wiggenweld Elixir: +10 health.
* Alicorn Brew: +20 health.
* Boosting Salve: +20 max health.
* Rejuvenation Juice: +10 base power.
Weapons & Spells
* Sword: +10 power.
* Grit Gourd Spell: +10 power, but drains -5 health.
* Pinkie Pulse: +20 power, but drains -10 health.
* Shielding Spell (×2 uses): Block all enemy damage for one turn.
These relics may tip the scales of light or shadow—wield them with wisdom.

Should you gather the six Elements and triumph in the Throne Room, the prophecy is fulfilled:Nightmare Moon falls, Princess Luna is reborn,and harmony is restored to Equestria.


Should your health fail, the darkness claims you,and the Elements scatter from your hooves.If Nightmare Moon seizes them first,Equestria is lost to eternal night.
Yet as the moon wanes and waxes,so too may destiny grant you another chance.

So it is written. So it awaits.
Step forth, brave warrior, for the Castle of the Two Sisters opens only to those who dare to claim their fate.
"""

ATTACK_PROMPT = "> click enter to attack "

FIGHT_WON = "yipee you won!"

FIGHT_LOST = "oh no you died"

VICTORY = """
Congratulations!!! You have collected all the elements of harmony yippee!!!
With all the elements, you restored the magic of friendship in Equastria and purified Nightmare Moon back to Princess Luna!
And with that your mission has ended and Equastria is safe! till next time!
THANKS FOR PLAYING!!!
"""

DIVIDER = "𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def linebreak():
    print("\n")


def print_lines(
        *lines: str,
        continue_prompt: str | None = None,
) -> None:
    """Prints each line in the given list of lines.

    If continue_prompt is given, prompts the user to press a key to continue
    after printing all lines.
    """
    for line in lines:
        print(line)
    if continue_prompt:
        input(continue_prompt)


def alert_element_found(element: str) -> None:
    """Alerts user that they have found an element."""
    print(f"congratulations! u found the {element}")


def alert_enemy(enemy: str) -> None:
    """Alerts user that they have encountered an enemy."""
    print(f"oh no {enemy} has appeared")


def alert_no_loot(enemy: str) -> None:
    """Alerts user that the enemy has no loot."""
    print(f"awh man {enemy} did not drop anything :(")

def prompt_loot(enemy: str) -> None:
    """Prompts user to press a key to pick up an enemy's dropped item."""
    print(DIVIDER)
    print(f"oh look! {enemy} dropped something!")
    input("> click enter to see what it is! ")


def prompt_inline_choice(
        prompt: str,
        options: list[str],
        prefix: str = "",
        separator: str = "/",
) -> str:
    """ Prompts the user to choose from a list of options inline and returns the chosen option """
    if len(options) <= 1:
        raise ValueError("At least two options are required.")
    if len(options) > 3:
        raise ValueError("A maximum of three options are supported.")
    options_str = separator.join(options)
    while True:
        choice = input(f"{prefix}{prompt} ({options_str}): ")
        if choice in options:
            return choice
        else:
            print(f"Invalid choice.")


def prompt_numbered_choice(
        preamble: str,
        options: list[I],
        prompt: str = "Enter the number of your choice: ",
) -> I:
    """ Prompts the user to choose from a list of options by number and returns the chosen option """
    if len(options) <= 1:
        raise ValueError("At least two options are required.")
    print(preamble)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {str(option)}")
    while True:
        choice = input(prompt)
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")