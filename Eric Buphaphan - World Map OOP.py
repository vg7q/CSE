class Room(object):
    def __init__(self, name, north, east, south, west):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals() [getattr(self, direction)]


hdum = Room ()


current_node = hdum
directions = ['north', 'south', 'east', 'west']

while True:
    print(current_node['name']) # change
    print(current_node['description']) # change
    print(current_node)
    command = input ('>_')
    if command == 'quit':
        quit (0)
    if command in directions:
        try:
            # change
            name_of_node = current_node ['PATHS'][command]
            print(name_of_node)
        except KeyError:
            print("you cannot go this way")
    else:
        print("command not recognized")