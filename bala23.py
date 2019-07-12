abc=int(input())
for i in range(2,abc):
    if(abc%i==0):
        print("no")
        break
else:
    print("yes")
