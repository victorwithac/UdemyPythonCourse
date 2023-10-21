class Class:
    # @staticmethod #is a function inside the class
    # def function_in_the_class(*args, **kwargs):
    #     print('This', args, kwargs)

    def a_function(*args, **kwargs):
        print('this')



# c1 = Class()
# c1.function_in_the_class(1, 2, 3)
# Class.function_in_the_class(number=10)


Class.a_function(x=1, y=2, z=3)