# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 06:47:24 2020

@author: ms101
"""

if __name__ == "__main__":

    birthdays = {"Leonardo da Vinci": "15.04.1452",
                 "Galileo Galilei": "15.02.1564",
                 "Stephen Hawking":"08.01.1942" }
    
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    for name in birthdays.keys():
        print(name)
    lookup = "y"
    while lookup == "y":
        query = input("Who's birthday do you want to look up?")
        try: 
            print("{}'s birthday is {}".format(query,birthdays[query]))
            lookup = input("Do you want to look up another name?(y/n)")
        except KeyError:
            print("We don't know the birthday of that Person, sorry")
            lookup = input("Do you want to look up another name?(y/n)")