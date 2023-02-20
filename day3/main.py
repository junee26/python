# # text alignment
# cstr = "ABCD"
# print(cstr.center(8, '#'))
# print(cstr.ljust(8, '#'))
# print(cstr.rjust(8, '#'))
import json

#list comprehension
# check if string length == 5
# fruits =  ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = [x for x in fruits if len(x) == 5]
#
# print(newlist)
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# fruit = [x for x in fruits if "a" in x]
# print(fruit) #print in list
# fruit = [print(x) for x in fruits if "a" in x]
# #print in fruit



# student_1 ={
#     "name": "Cezane",
#     "USN":"006644",
#     "locaion": "Nepal"
# }
#
# student_2 ={
#     "name": "Junee",
#     "USN":"113322",
#     "locaion": "Nepal"
# }
#
# student_3 ={
#     "name": "Anish",
#     "USN": "1133222",
#     "locaion": "Nepal"
# }
#
# student_4 ={
#     "name": "Nisht",
#     "USN": "1133222",
#     "locaion": "India"
# }
#
# friend_list = [student_1, student_2, student_3, student_4]
#
# nepal = [x for x in friend_list if x["locaion"] == "Nepal"]
# print(nepal)
#
# india = [x for x in friend_list if x["locaion"] == "India"]
# print(india)
#
# name_with_ee = [x for x in friend_list if "ee" in x["name"]]
# print(name_with_ee)
#
# name_with_ee = [x for x in friend_list if "3" in x["USN"]]
# print(name_with_ee)

# import requests
# request_url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url=request_url)
# json_response=response.json()
# print(json_response);
#
# change = [x for x in json_response if len(x['title'].split()) >=8]
# print(len(json_response),change)

#
# import requests
# request_url = "https://jsonplaceholder.typicode.com/comments"
# response = requests.get(url=request_url)
# json_response=response.json()
# all_email = [i for i in json_response if i['id']< 5]
# print(all_email)

#
# #print email
# import requests
# request_url = "https://jsonplaceholder.typicode.com/comments"
# response = requests.get(url=request_url)
# json_response=response.json()
# all_email = []
# for email in json_response:
#     all_email.append((email['email']))
# print(all_email)

# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# response = requests.post(api_url, json=todo)
# print(response.json())

#postID is 5 where name contain ee
# import requests
# api_url = "https://jsonplaceholder.typicode.com/comments"
# response = requests.get(url=api_url, params = {
#     "postId" : "5"
# })
# data = response.json()
# name_ee = [i for i in data if i["name"].count("e")>2]
# print(name_ee)

# import requests
# api_url = "https://jsonplaceholder.typicode.com/posts"
# data = { 'title': 'foo', 'body': 'bar', 'userId': 1,}
# data_string = json.dumps(data)
# response = requests.post(api_url, json=data, headers= {'Content-type': 'application/json; charset=UTF-8',
#   })
# print(response); #status
# # print(response.json()); #data

# import requests
# import json
#
# api_url = "https://api.publicapis.org/random"
# response = requests.get(api_url)
# data = []
# for i in range(0,5):
#     response = requests.get(api_url).json()
#     data.append(response)
# print(data)

# import requests
# import json
# base_url = "https://api.publicapis.org/"
# end_url = "random"
# request_url = base_url + end_url;
# end_value = []
# for i in range(5):
#     response = requests.get(request_url)
#     data = response.json()
#     end_value.append(data["entries"][0])
# print(len(end_value))

import requests
request_url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url=request_url, params={"postId": input("enter")})
va = (response.json())
print(va)
