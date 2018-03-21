world_map = {
    'WESTHOUSE': {
        'NAME': 'West of house',
        'DESCRIPTION': 'You are west of a white house' ,
        'PATHS': {
            'NORTH':  'NORTHHOUSE',
            'SOUTH':  'SOUTHHOUSE'
        }
    },
    'NORTHHOUSE' : {
        'NAME':   'North of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS':  {
            'WEST': 'WESTHOUSE'

        }
    }
}
current_node = world_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    print(current_node)
    command = input ('>_')
    if command == 'quit':
        quit (0)
    if command in directions:
        try:
            name_of_node = current_node ['PATHS'][command]
            print(name_of_node)
        except KeyError:
            print("you cannot go this way")
    else:
        print("command not recognized")
