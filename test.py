from enemy import Enemy, Troll, Vampire, VampireKing
from player import Player

mask = Player("Batman")

print(mask.name)
print(mask._lives)

mask._lives -= 1
print(mask._lives)
mask._lives -= 1
print(mask)
mask._lives -= 1
print(mask)
print()
print("*"* 100)
print()
mask._lives -= 1
print(mask)      # uses the __str__ method we defined to describe the object in form of a string

mask._lives = 9
print(mask)
print(mask._lives)

print("*" * 100)

mask.level += 10
print(mask._score)
print(mask.level)
print(mask)

print("*" * 100)

mask.level = 23
print(mask._score)

mask.level -= 26
print(mask._score)
print(mask.level)
print(mask)
print("*" * 100)

mask.score = 400
print(mask)


# random_monster = Enemy("Basic Enemy", 12, 1)
# print(random_monster)

# random_monster.take_damage(4)
# print(random_monster)

# random_monster.take_damage(8)
# print(random_monster)

# random_monster.take_damage(8)
# print(random_monster)
print()

ugly_troll = Troll("Pug")
print("Ugly Troll: {}".format(ugly_troll))

another_troll = Troll("ug")
print("Another troll : {}".format(another_troll), end="")

brother = Troll("Urg")
print(f" and his brother {brother}")

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()


vamp = Vampire('Vlad')
print(vamp)
# vamp.take_damage(10)
# print(vamp)
# vamp.take_damage(10)
# print(vamp)
# vamp.take_damage(4)
# print(vamp)
# vamp.take_damage(1)
# print(vamp)
# vamp.take_damage(11)
# print(vamp)
# vamp.take_damage(1)
# vamp.take_damage(1)
# vamp.take_damage(1)
# vamp.take_damage(1)
print(vamp)
print("*" * 100)
print()

ugly_troll.take_damage(30)
# print(ugly_troll._default_health)
print(ugly_troll)
another_troll.take_damage(30)
another_troll.take_damage(30)
# print(another_troll)

while vamp._alive:
    vamp.take_damage(1)
    print(vamp)

sasha = VampireKing("Dracula")
print(sasha)

while sasha._alive:
    sasha.take_damage(10)
    # print(sasha)