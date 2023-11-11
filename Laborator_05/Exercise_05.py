'''
Ex.05 Create a class hierarchy for animals, starting with a base class Animal. Then, create subclasses like Mammal, Bird, and Fish.
Add properties and methods to represent characteristics unique to each animal group.
'''

class Animal:
    existing_id = set()
    def __init__(self, id, name, age, weight, height, colour):
        if id in Animal.existing_id:
            raise ValueError(f"The id {id} is already used.")
        self.id = id
        Animal.existing_id.add(id)
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.colour = colour

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def can_walk(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def can_swim(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def can_fly(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class Mammal(Animal):
    def __init__(self, id, name, age, weight, height, colour, number_of_legs, diet_type):
        super().__init__(id, name, age, weight, height, colour)
        self.number_of_legs = number_of_legs
        self.diet_type = diet_type

    def set_number_of_legs(self, number_of_legs):
        self.number_of_legs = number_of_legs

    def get_number_of_legs(self):
        return self.number_of_legs

    def set_diet_type(self, diet_type):
        self.diet_type = diet_type

    def get_diet_type(self):
        return self.diet_type

    def hunt_or_forage(self):
        if self.diet_type in ["Carnivore", "Omnivore"]:
            return f"{self.name} is hunting."
        else:
            return f"{self.name} is foraging."

    def can_walk(self):
        if self.number_of_legs > 0:
            return True
        else:
            return False

    def can_swim(self):
        return False

    def can_fly(self):
        return False


class Bird(Animal):
    def __init__(self, id, name, age, weight, height, colour, wing_span):
        super().__init__(id, name, age, weight, height, colour)
        self.wing_span = wing_span

    def set_wing_span(self, wing_span):
        self.wing_span = wing_span

    def get_wing_span(self):
        return self.wing_span

    def lay_eggs(self):
        return f"{self.name} is laying eggs."

    def can_walk(self):
        return True

    def can_swim(self):
        return False  # Some birds can swim, but not all. This can be overridden.

    def can_fly(self):
        if self.age > 0:
            return True
        else:
            return False


class Fish(Animal):
    def __init__(self, id, name, age, weight, height, colour, number_of_fins):
        super().__init__(id, name, age, weight, height, colour)
        self.number_of_fins = number_of_fins

    def set_number_of_fins(self, number_of_fins):
        self.number_of_fins = number_of_fins

    def get_number_of_fins(self):
        return self.number_of_fins

    def swim(self):
        return f"{self.name} is swimming."

    def can_walk(self):
        return False

    def can_swim(self):
        return True

    def can_fly(self):
        return False




