'''
Author: MJ.XU
Date: 2022-07-18 17:29:14
LastEditTime: 2022-09-29 17:36:57
LastEditors: MJ.XU
Description: 
Personal URL: https://macuxavier.github.io/
'''

import csv
from ctypes import *
from numbers import Number

with open('a.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        # print(type(row))
        numbers = [int(x, 16) for x in row]
        # numbers = ['0x{:02X}'.format(int(x, 16)) for x in row]
        # numbers = [int(x, 16) for x in row]
        # numbers_c=(c_ubyte *1)(numbers[1])
        # str1 = '0x{:02X}'.format(numbers[0])
        # myinput_1 = hex(numbers)
        print(numbers)  # type of row: list
        # print(str1)
