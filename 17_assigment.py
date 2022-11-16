

a = 10
b = 20 
c = 30

a,b,c = 10,20,30 


a,b = b,a

print(a,b,c)

# a+= 5     #a = a+5
# print(a,b,c)

# a-= 5     #a = a-5
# print(a,b,c)

# a*= 5     #a = a*5
# print(a,b,c)

# a/= 5     #a = a/5
# print(a,b,c)

# a%= 5     #a = a %5
# print(a,b,c)


# a**= 5    #a = a**5
# print(a,b,c)

# a//=  5    # a= a//5
# print(a,b,c)

sayılar = (1,2,3,4,5,6)

a,b,*c = sayılar
print(a,b,c)
a,*b,c = sayılar
print(a,b,c)
*a,b,c = sayılar
print(a,b,c)


