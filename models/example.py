#!/usr/bin/python3

import inspect
# print(inspect.getsource(TestCase))


def my_func(**kwargs):
   print(kwargs)

new_dict = {'name': 'Abia', 'age': 20, 'gender': 'female'}
my_func(**new_dict)

