def bmi(height, weight):
    return weight / (height / 100) ** 2

class Person:
    def __init__(self, n, h , w):
        self.name = n
        self.height = h
        self.weight = w
    def return_bmi(self):
        return self.weight / (self.height / 100) ** 2
    def is_overweight(self):
        if self.weight >= 100:
            return True
        else:
            return False


p1 = Person("Elwing", 175, 75)
print(p1.name, p1.return_bmi())
print("過重與否:", p1.is_overweight())

p2 = Person("Bob", 180, 80)
print(p2.name, p2.return_bmi())
print("過重與否:", p2.is_overweight())