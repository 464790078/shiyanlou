#!/usr/bin/env python3
x = float(input("Plesase input your number: "))
n = term = result = 1
while n < 100:
    term *= x/n
    result += term
    n += 1
    if term < 0.0001:
        break
print("No of Times is {} and result if {}".format(n,result))
