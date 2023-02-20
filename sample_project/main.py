# # enter three number in one line
# a, b, c = input("enter three number").split(" ")
# print(a,b,c);
#
# #get harrypan1
# # h = "harryPotter"
# # p = "peterPan"
# #
# # print(h[0:5]+p[5:])
# #
# # print(h[0:5],p[5:])
#
# #count vowel in given string
# # string = input("Enter String: ")
# #
# # count = 0;
# #
# # for i, x  in enumerate(string):
# #     if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
# #         count += 1
# # print( count)
#
# # string = input("Enter String: ")
# # string = string.lower();
# # total = 0
# # total += string.count("abc");
# # print(total)
#
# #traingular num
# # sum = 0
# # number = int(input('Enter number'))
# # for i in range(number):
# #     sum += i;
# #     if sum == number:
# #         print('triaingular numb')
# #
# #     else:
# #         print('not triaingular numb')
# #
#
# # def temp_f():
# #     for i in range(0, 100, 5):
# #         yield i
# #
# # temp = temp_f()
# # print(temp.__next__())
# # print(temp.__next__())
#
# # n = int(input("Enter number of lines of pattern: "))
# #
# # for i in range(1,n+1):
# #     for j in range(1, 5, i+1):
# #         print((j+1)%2, end="")
# #     print()
#
# # n = int(input("Enter number of lines of pattern: "))
# def temp_f():
#     for i in range(1, 5 + 1):
#         for j in range(1, i + 1):
#             yield ((j + 1) % 2)
#
# temp = temp_f()
# for i in range(0, 5):
#     print(temp.__next__())
#     print(temp.__next__())
#
# #palindrone
# string = "jjssjj"
# lower_String = string.lower()
# li = list(lower_String)
# reverse_li = li[::-1]
# if(li == reverse_li):
#     print("palindrone")
# else:
#     print("not palindrone")
#
# #check if value present in dictionary list or not
# dict1 = {
#     "name" : "junee",
#     "location" : "ktm",
#     "Usn" : "101"
# }
# dict2 = {
#     "name" : "sunee",
#     "location" : "bkt",
#     "Usn" : "201"
# }
# list = [dict1, dict2]
# value = input("Enter value")
#
# for i, j in enumerate(list):
#     if value in j["name"] or value in j["location"] or value in j["Usn"]:
#         print(j);

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return node


print(get_attr_number('ff'))