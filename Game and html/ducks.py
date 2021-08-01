class Wing(object):

    def __init__(self, ratio) -> None:
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weeeee! This is fun")
        elif self.ratio == 1:
            print("This is hard work but I'm flying")
        else:
            print("I think I'd rather walk")


class Duck(object):

    def __init__(self) -> None:
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, Waddle, Waddle")

    def swim(self):
        print("Come on in, the water is lovely")
    
    def quack(self):
        print("Quack, Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):
    
    def walk(self):
        print("Waddle, Waddle, I waddle too")
    
    def swim(self):
        print("Come on in, but it's a bit chilly this far South")
    
    def quack(self):
        print("Are ya 'avin' a larf?? I'm a penguin!")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == "__main__":
    donald = Duck()
    donald.fly()

    # percy = Penguin()
    # test_duck(percy)

