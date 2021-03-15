'''
Single Responsibility Principle.

A class has to have on responsibility. If it has more, it becomes coupled. 
A single change to one responsibility might lead to change the other responsibility.
'''

##############
# Violation. #
##############

class User:

    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age

    def get_name(self) -> str:

        return self.name
    
    def get_age(self) -> int:

        return self.age
    
    def save(self, user: User):
        pass


'''
It is violating the single responsibility principle, as it is performint two tasks or 
responsibilities: user database management and user property management.
'''

#############
# Solution. #
#############

class UserDB:

    def get_user(self) -> User:
        pass

    def save(self, user:User):
        pass


class User:

    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age
        self._db = UserDB()

    def get_name(self) -> str:

        return self.name
    
    def get_age(self) -> int:

        return self.age

    def save(self):

        self._db.save(user=self)


'''
This way the related features are groupped together and it is not violating
the single responsibility principle anymore.
'''