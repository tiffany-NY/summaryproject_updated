class Map:

    def __init__(self, size: int, xcoord: int, ycoord: int, location: str) -> None:
        self.size = size #size of map
        self.xcoord = xcoord #xcoord of coordinates of player
        self.ycoord = ycoord #ycoord of cordinates of player
        self.current_location = location #room the player is in

    def show_current_location(self) -> str:
        """
        Displays the name of the room Twilight is currently in
        """
        print(f'Your current location is {self.current_location}.')

    def set_current_location(self, location: str) -> None:
        """ 
        Updates the location Twilight to the room shes is currently in
        """
        self.current_location = location
        return self.current_location

    def display_map(self) -> str:
        """
        Displays the map
        """
            #x = 0    #x = 1
        map = [['room1', 'room2'], #y = 0
            ['room3','room4']] #y = 1

        print(map)

    def move_location(self) -> None:
        """
        Updates the coordiates of the player 
        """
        #grid of map
                #x = 0    #x = 1
        map = [['room1', 'room2'], #y = 0
               ['room3','room4']] #y = 1

        #control for movement
        if self.ycoord > 0:
            print('1 - North') #up

        if self.ycoord < len(map) - 1:
            print('2 - South') #down
        
        if self.xcoord < len(map[0]) - 1:
            print('3 - East') #right

        if self.xcoord > 0 :
            print('4 - West') #left

        #promps user for number representing the movements
        movement = input('Input a number for your next move: ')

        #up
        if movement == 1:
            if self.ycoord > 0:
                self.ycoord += 1

        #down
        elif movement == 2:
            if self.ycoord < len(map) - 1:
                self.ycoord -= 1

        #right
        elif movement == 3:
            if self.xcoord < len(map[0]) - 1:
                self.xcoord += 1
        
        #left
        else:
            if self.xcoord > 0:
                self.xcoord -= 1