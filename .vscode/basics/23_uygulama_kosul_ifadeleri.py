
#UYGULAMA-1

# sayi = int(input ("sayı giriniz: "))                #kulllanıcıdan veri almak istediğimizde input fonksiyonunun kullanırız 

# if (sayi > 0):
#     if (sayi % 2 == 1):
#         print("girilen sayı pozitif tek sayıdır.")
#     else:
#         print("girilen sayı pozitif fakat tek değil")
# else:
#     print("girilen sayı negatiftir.")


#UYGULAMA-2

# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))       

# if (x>y) and (x>z):
#     print("x en büyük")
# elif (y>x) and (y>z):
#     print("y en büyük")
# elif (z>x) and (z>y): 
#     print("z en büyük sayı")
          
#UYGULAMA-3

isim = input("isim : ")
yaş = int(input("yaş : "))
egitim = input("eğitim : ")

if (yaş >= 18):
    if (egitim == "lise") or (egitim == "universite"):
        print("ehliyet alabilirsniz")
    else:
        print(f'{isim} ehliyet alamazsınız çünkü eğtim durumunuz yetersiz.')
else:
    print(f'{isim} ehliyet alamzsınız çünkü yaşınız tutmuyor.')
