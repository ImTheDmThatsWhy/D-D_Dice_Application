# Exception is this case is being used as a subclass to make new exceptions.
# Exception is a built in class in Python3 and is referred to the base Exception,
# which is required to create all custom Exception classes.


# The NegativeError is a custom class that raises an exception if negative input is used.
# Parameters:
#     Exception: Parametre 1, is a built-in
#     python sub class that is being used to
#     create a custom class.
# Code:
#     pass is being used to prevent an error
#     as no definition is required for this
#     class.
class NegativeError(Exception):
    pass


# The NonExistantDice custom class is an exception that is raised if a user enters a dice combination that does not exist.
# This is a custom class that raises an exception if a dice that does not exist is inputted.
# Parameters:
#     Exception: Parametre 1, is a built-in
#     python sub class that is being used to
#     create a custom class.
# Code:
#     pass is being used to prevent an error
#     as no definition is required for this
#     class.
class NonExistantDice(Exception):
    pass


# The InnappropriateInput custom class is an exception that is raised if a user enters an incorrect input when prompted.
# Parameters:
#     Exception: Parametre 1, is a built-in
#     python sub class that is being used to
#     create a custom class.
# Code:
#     pass is being used to prevent an error
#     as no definition is required for this
#     class.
class InappropriateInput(Exception):
    pass


# The NoInput custom class in an exception that is raised if the user leaves the input blank when prompted.
# Parameters:
#     Exception: Parametre 1, is a built-in
#     python sub class that is being used to
#     create a custom class.
# Code:
#     pass is being used to prevent an error
#     as no definition is required for this
#     class.
class NoInput(Exception):
    pass
