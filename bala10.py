m=int(input())
b=m
n=0
while m!=0:
  c=m%10
  n=n*10+c
  m=m//10
if(n==b):
  print("yes")
else:
  print("no")
