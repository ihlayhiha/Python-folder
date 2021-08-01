class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1) -> None:
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True
        self._default_health = self.hit_points
        
    def take_damage(self, damage):
        if self.lives == 0:
            print(f"{self.name} is already dead")
        else:
            total_damage = damage
            while self.hit_points <= damage and self.lives >= 1:
                self.lives -= 1
                damage -= self.hit_points
                self.hit_points = self._default_health
            if self.lives == 0:
                print(f"Your beloved '{self.name}' died.")
                self.hit_points = 0
            else:
                self.hit_points -= damage
            print(f"I took {total_damage} points damage and have {self.hit_points} left.")
    
    def __str__(self) -> str:
        return "Name: {0.name}, Lives: {0._lives}, Hit Points: {0._hit_points}".format(self)


class Troll(Enemy):
    
    def __init__(self, name) -> None:
        # super(Troll, self).__init__(name=name, hit_points=23, lives=1)
        super().__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you.".format(self))
    
class Vampire(Enemy):

    def __init__(self, name) -> None:
        super().__init__(name=name, hit_points=12, lives=3)

