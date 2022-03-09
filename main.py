class Backpack:
    def __init__(self, color, size, items, open):
        self.color = color
        self.size = size
        self.items = items
        self.open = open

    def openBag(self):
        self.open = True
        print('Bag Opened')
    def closeBag(self):
        self.open = False
        print('Bag Closed')
    def putin(self, item):
        if self.open:
            self.items.append(item)
            print('Item added succesfully')
        else:
            print("Item couldn't be added")
    def takeout(self, item):
        x=0
        if self.open:
            for i in range(len(self.items)):
                if self.items[i] == item:
                    x=1
            if x == 1:
                self.items.remove(item)
                print('Item removed succesfully')
            else:
                print('Item not in bag')
        else:
            print("Backpack is closed")
smallBlueBackpack = Backpack('blue', 'small', [], False)
mediumRedBackpack = Backpack('red', 'medium', [], False)
largeGreenBackpack = Backpack('green', 'large', [], False)

smallBlueBackpack.openBag()
smallBlueBackpack.putin('lunch')
smallBlueBackpack.putin('jacket')
smallBlueBackpack.closeBag()
smallBlueBackpack.openBag()
smallBlueBackpack.takeout('jacket')
smallBlueBackpack.closeBag()
