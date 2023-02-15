# W="AAAAABBCCCCDDDEEEEEEEFGGGH"  #5A2B4C3D7EF3G
# W += " "
# ilosc = 1
# H = ""
# for i in range(len(W)-1):
#   if W[i] == W[i+1]:
#      ilosc += 1
#   else:
#     if ilosc > 1:
#        H += str(ilosc)
#     H += W[i]
#     ilosc = 1
# print(H)

# for i in range(10):
#   print(W[i])



licz1 = int(input())
mia1 = int(input())
licz2 = int(input())
mia2 = int(input())
#nww liczebnikow
# iloczyn mianownikow
wspolny= int(mia1*mia2 / gcd(mia1, mia2))


