# #zadanie 1
# a=int(input())
# b=int(input())
# c=int(input())

# #arytmetyczny 
# if b - a == c - b: print("Jest arytmetyczny")
  
# #geometryczne
# if b / a == c / b: print("Jest geometryczny")  
# #rosnący
# if a < b < c: print("Jest rosnący")
  
# #malejący
# if a > b > c: print("jest malejący")

    
  




#zadanie 2
# suma=0
# for i in range(100,999):
#  if i % 8 == 0 and i % 16 != 0:
#     suma += i
# print(suma)

#zadanie 3
# for i in range(99,9,-1):
#   if i % 7 == 0:
#     wielok=i
#     break
# ilość=0
# for i in range(1000,10000):
#   if wielok == 0:
#     ilość=ilość+1

#zadanie 4
# ilosc= 0
# for i in range(10,100):
#   cd = i // 10
#   cj = i % 10
#   if cd >= 2*cj:
#     ilosc += 1
# print(ilosc)


#zadanie 5
ilosc= 0
suma= 0
for i in range(10,100):
  cs = i //100
  cd = (i%100)// 10
  cj = i % 10
  if cd >= 2*cj:
    ilosc += 1
print(ilosc)

  