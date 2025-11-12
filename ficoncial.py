num = int(input("enter the number:"))
a, b = 2, 7
for i in range(num):
  print(a,end=" ")
  a, b=b, a+b
