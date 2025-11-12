#sum of first n natural number
n = int(input("enter the number"))
if num < 0:
  print("enter a number")
else: 
  sum_number = 0
  counter = 1
  while counter <= num:
    sum_number += counter
    counter += 1
print("the sum is",sum_number)
