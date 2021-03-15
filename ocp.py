'''
Open-Closed Principle.
Software entities(Classes, modules, functions) should be open for extension, not
for modification.
'''

##############
# Violation. #
##############

class User:

    def __init__(self, name: str, stage: str):

        self.name = name
        self.stage = stage

    def get_name(self) -> str:

        return self.name


def user_bonus(users: list):

    for user in users:

        if user.stage == 'beginning':
            print('{} received 700 bonus points.'.format(user.name))

        elif user.stage == 'middle':
            print('{} received 2100 bonus points.'.format(user.name))


users = [
    User(name='Foo', stage='beginning'),
    User(name='Bar', stage='middle')
]

user_bonus(users)


'''
The user_bonus function seems ok when we have two different stages to consider,
but even with just ten different stage, it becomes long and a headache to manage.
'''

#############
# Solution. #
#############

class User:

    def __init__(self, name: str, stage: str):

        self.name = name
        self.stage = stage

    def get_name(self) -> str:

        return self.name
    
    def get_bonus(self):
        
        return 700


class MidStageBonus(User):

    def get_bonus(self):

        return super().get_bonus() * 3


class AdvancedStageBonus(MidStage):

    def get_bonus(self):

        return super().get_bonus() * 3


'''
This way any new bonus type can be just typed here, without changing anything else.
'''