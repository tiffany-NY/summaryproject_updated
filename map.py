        #x = 0    #x = 1   #x = 2
map = [['Hallway', 'Garden', 'Drawing Room'], #y = 0
        ['Kitchen','Tea Room', 'Study'],  #y = 1
        ['Throne Room', 'Chambers', 'Artillery'], #y = 2
        ['Dungeon', 'Crown Room', 'Ballroom'], #y = 3
        ['Stables', 'Gallery', 'Library']] #y = 4

details = {
    'Hallway': {
        'name': 'Hallway',
        'enemy': ['doofus1', 100, 5],
        'weapon': ['sword', 10, 0]
    },
    'Garden': {
        'name': 'Garden',
        'enemy': ['doofus2', 100, 7],
        'weapon': ['kaboom spell', 10, -5]
    },
    'Drawing Room': {
        'name': 'Drawing Room',
        'enemy': ['doofus3', 100, 7],
        'potion': ['Mrs scowers all purpose maggi mee', 'x2', '0', '0', 50]
    },
    'Kitchen': {
        'name': 'Kitchen',
        'enemy': ['doofus4', 100, 10],
        'potion': ['Wiggenweld juice', '+10', '0', '0', '50']
    },
    'Tea Room': {
        'name': 'Tea Room',
        'enemy': ['doofus5', 100, 10],
        'weapon': ['Pinkie spell', 20, -5]
    },
    'Study': {
        'name': 'Kitchen',
        'enemy': ['doofus6', 100, 13],
        'potion': ['Alicorn Elixer', '+20', '+10', '+10', '10']
    },
    'Throne Room': {
        'name': 'Throne Room',
        'enemy': ['Nightmare Moon', 250, 30]
    },
    'Chambers': {
        'name': 'Chambers',
        'enemy': ['doofus7', 100, 15],
        'weapon': ['Wobuffet Wall', 0, 0]
    },
    'Artillery': {
        'name': 'Artillery',
        'enemy': ['doofus8', 100, 15],
        'potion': ['Boosting Salve', '0', 'x2', '0', 30]
    },
    'Dungeon': {
        'name': 'Dungeon',
        'enemy': ['doofus9', 100, 18],
        'potion': ['Gigantamax Power', '0', '0', 'x2', 20]
    },
    'Crown Room': {
        'name': 'Crowd Room',
        'enemy': ['doofus10', 100, 12],
        'weapon': ['kaboom spell', 10, -5]
    },
    'Ballroom': {
        'name': 'Ballroom',
        'enemy': ['doofus11', 100, 14],
        'potion': ['Mrs scowers all purpose maggi mee', 'x2', '0', '0', 50]
    },
    'Stables': {
        'name': 'Stables',
        'enemy': ['doofus12', 100, 8],
        'weapon': ['Pinkie Spell', 20, -5]
    },
    'Gallery': {
        'name': 'Gallery',
        'enemy': ['doofus13', 100, 15],
        'potion': ['Kaboom Spell', 10, -5]
    },
    'Library': {
        'name': 'Library',
        'enemy': ['doofus14', 100, 8],
        'potion': ['Gigantamax Power', '0', '0', 'x2', 20]
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
        
        else:
            self.move_location()

        self.current_location = map[self.ycoord][self.xcoord]