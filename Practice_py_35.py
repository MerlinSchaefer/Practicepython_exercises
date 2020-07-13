# -*- coding: utf-8 -*-
"""
In the previous exercise we saved information about famous scientists’ names and birthdays to disk.
In this exercise, load that JSON file from disk, extract the months of all the birthdays, 
and count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
"""


import json
from collections import Counter

Monthname = {"01": "January",
	"02": "February",
	"03": "March", 
	"04": "April",
	"05": "May",
	"06": "June",
	"07": "July",
	"08": "August",
	"09": "September",
	"10": "October",
	"11": "November",
	"12": "December"}

with open("birthdays.json","r") as file:
        birthdays = json.load(file)
months = []    
for birthday in birthdays.items():
    months.append(Monthname[birthday[1][3:5]])
months_count = Counter(months)
print(months_count)
