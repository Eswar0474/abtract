class Animal():
    def make_sound(self):
        print("sound")
class Dog(Animal):
    def make_sound(self):
        print("sound by dog")
class Cat(Animal):
    def make_sound(self):
        print("sound by cat")
for i in [Cat(),Dog()]:
    i.make_sound()