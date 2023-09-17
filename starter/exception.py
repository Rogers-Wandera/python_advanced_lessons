# Exceptions
x = 4
try:
    # print(x/0)
    # print(y)
    if type(x) is not str:
        raise Exception("X should be a string")
except NameError:
    print("NameError: Name 'y' is not defined")
except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero")
except Exception as error:
    print(f"Error: {error}")
finally:
    print("Me i just run regardless")


# creating custom errors
class CustomError(Exception):
    pass


try:
    if type(x) is not list:
        raise CustomError("X should be a list")
except Exception as error:
    print(f"Error: {error}")
