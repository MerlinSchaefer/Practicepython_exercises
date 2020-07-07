# -*- coding: utf-8 -*-
"""
In the previous exercise we created a dictionary of famous scientists’ birthdays. 
In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file 
on disk, rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, 
and update the JSON file you have on disk with the scientist’s name.
"""


import json
"""
# This code was used to create the .json file

birthdays = {"Leonardo da Vinci": "15.04.1452",
                 "Galileo Galilei": "15.02.1564",
                 "Stephen Hawking":"08.01.1942",
                 "Jane Goodall": "03.04.1934",
                 "Gregor Mendel": "20.06.1822"}

with open("birthdays.json","w") as file:
    json.dump(birthdays,file)
    """
if __name__ == "__main__":   
    with open("birthdays.json","r") as file:
        birthdays = json.load(file)
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    for name in birthdays.keys():
        print(name)
    choice = input("Do you wish to look up a birthday [1] or do you wish to add a name and birthday[2]? (Enter 1 or 2) ")
    if choice == "1":
        lookup = "y"
        while lookup == "y":
            query = input("Who's birthday do you want to look up?")
            try: 
                print("{}'s birthday is {}".format(query,birthdays[query]))
                lookup = input("Do you want to look up another name?(y/n)")
            except KeyError:
                print("We don't know the birthday of that Person, sorry")
                lookup = input("Do you want to look up another name?(y/n)")
    elif choice == "2":
        add = "y"
        while add == "y":
            name = input("Please enter the name to add: ")
            birthday = input("Please enter the birthday of {} ".format(name))
            birthdays[name] = birthday
            add = input("Do you wish to add another name?(y/n) ")
    else:
        print("You can only look up or add a birthday.")
        
    with open("birthdays.json","w") as file:
        json.dump(birthdays,file)