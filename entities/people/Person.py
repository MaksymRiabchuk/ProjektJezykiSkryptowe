from memory_profiler import profile


# @profile
def id_generator_func():
    current_id = 0
    while True:
        current_id += 1
        yield current_id


class Person:
    # @profile
    def __init__(self, name, lastname, age):
        self.generateId = id_generator_func()
        self.id = next(self.generateId)
        self.age = age
        self.name = name
        self.lastname = lastname

    # @profile
    def printPersonInfo(self):
        print("Name: ", self.name)
        print("Lastname: ", self.lastname)
        print("Age: ", self.age)
