'''
Interface Segregation Principle.
This principle is used for large interfaces, and the point is that the interface should 
implement only generic methods, which are used by all clients.
'''

##############
# Violation. #
##############

class IAnimalMove:

    def walk(self):

        raise NotImplementedError

    def swim(self):

        raise NotImplementedError

    def fly(self):

        raise NotImplementedError


class Fish(IAnimalMove):

    def walk(self):
        pass

    def swim(self):
        pass
    
    def fly(self):
        pass

class Bird(IAnimalMove):

    def walk(self):
        pass

    def swim(self):
        pass
    
    def fly(self):
        pass

class Mammal(IAnimalMove):

    def walk(self):
        pass

    def swim(self):
        pass
    
    def fly(self):
        pass

'''
The IAnimalMove interface defines the different movement types by the classified animals. The
violation comes when we consider that the Fish class has to implement the fly method for example.
'''

#############
# Solution. #
#############

class IAnimalMove:

    def move(self):

        raise NotImplementedError


class Fish(IAnimalMove):

    def move(self):
        pass


class Bird(IAnimalMove):

    def move(self):
        pass


class Mammal(IAnimalMove):

    def move(self):
        pass

'''
By having a way more general interface, our animal classes do not have to implement 
useless methods.
'''