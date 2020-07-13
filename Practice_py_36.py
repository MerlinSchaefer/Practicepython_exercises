# -*- coding: utf-8 -*-
"""
In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
"""

import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

# code from previous exercise to get the counts for each month
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

# Plotting
output_file("birthday_hist.html") #setting output file

x = []
y = []
for i,j in months_count.items():
    x.append(i)
    y.append(j)
x_categories = [value for value in Monthname.values()]

p = figure(x_range=x_categories, y_range=(0,max(y)+1))

p.vbar(x=x, top=y, width=0.5, color = "teal")

show(p)