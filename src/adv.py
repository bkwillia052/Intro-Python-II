from room import Room
from player import Player
import textwrap
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].add_item(Item("Medallion", "A golden & gemstone medallion"))
room['foyer'].add_item(Item("Medallion", "A golden & gemstone medallion"))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player(room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    room = p.room
    items = room.item_list 

    print('=== \n')
    print(f"Your presence now graces the {room.name}. \n  {room.description}")
    
    if items:
        print(f"There are items here!: {items}")

    
        
    action = input("\n Which direction will you move? (North|South|East|West): \n").lower().split(" ")
    

    if len(action) == 1:
        action = action[0]
        if action == 'q':
            break
        elif action == 'north':
            p.move(p.room.n_to)
        elif action == 'south':
            p.move(p.room.s_to)
        elif action == 'east':
            p.move(p.room.e_to)
        elif action == 'west':
            p.move(p.room.w_to)
        elif action == 'i' or action == 'inventory':
            p.list_inventory()
    else:
        
        act = action[0]
        item = action[1]
        if act == 'get' or act == "take":
            p.get_item(item)
        elif act == 'drop':
            p.drop_item(item)




#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
