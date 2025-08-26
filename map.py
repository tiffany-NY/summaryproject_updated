from menu import menu
        #x = 0    #x = 1   #x = 2
map = [['Hallway', 'Garden', 'Drawing Room'], #y = 0
        ['Kitchen','Tea Room', 'Study'],  #y = 1
        ['Throne Room', 'Chambers', 'Artillery'], #y = 2
        ['Dungeon', 'Crown Room', 'Ballroom'], #y = 3
        ['Stables', 'Gallery', 'Library']] #y = 4

details = {
    'Hallway': {
        'name': 'Hallway',
        'enemy': ['doofus1', 50, 3],
        'item': {'weapon': {"name": "sword", "damage": 10, "health": 0},
                 'potion': {"name": "Mrs scowers all purpose maggi mee", "health": "x2", "max_health": "0", "default_power": "0"}
        }
    },
    'Garden': {
        'name': 'Garden',
        'enemy': ['doofus2', 50, 3],
        'item': {'weapon': {"name": "kaboom spell", "damage": 10, "health": -5}}
    },
    'Drawing Room': {
        'name': 'Drawing Room',
        'enemy': ['doofus3', 100, 5],
        'item': {'elements': "element of laughter",
                'potion': {"name": "Alicorn elixer", "health": "+20", "max_health": "+10", "default_power": "+10"}}
    },
    'Kitchen': {
        'name': 'Kitchen',
        'enemy': ['doofus4', 50, 3],
        'item': {'potion': {"name": "Mrs scowers all purpose maggi mee", "health": "x2", "max_health": "0", "default_power": "0"}}
    },
    'Tea Room': {
        'name': 'Tea Room',
        'enemy': ['doofus5', 100, 5],
        'item': {'elements': "element of honesty"}
    },
    'Study': {
        'name': 'Study',
        'enemy': ['doofus6', 50, 3],
        'item': {'potion': {"name": "Alicorn elixer", "health": "+20", "max_health": "+10", "default_power": "+10"}}
    },
    'Throne Room': {
        'name': 'Throne Room',
        'enemy': ['Nightmare Moon', 250, 30],
        'item': {'elements': "element of magic"}
    },
    'Chambers': {
        'name': 'Chambers',
        'enemy': ['doofus7', 50, 5],
        'item': {'weapon': {"name": "wobuffet wall", "damage": 0, "health": 0}}
    },
    'Artillery': {
        'name': 'Artillery',
        'enemy': ['doofus8', 100, 7],
        'item': {'elements': "element of generosity"}
    },
    'Dungeon': {
        'name': 'Dungeon',
        'enemy': ['doofus9', 50, 3],
        'item': {'potion': {"name": "Gigantamax powder", "health": "0", "max_health": "0", "default_power": "x2"}}
    },
    'Crown Room': {
        'name': 'Crowd Room',
        'enemy': ['doofus10', 50, 5],
        'item': {'potion': {"name": "Boosting salve", "health": "0", "max_health": "x2", "default_power": "0"}}
    },
    'Ballroom': {
        'name': 'Ballroom',
        'enemy': ['doofus11', 50, 7],
        'item': {'potion': {"name": "Mrs scowers all purpose maggi mee", "health": "x2", "max_health": "0", "default_power": "0"}}
    },
    'Stables': {
        'name': 'Stables',
        'enemy': ['doofus12', 50, 3],
        'item': {'weapon': {"name": "pinkie spell", "damage": 20, "health":-5}}
    },
    'Gallery': {
        'name': 'Gallery',
        'enemy': ['doofus13', 100, 5],
        'item': {'elements': "element of loyalty"}
    },
    'Library': {
        'name': 'Library',
        'enemy': ['doofus14', 100, 7],
        'item': {'elements': "element of kindness"}
    }
}

        
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
        return f'Your current location is {self.current_location}.'

    def display_map(self) -> str:
        """
        Displays the map
        """
        return self.map

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
