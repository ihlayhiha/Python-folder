import random

class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1) -> None:
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True
        
    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points of damage, {} left".format(damage, remaining_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life.".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self) -> str:
        return "Name: {0._name}, Lives: {0._lives}, Hit Points: {0._hit_points}".format(self)


class Troll(Enemy):
    
    def __init__(self, name) -> None:
        # super(Troll, self).__init__(name=name, hit_points=23, lives=1)
        super().__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you.".format(self))
    
class Vampire(Enemy):

    def __init__(self, name) -> None:
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("**** {0._name} dodges ****".format(self))
            return True
        else:
            return False
    
    def take_damage(self, damage):
        if not self.dodges():
            return super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name) -> None:
        super().__init__(name=name)
        self._hit_points = 140

    def take_damage(self, damage):
        return super().take_damage(damage=damage//4)

