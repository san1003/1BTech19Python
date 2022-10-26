#Zad 5
a = int(input())
b = int(input())
c = int(input())
if a<b+c and b<c+a and c<b+a:
  print("TAK da się")
else:
 print("NIE da się")