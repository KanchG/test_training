# declaration of different data types
import ast
import json

str_var = "this is a string"
str_int_var = "1,2,3,4,5,6,7,8,9"
lst_var = [1, "abc", (2, 3, 4), 0.009]
tuple_var = (1, "abc", (2, 3, 4), 0.009)
set_var = set(lst_var)
dict_var = {1: "one", 2: "two", 3: "three"}

# casting data types to one another
# string to list - 2 ways
# ========================

str_lst1 = str_var.split()
# ['this', 'is', 'a', 'string']

str_lst2 = list(str_var)
# ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']

str_lst3 = list(str_var.split())
# ['this', 'is', 'a', 'string']

str_lst4 = list(str_var.strip(" "))
# ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']

# string to tuple - 2 ways
# ==========================
str_tup1 = tuple(map(str, str_int_var.split()))
# ('1,2,3,4,5,6,7,8,9',)

str_tup = tuple(map(str, str_int_var.split(",")))
# ('1', '2', '3', '4', '5', '6', '7', '8', '9')

str_tup2 = tuple(map(int, str_int_var.split(",")))
# (1, 2, 3, 4, 5, 6, 7, 8, 9)

str_tup3 = tuple(str_var.split())
# ('this', 'is', 'a', 'string')

str_tup4 = eval(str_int_var)
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
# SyntaxError: unexpected EOF while parsing - eval(str_var)

# string to set
# =============
str_set1 = set(str_var)
# {'n', 'h', ' ', 'i', 'a', 'r', 's', 'g', 't'}
str_set2 = set(str_int_var)
# {'1', '4', '5', ',', '6', '2', '9', '3', '8', '7'}

# string to dict - 3 ways
# =========================
str_json = '{"one": 1, "two": 2, "three": 3}'
str_dict1 = json.loads(str_json)
# {'one': 1, 'two': 2, 'three': 3}

str_dict2 = ast.literal_eval(str_json)
# {'one': 1, 'two': 2, 'three': 3}

# list to str
# ========================
# manual concat will work too
lst_str = ""
lst_str1 = lst_str.join(str_var)

# list to tuple
# ========================

lst_tup1 = tuple(lst_var)
# (1, 'abc', (2, 3, 4), 0.009)
lst_tup2 = tuple(i for i in lst_var)
# (1, 'abc', (2, 3, 4), 0.009)
lst_tup3 = (*lst_var, )
# (1, 'abc', (2, 3, 4), 0.009)

# list to set
# ========================

lst_set = set(lst_var)
# {1, 0.009, (2, 3, 4), 'abc'}

# list to dict
# ========================
# 2 ways - dict comprehension and zip fuction
var = ["a", 1, "b", 2, "c", 3]
lst_dict1 = {var[i]: var[i+1] for i in range(0, len(var), 2)}
# {'a': 1, 'b': 2, 'c': 3}

var_lst = [["a", 1], ["b", 2], ["c", 3]]
lst_dict3 = dict(var_lst)
# {'a': 1, 'b': 2, 'c': 3}

iter_lst = iter(var)
lst_dict2 = dict(zip(iter_lst, iter_lst))
# {'a': 1, 'b': 2, 'c': 3}

# tuple to str
# ========================
tup_var = ("abc", "def", "ghi")
tup_str = "".join(tup_var)
# abcdefghi

# tuple to list
# ========================

tup_lst = list(tuple_var)
# [1, 'abc', (2, 3, 4), 0.009]

# tuple to set
# ========================

tup_set = set(tuple_var)
# {1, 0.009, (2, 3, 4), 'abc'}

# tuple to dict
# ========================

var = ("a", 1, "b", 2, "c", 3)
tup_dict1 = {var[i]: var[i+1] for i in range(0, len(var), 2)}
# {'a': 1, 'b': 2, 'c': 3}

iter_tup = iter(var)
tup_dict2 = dict(zip(iter_tup, iter_tup))
# {'a': 1, 'b': 2, 'c': 3}

var_tup = (("a", 1), ("b", 2), ("c", 3))
tup_dict3 = dict(var_tup)
# {'a': 1, 'b': 2, 'c': 3}

# set to str
# ========================

set_str = str(set_var)
# print("string:" + set_str)
# string:{1, 0.009, 'abc', (2, 3, 4)}

# set to tuple
# ========================

set_tup = tuple(set_var)
# (1, 0.009, 'abc', (2, 3, 4))

# set to list
# ========================

set_lst = list(set_var)
# ['abc', 1, 0.009, (2, 3, 4)]

# set to dict
# ========================

set_dict = dict.fromkeys(set_var, 0)
# {'abc': 0, 1: 0, 0.009: 0, (2, 3, 4): 0}

# dict to str
# ========================

dict_str = str(dict_var)
# print("string:" + dict_str)
# string:{1: 'one', 2: 'two', 3: 'three'}

# only values
dict_str_values = "".join(dict_var.values())
# onetwothree

# dict to list
# ========================

dict_lst = list(dict_var.values())
# ['one', 'two', 'three']
dict_lst1 = list(dict_var)
# [1, 2, 3]

# dict to tuple
# ========================

dict_tup = tuple(dict_var.values())
# ('one', 'two', 'three')
dict_tup1 = tuple(dict_var)
# (1, 2, 3)

# dict to set
# ========================

dict_set = set(dict_var.values())
# {'two', 'three', 'one'}
dict_set1 = set(dict_var)
# {1, 2, 3}

