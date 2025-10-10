from character import Character, Higherup, twilight
import data
from menu import menu


location_data = data.load_game_data()['locations']
map = data.load_map_data()

details = location_data


def unlock():
    if twilight.own_inventory.element_count >= 5:
        return True
    return False
        
class Map:
    def __init__(self, map, xcoord: int, ycoord: int) -> None:
        self.map = map
        self.xcoord = xcoord #xcoord of coordinates of player
        self.ycoord = ycoord #ycoord of cordinates of player
        self.current_location = map[self.ycoord][self.xcoord] #room the player is in

    def show_current_location(self) -> str:
        """
        Displays the name of the room Twilight is currently in
        """
        location_message = f'Your current location is {self.current_location}.'
        print(location_message)
        return location_message

    def display_map(self) -> str:
        """
        Displays the map
        """
        map_representation = '\n'.join([' '.join(row) for row in self.map])
        print(map_representation)
        return map_representation

    def move_location(self) -> None:
        """
        Updates the coordiates of the player, locks throne room until unlocked
        """
        print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
        self.show_current_location()
        #control for movement

        if unlock() == False:
            if self.current_location == map[3][0]:
                print("## You can't move north! its locked!!")
            else:
                if self.ycoord > 0:
                    print('1 - North') #up

            if self.current_location == map[1][0]:
                print("## You can't move south! its locked!!")
            else:
                if self.ycoord < len(map) - 1:
                    print('2 - South') #down

            if self.xcoord < len(map[0]) - 1:
                print('3 - East') #right

            if self.current_location == map[2][1]:
                print("## You can't move west! its locked!!")
            else:
                if self.xcoord > 0:
                    print('4 - West') #left

            print('5 - Menu')

        else:
            if self.ycoord > 0:
                print('1 - North') #up
            if self.ycoord < len(map) - 1:
                print('2 - South') #down
            if self.xcoord < len(map[0]) - 1:
                print('3 - East') #right
            if self.xcoord > 0 :
                print('4 - West') #left
            print('5 - Menu')
        
        movement = int(input('> enter a number for your next move: '))
        if movement == 1:
            if self.ycoord > 0:
                self.ycoord -= 1
        elif movement == 2:
            if self.ycoord < len(map) - 1:
                self.ycoord += 1
        elif movement == 3:
            if self.xcoord < len(map[0]) - 1:
                self.xcoord += 1
        elif movement == 4:
            if self.xcoord > 0:
                self.xcoord -= 1
        elif movement == 5:
            menu()
        else:
            self.move_location()
            
        self.current_location = map[self.ycoord][self.xcoord] 

castle = Map(map, 0, 0)
