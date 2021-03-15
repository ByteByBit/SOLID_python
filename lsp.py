'''
Liskov Substitution Principle.
The aim of this principle is to ascertain that a sub-class can assume the place of its
super-class without errors.  If the code finds itself checking the type of class then,
it must have violated this principle.
'''

##############
# Violation. #
##############

class Vehicle:

    def __init__(self, name: str, year_of_produce: int):

        self.name = name
        self.year_of_produce = year_of_produce

    def get_name(self) -> str:

        return f'The vehicle name {}'.format(self.name)

    def get_year_of_produce(self) -> str:

        return f'The vehicle produced in {}'.format(self.year_of_produce)

    def engine(self):
        pass

    def start_engine(self):

        self.engine()


class Car(Vehicle):

    def start_engine(self):
        pass


class Bicycle(Vehicle):

    def start_engine(self):
        pass

'''
Usually bycicles have no engine, therefore it is a bit hard to start it. This is the reason
why this example violates the Liskov Substitution Principle.
'''

#############
# Solution. #
#############

class Vehicle:

    def __init__(self, name: str, year_of_produce: int):
        self.name = name
        self.year_of_produce = year_of_produce

    def get_name(self) -> str:

        return f"The vehicle name {}".format(self.name)

    def get_year_of_produce(self) -> str:

        return f'The vehicle produced in {}'.format(self.year_of_produce)


class VehicleWithoutEngine(Vehicle):

    def start_moving(self):

        raise NotImplemented


class VehicleWithEngine(Vehicle):

    def engine(self):
        pass

    def start_engine(self):

        self.engine()


class Car(VehicleWithEngine):

    def start_engine(self):
        pass


class Bicycle(VehicleWithoutEngine):

    def start_moving(self):
        pass


'''
This way, the start_engine method is implemented only in classes referring to objects
with engine. Objects or vehicles without engine has a start_movin method instead.
'''