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

    def get_item(self, item):
        newItem = self.room.remove_item(item)
        self.inventory.append(newItem)
        newItem.on_take()

    def drop_item(self, item):
        chosen_item = list(filter(lambda i: i.__dict__["name"].lower() == item, self.inventory))[0]
        self.inventory.remove(chosen_item)
        chosen_item.on_drop()
        self.room.add_item(chosen_item)

    def list_inventory(self):

        if not self.inventory:
            print("**Your inventory is empty.**")
        else:
            print("\n INVENTORY:")
            for index, i in enumerate(self.inventory): #enumerate turns a class object wrapper into a dictionary
                print(f" {index+1}) {i.name}: {i.description}")
                
        
