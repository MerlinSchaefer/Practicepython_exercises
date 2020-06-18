# -*- coding: utf-8 -*-
"""
Take the code from the How To Decode A Website exercise , 
and instead of printing the results to a screen, write the results to a txt file. 
In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
"""


import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
filename = (input("Name the file to save to: ") + ".txt")
valid_tags = ['p']
with open (filename,"w") as open_file:
    for tag in soup.findAll("p"):
        if tag.string != None: #get rid of the None appearing
            open_file.write(tag.string)
        
    