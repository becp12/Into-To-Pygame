import pygame
import random

# Exercise 1
# name = input("What's your name: ")
# print("Hello", name)

# Exercise 2
# x = 10
# print(x)

# Exercise 3
# number = int(input("Enter a number: "))
# if number > 10:
#     print("Your number is greater than 10")
# elif number < 10:
#     print("Your number is less than 10")
# else:
#     print("Your number is equal to 10")

# Exercise 4
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Your number is even")
# else:
#     print("Your number is odd")

# Exercise 5
# list = ["dog", "cat", "bird"]
# for item in list:
#     print(item)

# Exericse 6
# list = []
# for x in range(10):
#     list.append(random.randint(0, 10))
# print(list)

# Exercise 7
# list = [20, 13, 17, 4, 99, 24]
# number = int(input("Enter a number: "))
# lessThan = 0
# for x in list:
#     if number > x:
#         lessThan += 1
# print(f"There are {lessThan} numbers in the list that are less than your number")

# Exericse 8
# while True:
#     word = input("Enter a word: ")
#     if word == "stop":
#         break
#     for letter in word:
#         print(letter)
# print("Loop is over")

# Exercise 9
# numList = []
# sum = 0
# while True:
#     number = input("Enter a number: ")
#     numList.append(number)
#     if number == "stop":
#         numList.remove("stop")
#         for num in numList:
#             num = int(num)
#             sum += num
#         print("The average of your numbers is " + str(sum / len(numList)))
#         break

# numList = []

# def take_average():
#     total = 0
#     for num in numList:
#         total += num
#     average = total/len(numList)
#     print(f"The average of the numbers is {average}")

# while True:
#     answer = input("Enter a number (type 'stop' to take the average): ")
#     if answer == "stop":
#         take_average()
#         break
#     else:
#         numList.append(int(answer))