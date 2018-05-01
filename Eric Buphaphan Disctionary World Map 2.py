world_map = {
    'SPAWN' : {
        'NAME': 'Spawn Room',
        'DESCRIPTION': 'your car ran out of gas there\'s an abandon police station/prison',
        'PATHS': {
            'NORTH':  'LIBRARYHOUSE',
        }
    },
    'LIBRARYHOUSE': {
        'NAME': 'Library',
        'DESCRIPTION': "Don't make a sound or they will hear you",
        'PATHS':  {
            'SOUTH':  'SPAWN',
            'EAST': 'HALL'
        }
    },
    'HALL': {
        'NAME': 'Hallway',
        'DESCRIPTION': "scratch",
        'PATHS': {
            'EAST': 'SILENT',
            'WEST': 'LIBRARYHOUSE'
        }
    },
    'SILENT': {
        'NAME': 'deadzone',
        'DESCRIPTION': "find or fight your way out",
        'PATHS': {
            'SOUTH': 'CHURCH',
            'WEST': 'HALL'
        }
    },
    'CHURCH':{
        'NAME': 'church',
        'DESCRIPTION': "Dont open the box",
        'PATHS': {
            'SOUTH': 'JUMP',
            'NORTH': 'SILENT',
            'EAST': 'CHOICES'
        }
    },
    'JUMP': {
        'NAME': 'jump scare',
        'DESCRIPTION':  "screach!",
        'PATHS': {
            'NORTH': 'CHURCH',
        }
    },
    'CHOICES': {
        'NAME': 'hall of choices',
        'DESCRIPTION': "choose a path for an item",
        'PATHS': {
            'EAST': 'BOX_CHOICE_2',
            'NORTHEAST': 'BOX_CHOICE_3',
            'SOUTHEAST': 'BOX_CHOICE_1',
            'NORTH': 'SILENT_ROOM',
            'SOUTH': 'SCARE'
        }
    },
    'SCARE': {
        'NAME': 'jump scare',
        'DESCRIPTION': "random loud noice",
        'PATHS': {
            'NORTH': "CHOICES",
        }
    },
    'BOX_CHOICE_1': {
        'NAME': 'room 1',
        'DESCRIPTION': "nothing",
        'PATHS': {
            'NORTHWEST': "CHOICES",
        }
    },
    'BOX_CHOICE_2': {
        'NAME': 'room 2',
        'DESCRIPTION': "nothing",
        'PATHS': {
            'WEST': "CHOICES",
        }
    },
    'BOX_CHOICE_3': {
        'NAME': 'room 3',
        'DESCRIPTION': "key",
        'PATHS': {
            'SOUTHWEST': "CHOICES",
        }
    },
    'SILENT_ROOM': {
        'NAME': 'run or hide',
        'DESCRIPTION': "shhh",
        'PATHS': {
            'NORTH': "QUIZ_OR_FIZZ",
            'SOUTH': "CHOICES"
        }
    },
    'QUIZ_OR_FIZZ': {
        'NAME': 'solve the question or solve your death',
        'DESCRIPTION': "solve my question, or solve your death, what can fly up slow but falls down fast?",
        'PATHS': {
            'SOUTH': "SILENT_ROOM",
            'EAST': "QUIZ_OR_FIZZ_2"
        }
    },
    'QUIZ_OR_FIZZ_2': {
        'NAME': 'solve or fall!',
        'DESCRIPTION': "solve or fall, what can glide but cant hide?",
        'PATHS': {
            'SOUTH': "MINIONS",
            'WEST': "QUIZ_OR_FIZZ"
        }
    },
    'MINIONS': {
        'NAME': 'Exit',
        'DESCRIPTION': "defeat the minions",
        'PATHS': {
            'SOUTH': "BOSS",
            'NORTH': "QUIZ_OR_FIZZ_2"
        }
    },
    'BOSS': {
        'NAME': 'Boss_Room',
        'DESCRIPTION': "you thought it was over?",
        'PATHS': {
            'NORTH': "MINIONS"
        }
    },
}
current_node = world_map['SPAWN']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTHWEST', 'NORTHEAST', 'SOUTHEAST', 'SOUTHWEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
