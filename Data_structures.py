
# # 1
# a = "My Name"

# print(a[::-1])


# # 2

# b  = "excellent"
# c = 0
# for i in b:
#     if "a" ==  i or "e" == i or "i" == i or "o" == i or "u" == i:
#         c += 1
# print(c)


# # 3
# s =  "1234567"
# r = s[::-1]


# if s == r:
#     print("yes")
# else:
#     print('NO')

# # 4

# word = "A decimal point"
# anagram = "i m a dot in place "

# without_whitespace = ""
# for i in word:
#     if i == " ":
#         continue
#     without_whitespace += i


# for i in anagram:
#     without_whitespace_arg = ""
#     if i == " ":
#         continue
#     without_whitespace_arg += i
#     if without_whitespace_arg in without_whitespace:
#         print("Checking....")
#     else:
#         print("Not anagram")
#         break
# else:
#     print("Yea anagram")

# # 5


# def occurance_finder(text,substring):
#     where_is = []
#     start = 0

#     while True:
#         finder = text.find(substring,start)
#         if finder == -1:
#             break
#         where_is.append(finder)
#         start = finder+1
    
#     return where_is
        




# print(occurance_finder("banana","ana"))


# # 6

# def string_repetation_replacemt(text):
#     after_text = ""
#     count = 1
#     for i in range(1,len(text)): 
#         if text[i] == text[i - 1]:
#             count += 1
        
#         else :
#             after_text += text[i - 1] + str(count)
#             count = 1 
#     after_text += text[i - 1] + str(count)
    
#     return after_text

# print(string_repetation_replacemt("aaabbbccc"))

# # 7

# def Unique_string_checker(text):
#     checking_variables = ""

#     for i in text:
#         if i in checking_variables:
#             return "It is not a unique charactes word"
            
#         else:
#             checking_variables += i
#     return "it is unique characters word"



# print(Unique_string_checker("flash"))

# #8

# def lower_upper(text,lowercase_or_uppercase):
#     lowercase_or_uppercase = lowercase_or_uppercase.lower()
#     upgraded_text = ""
#     if lowercase_or_uppercase == "lowercase":
#         upgraded_text = text.lower()

#     elif lowercase_or_uppercase == "uppercase":
#         upgraded_text = text.upper()

#     return upgraded_text

# print(lower_upper("apple","uppercase"))



# # 9 

# def word_in_a_string(string):
#     count = 0

#     for i in string:
#         if i == " ":
#             count += 1
#     else:
#         pass
#     count += 1

#     return(count)


# print(word_in_a_string("hello jonny"))



# #10

# string_1 = "hello"
# string_2 = "steve"

# contacenate = ''.join([string_1,string_2])
# print(contacenate)

# #11


# def remove_element(lst, element):
#     return [x for x in lst if x != element]


# my_list = [1,2,3,2,4,2]
# element = 2

# new_list = remove_element(my_list,element)
# print(new_list)

# # 12

# A_list = [2,6,3,7,10]
# A_list.sort()

# second_largest_number = A_list[-2]
# print(second_largest_number)

# # 13

# my_list = ["apple","apple","grapes","banana","banana","banana"]
# my_dict = {}

# for i in my_list:
#      counts = my_list.count(i)
     
#      if i in my_dict:
#         pass
        
#      else:
#           my_dict.update({i:counts})

# print(my_dict)

# # 14


# my_list2 = ["apple","johhny","banana","grapes"]

# my_list2 = my_list2[::-1]

# print(my_list2)




# # 15


# my_list3 = [1, 2, 3, 2, 4, 5, 5,4,6]
# unique = []

# for item in my_list3:
#     if item not in unique:
#         unique.append(item)

# my_list3 = unique
# print(my_list3)

# # 16

# my_list4 = [1,2,3,4,7,6,7]

# if my_list4 == sorted(my_list4):
#     print("Assending")
# elif my_list4 == sorted(my_list4,reverse=True):
#     print("Decending")
# else:
#     print("not sorted")


# # 17 
# my_list5 = [1,2,3,4,5,6,7,8]
# my_list6 = [9,10,11,12,13,14,15,16]

# list1 = my_list5 + my_list6
# sorted(list1)
# print(list1)

# # 18

# list2 = [1,2,3,4,5,6,7]
# list3 = [1,3,9,10,7]

# intersected_elements = []

# for i in list3:
#     if i in list2:
#         intersected_elements.append(i)

# print(intersected_elements)

# # 19

# list4 = [1,2,3,4,5,6,7]
# list5 = [9,10,11,5,12,1,2,3]

# union_list = list4+list5
# print(union_list)

# unique = []

# for item in union_list:
#     if item not in unique:
#         unique.append(item)

# union_list = unique
# print(union_list)

# # 20
# import random

# def shuffle(list_):
#     len_of_list = len(list_)

#     for i in range(len_of_list-1,0,-1):
#         random_index = random.randint(0,i)
#         list_[i] , list_[random_index] = list_[random_index],list_[i]
#     return list_

# my_list6 = [1,2,3,4,5,6,7]
# print(shuffle(my_list6))  

# # 21
# tuple1 = (1,2,3,4,5,6)
# tuple2 = (7,8,9,1,2,3)


# def tuple_converter(tuple1,tuple2):
#     commom_values = []
#     for i in tuple1:
#         if i in tuple2:
#             commom_values.append(i)

#     return tuple(commom_values)

# print(tuple_converter(tuple1,tuple2))

# # 22

# # first_intergers = (input("Enter First values:  "))
# # second_integers = (input("Enter Second values:  "))



# # set1 = set(map(int,first_intergers.split(",")))
# # set2 = set(map(int,second_integers.split(",")))

# # common_value = set()
# # for i in set1:
# #     if i in set2:
# #         common_value.add(i)

# # print(common_value)

# # 23

# a = (1,2,3,4)
# b = (1,2,3,4)
# print(type(a))
# print(a+b)

# def tuple_concatenator():
#     Input1 = input("First tuple Please write comas:    ")
#     Input2 =  input("Second tuple Please write comas:    ")
    

#     tuple3 = tuple(map(int,Input1.split(",")))
#     tuple4 = tuple(map(int,Input2.split(",")))

#     contacenate_tuple = tuple3 + tuple4
#     return contacenate_tuple

# print(tuple_concatenator())

# # 24 
  
# first_input = input("Enter some words:    ")
# second_input = input("Enter some words:    ")


# set1 = set(first_input.split(","))
# set2 = set(second_input.split(","))

# unique_element = set()
# for i in set1:
#     if i not in set2:
#         unique_element.add(i)

# print(f'Element that are in first set but not in second {unique_element}')

# # 25

# raw_tuple5 = (input("Enter values :  "))
# tuple5 = tuple(map(int,raw_tuple5.split(",")))

# start_index = int(input("Enter the start of index:    "))
# end_index = int(input("Enter the end of index:    "))+1



# print(tuple5[start_index:end_index])


# # 26

# set3 = set(input("Enter some words:   ").split(","))
# set4 = set(input("Enter some words:   ").split(","))

# set3.update(set4)
# union = set3
# print(union)

#27

# tuple6 = input("Enter int:   ")

# org_tuple6 = tuple(map(int,tuple6.split(",")))


# def find_max_min(tup):
#     max_val = max(tup)
#     min_val = min(tup)

#     return max_val ,min_val

# maximum,minimum = find_max_min(org_tuple6)

# print("Maximum: ",maximum )
# print("Minimum: ",minimum )

# 28


# set1 = {1,2,3,4}
# set2  = {4,5,6,7}



# Intersetion = set()

# difference = set1.difference(set2)

# for i in set1:
#     if i in set2:
#         Intersetion.add(i)


# set1.update(set2)
# union = set1

# print("Union: ", union)
# print("Intersection: ", Intersetion)
# print("difference: ", difference)

# # 29

# tuple3 = tuple(map(int,input("Enter elements of tuple seprated by space:    ").split(",")))
# element = int(input("Enter the element to count:   "))


# count = tuple3.count(element)

# print("Count of element: " ,count)

# #30

# set7 = set(input("Enter first set of string").split(","))
# set8 = set(input("Enter second set of string").split(","))
# result = set7.symmetric_difference(set8)
# print("Symmetric differnence:  ",result)

## 31

# list5 = list(input("Enter words:   ").split(","))
# dict5 = {}

# for i in list5:
#     key = i
#     value=list5.count(i)

#     dict5.update({key:value})

# print(dict5)

# 32

# dict6 = {}
# numbers = int(input("How many items in first dict:   "))

# for i in range(numbers):
#     key = input("Enter Key:   ")
#     value = int(input("Enter value:   "))
#     dict6[key] = value

# dict7 = {}
# numbers1 = int(input("How many items in second dict:    "))
# for i in range(numbers1):
#     key = input("Enter Key:   ")
#     value = int(input("Enter value:   "))
#     dict7[key] = value


# merged_dict = dict6.copy()

# for key,value in dict7.items():
#     if key in merged_dict:
#         merged_dict[key] += value
#     else:
#         merged_dict[key] = value

# print("Merged_dict:  ",merged_dict)

# # 33

# def get_nested_value(d, keys):
#     current = d
#     for key in keys:
#         if key in current:
#             current = current[key]
#         else:
#             return None
#     return current


# nested_dict = {"a": {"b": {"c": 10}}}
# keys = ["a", "b", "c"]
# print(get_nested_value(nested_dict, keys))


#34

def sort_dict(d, descending = False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=descending))

my_dict = {"apple": 5, "banana": 2, "orange": 7}

print("Ascending:", sort_dict(my_dict))
print("Descending:", sort_dict(my_dict, descending=True))

#35

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted


my_dict = {"a": 1, "b": 2, "c": 1}
print(invert_dict(my_dict)) 

