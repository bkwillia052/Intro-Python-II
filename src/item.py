
class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return str(self.__dict__)
    
    def on_take(self):
        print(f"A {self.name} has been picked up.")
        
    def on_drop(self):
        print(f"A {self.name} has been dropped.")