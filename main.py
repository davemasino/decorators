def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


# This is a short way of saying
# def say_whee():
#     print("Whee!")
#
#
# say_whee = my_decorator(say_whee)
@my_decorator
def say_whee():
    print("Whee!")


say_whee()
