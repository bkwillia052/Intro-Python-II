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

    def __str__(self):
        return f'\n{self.name}\n\n    {self.description}\n\n'
    
    def add_item(self, item):
        self.items.append(item)
        self.item_list = [i.__dict__["name"] for i in self.items]
    def remove_item(self, item):

        chosen_item = list(filter(lambda i: i.__dict__["name"].lower() == item, self.items))[0]

        if not chosen_item:
            print("No such item exists!")
        else:
            self.items.remove(chosen_item)
            self.item_list = [i for i in self.items]
            return chosen_item

