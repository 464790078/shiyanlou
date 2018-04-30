#!/usr/bin/env python3
days = int(input("Enter days: "))
months = days // 30
days = days % 30
print("Months = {} Days= {}".format(months,days))
numbers = int(input("please input your number:"))
if numbers <= 100:
    print("your number is smaller than 100")
else:
    print("your number is bigger than 100")
