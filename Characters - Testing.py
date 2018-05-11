class Character(object):
    def __init__(self, name, description, dialogue, holding):
        self.name = name
        self.description = description
        self.health = 70
        self.dialogue = dialogue
        self.holding = holding
        self.dead = False

    def pick_up(self):
        if self.holding:
            print("you cannot pick up this item")
        else:
            print("you picked up an item")

    def attack(self, target):
        print("%s attack %s" % (self.name, target.name))
        target.damage()

    def death(self):
        if self.health <= 0:
            self.dead = True
            print("%s is dead." % self.name)

    def damage(self):
        self.health -= 1
        if self.health >= 1:
            print("%s has %s health" % (self.name, self.health))
        else:
            self.death()


Bob = Character('Leo', 'A character', None, None)
Joe = Character('Toe', 'Another Character', None, None)

print(Bob.name)
print(Bob.description)
Bob.attack(Joe)
Joe.attack(Bob)