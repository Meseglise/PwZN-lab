# class Student:
#     pass
#
# s1 = Student()
# print(s1)

##

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'My name is {self.name}. Finna {self.name}'
#     def print_my_name(self):
#         print(f'{self.name = }')
# s1 = Student('Anna')
# print(s1)
# print(s1.name)
# s1.print_my_name()

##

class Student:
    classes = []

    def __init__(self, name):
        self.name = name
        self.classes = []
    def __str__(self):
        return f'My name is {self.name}. Finna {self.name}'
    def print_my_name(self):
        print(f'{self.name = }')
    def print_classes(self):
        print(self.classes)
    def add_class(self, c1):
        self.classes.append(c1)

s1 = Student('Anna')

s1.add_class('PwZN')
s1.add_class('MN')
s1.add_class('MMF')

s1.print_classes()

s2 = Student('Ziemowit')
s2.print_classes()