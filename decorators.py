
def decorator(func):
    def decoreted(input_text):
        print('func start')
        func(input_text)
        print('func end')
    return decoreted


@decorator
def hello_world(input_text):
    print(input_text)


hello_world('???')








# def check_integer(func):
#     def decorated(width, height):
#         if width >= 0 and height >= 0:
#             return func(width, height)
#         else:
#             raise ValueError("Error")
#     return decorated
#
#
# @check_integer
# def rect_area(width, height):
#     return width * height






# class User:
#     def __init__(self, auth):
#         self.is_authenticated = auth
#
# user = User(auth=False)
#
# r_area = rect_area(user, 10, 10)
# print(r_area)
#
#
# def check_integer(func):
#     def decorated(user, width, height):
#         if width >= 0 and height >= 0:
#             return func(user, width, height)
#         else:
#             raise ValueError("Error")
#     return decorated
#
# def login_integer(func):
#     def decorated(user, width, height):
#         if user.is_authenticated
#             return func(user, width, height)
#         else:
#             raise PermissionError("Error")
#     return decorated
#
# @check_integer
# @login_integer
# def rect_area(user, width, height):
#     return width * height


