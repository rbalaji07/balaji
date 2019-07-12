p=str(input().casefold())
o=['a','e','o','i','u']
if (p>="a") and (p<="z"):
  if(p in o):
    print("Vowel")
  elif(p not in o):
    print("Consonant")
else:
  print("invalid")
