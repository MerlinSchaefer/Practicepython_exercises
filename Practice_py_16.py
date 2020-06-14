# -*- coding: utf-8 -*-
"""
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password.
 Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. 
For weak passwords, pick a word or two from a list.
"""
import random 
import string

strength = input("Do you wish to generate a strong or a weak password? (strong/weak)").lower()
weak_pw = ["flower","book", "password","football","headphones","bottle","brain","paper"]

char = string.ascii_letters + string.digits + string.punctuation

if strength == "weak":
    pw = random.choice(weak_pw)
    print(pw)
else:
    pw = "".join(random.sample(char,random.randint(8,25))) 
    print(pw)
    
