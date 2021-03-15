'''
Dependency Inversion Principle.
High-level modules should not depend on low-level modules. Both low and high 
level classes should depend on the same abstractions. Abstractions should not depend 
on details. Details should depend upon abstractions.
'''

##############
# Violation. #
##############

class BackendDeveloper:
    '''Low-level module.'''

    @staticmethod
    def python():

        print('Writing Python code for the backend.')


class FrontendDeveloper:
    '''Low-level module.'''

    @staticmethod
    def javascript():

        print('Writing JavaScript & CSS code for the frontend.')


class Project:
    '''High-level module.'''

    def __init__(self):

        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()

    def develop(self) -> str:

        self.backend.python()
        self.frontend.javascript()
        
        return 'Develop project codebase.'


project = Project()
print(project.develop())

'''
In the example above, the High-level module depends on the Low-level modules. This violates the
Dependency Inversion Principle.
'''
#############
# Solution. #
#############

class BackendDeveloper:
   '''Low-level module.'''

   def develop(self):

       self.__python_code()

   @staticmethod
   def __python_code():

       print('Writing Python code for the backend.')


class FrontendDeveloper:
   '''Low-level module.'''

   def develop(self):

       self.__javascript()

   @staticmethod
   def __javascript():

       print('Writing JavaScript & CSS code for the frontend.')


class DeveloperTeam:
   '''Abstract module.'''

   def __init__(self):

       self.backend = BackendDeveloper()
       self.frontend = FrontendDeveloper()

   def develop(self):
       self.backend.develop()
       self.frontend.develop()


class Project:
   '''High-level module.'''

   def __init__(self):

       self.__developers = DeveloperTeam()

   def develops(self):

       return self.__developers.develop()


project = Project()
print(project.develops())


'''
This way, the High-level module is not depending on the Low-level module(s), but on abstraction,
therefore it conforms the Dependency Inversion Principle.
'''