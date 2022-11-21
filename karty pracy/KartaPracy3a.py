 
#Zad1
# n = int(pinut())
# for i in range(n):
#   print("*-", end="")

# n = int(input())
# print("*-I"*n)

#Zad2
# n = int(input())
# for i in range(1,n+1):
#   print("*"*i, end="")
#   if i % 2 == 0:
#      print("--", end="")
#   else:
#      print("II", end="")

#Zad3
# n = int(input())
# for i in range(1,n+1):
#   print("*"*i, end="")
#   if i % 2 == 0:
#      print("-", end="")
#   else:
#      print("I", end="")

#Zad7
n = int(input())

for i in range(n):
  for j in range(n):
    if i == 0 or j == 0 or i==n-1 or j==n-1 or (i==n//2 and j==n//2):
      print("*",end="")
    else:
      print("-",end="")
  print()

