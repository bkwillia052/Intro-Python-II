# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.room = room
        self.inventory = []
    def move(self, newroom):
        if newroom == None:
            print('\n \n INVALID MOVE: You cannot move here.')
        else:
            self.room = newroom 
