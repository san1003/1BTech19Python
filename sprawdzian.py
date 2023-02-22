n = int(input())
suma_n = 0
liczba = 0
for i in range(2,200):
  if n % i == 0:
    suma_n += 0
for i in range(2,n):
  liczba = liczba != 0
if n - suma_n != liczba:
  print("tak")
else:
  print("nie")