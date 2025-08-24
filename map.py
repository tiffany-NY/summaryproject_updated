from menu import menu
        #x = 0    #x = 1   #x = 2
map = [['hallway', 'kitchen', 'garden'], #y = 0
        ['study room','tea room', 'drawing room'],  #y = 1
        ['study room', 'a', 'artillery'], #y = 2
        ['b', 'c', 'd'], #y = 3
        ['chambers', 'crown room', 'throne room']] #y = 4

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
        print(f'Your current location is {self.current_location}.')

    def display_map(self) -> str:
        """
        Displays the map
        """
        for row in self.map:
            print(row)

    def move_location(self) -> None:
        """
        Updates the coordiates of the player 
        """

        #control for movement
        if self.ycoord > 0:
            print('1 - North') #up

        if self.ycoord < len(map) - 1:
            print('2 - South') #down
        
        if self.xcoord < len(map[0]) - 1:
            print('3 - East') #right

        if self.xcoord > 0 :
            print('4 - West') #left

        print('5 - Menu')

        #promps user for number representing the movements
        movement = int(input('Input a number for your next move: '))

        #up
        if movement == 1:
            if self.ycoord > 0:
                self.ycoord -= 1

        #down
        elif movement == 2:
            if self.ycoord < len(map) - 1:
                self.ycoord += 1

        #right
        elif movement == 3:
            if self.xcoord < len(map[0]) - 1:
                self.xcoord += 1
        
        #left
        elif movement == 4:
            if self.xcoord > 0:
                self.xcoord -= 1
        
        elif movement == 5:
            menu()

        else:
            self.move_location()

        self.current_location = map[self.ycoord][self.xcoord]    

castle = Map(map, 0, 0)