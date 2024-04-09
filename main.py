# Convert string representation of List to List in Python

from ast import literal_eval

my_str = '[1,2,3,4]'

# ✅ convert string representation of list to list (ast.literal_eval())

my_list = literal_eval(my_str)
print(my_list)  # 👉️ [1, 2, 3, 4]
print(type(my_list))  # 👉️ <class 'list'>
