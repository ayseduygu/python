# And operatör (VE)

# x=15
# sonuc= 10 < x < 20

# sonuc= (x>10) and (x<20)

#True and True => True
#True and False => False 
#False and False => False


# karne_notu = 80
# devamsızlık =12

# sonuc= (karne_notu>=50) and (devamsızlık < 10)

# print(sonuc)



#Or operatörü (VEYA)

#True or True => True
#True or False => True
#False or False => False

# x= 15
# sonuc = (x < 10) or (x & 3 == 0)
# print(sonuc)

#NOT operatörü 

# x = 15
# sonuc =not(x>10) 
# print(sonuc)

karne_notu = 90
devamsızlık =3
ceza_bilgisi = False

sonuc= (karne_notu>=85) and (devamsızlık < 10) and (ceza_bilgisi == False)

print(sonuc)

