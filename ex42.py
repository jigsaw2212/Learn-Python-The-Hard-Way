## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

#Dog is-a animal. Dog has-a __init__ and a name
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Cat is-s animal. Cat has a __init__
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a type of a object. Person has-a __init__. 
class Person(object):

    def __init__(self, name):
        ## Person has-a name which is equal to name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        # We are calling the __init__ of the base class using super keyword
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is a Cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary has-a pet equal to satan
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()