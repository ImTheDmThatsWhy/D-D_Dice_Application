# Exception is this case is being used as a subclass to make new exceptions. Exception is a built in class in Python3 and is referred to the base Exception, which is required to create all custom Exception classes.


# The negative error class is an exception that is raised if a user enters a negative input
class NegativeError(Exception):
    pass


# The NonExistantDice class is an exception that is raised if a user enters a dice combination that does not exist
class NonExistantDice(Exception):
    pass


# The InnappropriateInput class is an exception that is raised if a user enters an incorrect input when prompted
class InappropriateInput(Exception):
    pass


# The NoInput class in an exception that is raised if the user leaves the input blank when prompted.
class NoInput(Exception):
    pass
