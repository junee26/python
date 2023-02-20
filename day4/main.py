# def add(a,b,c):
#     return a+b+c
# print(add(1,2,3))


# print((lambda a,b,c: a+b+c)(1,2,3))


# def my_fun(a):
#     print(a)
#
# def my_fun2():
#     print("hello")
#     return 10
#
# # my_fun(my_fun2())
#
# my_fun(lambda : 20)

#to call 5 lambda function
# n, m = input("enter").split()
#
# def calc(a):
#     return a
#
# print(calc(lambda n, m: n + m)(int(n), int(m)))
# print(calc(lambda n, m: n * m)(int(n), int(m)))
# print(calc(lambda n, m: n - m)(int(n), int(m)))
# print(calc(lambda n, m: n / m)(int(n), int(m)))

# import qrcode
# img = qrcode.make('My name is junee')
# img.save("my_qr.png")

# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# txt = input("enter your name")
# qr.add_data(txt)
# qr.make(fit=True)
# img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
# img.save("test1.png")

# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# # txt = input("enter your name")
# qr.add_data({
#     "name" : "junee",
#     "location" : "ktm"
# })
# qr.make(fit=True)
# img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
# img.save("test12.png")

# class TripToNepal:
#     budget = 5000
#     tranport = "car"
#
#     def eat_smth(self, cost):
#         self.budget = self.budget - cost
#
#
#     def change_transport(self, newMode):
#         self.tranport = newMode
#         return self.tranport
#
#     def current_situation(self):
#         print(self.budget);
#
# trip = TripToNepal()
# trip.eat_smth(100)
# trip.eat_smth(200)
# print(trip.change_transport("bike"))
# trip.current_situation()
#
# #we cn create object again and again  of same class for multiple time
# trip = TripToNepal()
# trip.eat_smth(200)
# trip.current_situation()


# class caluculator:
#     a = 1
#     b = 2
#
#     def add(self):
#         print(self.a + self.b)
#
#     def sub(self):
#         print(self.a - self.b)
#
#     def div(self):
#         print(self.a / self.b)
#
#     def mul(self):
#         print(self.a * self.b)
#
#
# calc = caluculator()
# calc.add()
# calc.sub()
# calc.div()
# calc.mul()

#
#
# class Student:
#     name = []
#     usn = []
#     branch = []
#
#     def __init__(self, name, usn, branch):
#         self.name.append(name)
#         self.usn.append(name)
#         self.branch.append(name)
#
#     def display(self):
#         print(self.name, self.usn, self.branch)
#
#     def update_branch(self, branch):
#         self.branch = branch
#
# student = Student('junee', 100, 'a');
# student = Student('sunee', 200, 'a');
# student = Student('lunee', 300, 'a');
#
# student.display()

# search in given name
# name = "junee"
# if(name.count('une')):
#     print('true');

#search the input value
# class Student:
#     def __init__(self, name, usn, branch):
#         self.name = name
#         self.usn = usn
#         self.branch = branch
#
#     def update_branch(self, updateBranch):
#         self.branch = updateBranch
#         return self.branch
#
#
# # creating list
# list = []
# student = Student('munee', 2, 'a');
# print(student.update_branch('z'))
#
# list += [Student(name, usn, branch) for name, usn, branch in
#          [('junee', 2, 'a'), ('nisa', 40, 'b'), ('sunee', 44, 'c'), ('rina', 67, 'd')]]
#
# search_query = input("enter value")  # input is unee
# for obj in list:
#     if search_query in obj.name:
#         print(obj.name, obj.usn, obj.branch)


#find area and perimeter using *args
# from math import pi
#
#
# class Shape:
#     usn = ''
#     branch = ''
#
#     def __init__(self, *args):
#
#         if (len(args) == 1):
#             print(f"Area {pi * args[0] * args[0]}")
#             print(f"Perimeter 2*pi*args[0]")
#         else:
#             print(f"Area {args[0] * args[1]}")
#             print(f"Perimeter {(args[0] + args[1]) * 2}")
#
#
# s1 = Shape(10)
# s2 = Shape(10, 20)

class Atm:

    def __init__(self, balance, pin, card_no):
        self.balance = balance
        self.pin = pin
        self.card_no = card_no


    def display(self):
        print('sss')
        print("My Card number is", self.card_no)
        print("My Pin number is", self.pin)
        print("My Current balance is", self.balance)

    def withdrawl(self, pin):
        print(self.pin)
        entered_pin = input("enter your pin")

        

myATM = Atm(1000, 1234, 5678)
myATM.display()


