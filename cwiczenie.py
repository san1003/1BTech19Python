# x = int(input())
# suma = 0
# while x > 0:
#   cyfra = x % 10 
#   suma = cyfra + suma
#   x = x // 10
# print(suma)  

a = int(input())
for i in range(2,a):
  if a % i == 0:
    print("nie")
    exit(0)
print("tak")

