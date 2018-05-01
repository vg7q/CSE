class Room(object):
    def __init__(self, name, description, north, east, south, west, northwest, southwest, southeast, northest):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.northwest = northwest
        self.southwest = southwest
        self.southeast = southeast
        self.northeast = northest

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


SPAWN = 'your coming back from work from driving 3 days straight and you ran out of gas, you seen a abandon police ' \
        'station prison '
LIBRARY = 'the more you stay silent the more youll live, all you have to do is stay quiet'
HALLWAY = 'they knew you were here, they knew your sent, they know what your mind is going to do next'
SILENT = 'stay quiet around the nurses or they will se your fear'
CHURCH = 'don\'t open the box on the corner or you will be doomed even though theres a gun that has 8 rounds in it'
JUMP = 'they heard your foot steps in the silent room'
CHOICES = 'choose a rom and see what kind of weapons and armor to protect your self'
SCARE = '....'
BOX_CHOICES_1 = 'you found armor, you use and youll survive hits'
BOX_CHOICES_2 = 'you found ammo'
BOX_CHOICES_3 = 'you found nothing'
SILENT_ROOM = 'stay quiet if you want to live'
QUIZ_OR_FIZZ_1 = 'what can fly up slow but flies down fast'
QUIZ_OR_FIZZ_2 = 'what can glide but cant hide'
MIONIONS = 'take out the mionions if you want to live'
BOSS = 'kill the boss if you want to leave'


spawn = Room("spawn_room", SPAWN, 'library', '', '', '', '', '', '', '')
library = Room("Library", LIBRARY, '', 'hallway', '', '', '', '', '', '')
hallway = Room("HALLWAY", HALLWAY, '', 'silent', '', '', '', '', '', '')
silent = Room("SILENT", SILENT_ROOM, '', '', 'church', '', '', '', '', '')
church = Room("chruch", CHURCH, '', 'box_choices_1', 'jump', '', '', '', '', '')
jump = Room("jump", JUMP, 'church', '', '', '', '', '', '', '')
choices = Room("Choices", CHOICES, 'silent', '', 'scare', '', 'box_choice_3', '', 'box_choice_1', 'box_choice_2')
silent_room = Room("silent", SILENT_ROOM, 'quiz_or_fizz', '', 'choices', '', '', '', '', '',)
quiz_or_fizz = Room("quizz_or_fizz_1", QUIZ_OR_FIZZ_1, '', 'Quiz_or_fizz_2', 'Silent_room', '', '', '', '', '')
quizz_for_fizz = Room("quizz_or_fizz_2", QUIZ_OR_FIZZ_2, '', '', 'minions', '', '', '', '', '',)
minions = Room("minions", MIONIONS, 'quiz_or_fiz_2', '', 'boss', '', '', '', '', '')
boss = Room("boss", BOSS, 'minions', '', '', '', '', '', '', '')

current_node = spawn
directions = ['north', 'south', 'east', 'west', 'northwest', 'southwest', 'southeast', 'northeast']
short_directions = ['n', 's', 'e', 'w', 'nw', 'sw', 'se', 'ne']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("you cannot go this way")
    else:
        print("command not recognized")