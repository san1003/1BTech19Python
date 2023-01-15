#Zad 1
# x=int(input())
# suma=0
# while x > 0:
#   cyfra=x % 10
#   suma = suma + cyfra
#   x = x // 10
# print(suma)  

# 367 % 10 = 7
# 367 // 10 = 36

#Zad2
# a = int(input())

# if a % a==0 and a % 1==0:
#   print("jest liczba pierwsza")
# else:
#   print("nie jest liczba pierwsza")

#Zad3
# a = int(input())
# suma = 0
# for i in range(1,a):
#     if a % i == 0:
#         suma = suma + i
# if suma == a:
#   print("liczba jest doskonala")
# else:
#   print("liczba nie jest doskonala")

#Zad4
# a  = int(input())
# b  = int(input())
# x, y = a, b
# while y > 0:
#      x, y = y , x%y
# if x == 1:
#   print(f"TAK, {x} i {y} są liczbami względnymi pierwszymi")
# else:
#   print(f"NIE, {x} i {y} są liczbami względnymi pierwszymi")

#Zad5
# m =int(input())
# for i in range(10,20):
#   x,y=i,m
# while y > 0:
#       x,y = y,x%y
# if x == 1:
#     print(f" TAK,{i} i {m} są liczbami pierwszymi względnych")
# else:
#     print(f"NIE, {i} i {m} są liczbami pierszymi wzglednych")

#Zad6
