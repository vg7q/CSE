# Name
# Health
# Pick up items
# move
# attack
# death
# dialogue
# perform actions (use, Push, etc.)
# Descriptions
# status effect
# Take damage


class Character(object):
    def __int__(self, name, descriptions, dialogue, holding):
        self.name = name
        self.health = 10
        self.description = descriptions
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
        self.health -= 10
        if self.health >= 10:
            print("%s has % health" % (self.name, self.health))
        else:
            self.death()


Bob = Character()
