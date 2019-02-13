# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []
        self.item_list = []
    
    def add_item(self, item):
        self.items.append(item)
        self.item_list = [i.name for i in self.items]
    def remove_item(self, item):
        self.items.remove(item)
        self.item_list = [i.name for i in self.items]

