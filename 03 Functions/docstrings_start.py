# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """
    myFuncation(arg1, arg2) --> Doesn't really do anything, just prints.

    parameters:
    arg1: the first argument, whatever you feel like passing
    arg2: second argument, defaults to None.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
