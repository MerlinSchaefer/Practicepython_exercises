# -*- coding: utf-8 -*-
"""
You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.
"""
import time 

user_num = int(input("Please enter a number between 0-100 that you want the computer to guess: "))

count = 1
arr = list(range(0,101))
low = 0
high = len(arr)-1

while low <= high: 
  
    mid = (high + low) // 2
  
    # Check if user_num is present at mid 
    if arr[mid] < user_num: 
        low = mid + 1
        count += 1
        print("I guessed {} but that was too low. I will try again!".format(mid))
        time.sleep(1) # sleep for one sec to give more of a feel of "guessing"
    # If user_num is greater, ignore left half of array 
    elif arr[mid] > user_num: 
        high = mid - 1
        count += 1
        print("I guessed {} but that was too high. I will try again!".format(mid))
        time.sleep(1) # sleep for one sec to give more of a feel of "guessing"
    # If user_num is smaller, ignore right half of array
    else: 
        print("I got it! {} is your number. It took me {} guesses!".format(mid,count))
        break
