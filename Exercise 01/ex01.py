"""
Albert Garrow
PHY 280 - Winter 2020

Exercise 01
"""

import statistics

major = "Physics Research"
tacosRating = 8             #9 with sour cream
sleepRating = 11
data = [tacosRating, sleepRating]
ratingsAverage = statistics.mean(data)

print(major)
print(tacosRating)
print(sleepRating)

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
full_name = first_name + " " + last_name

print("first_name: " + str(type(first_name)))
print("last_name: " + str(type(last_name)))
print("full_name: " + str(type(full_name)))

print("My name is " + full_name + " and I give tacos a score of " + str(tacosRating) + " out of 10!") #turns out you concatenate an int in Python
print("My name is " + full_name + " and my sleeping enjoyment rating is " + str(sleepRating) + " / 10!")
print("Based on the factors above, my happiness rating is " + str(ratingsAverage) + " out of 10, or " + str(ratingsAverage*10) + "%!") 