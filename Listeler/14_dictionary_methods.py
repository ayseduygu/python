arabaAudi ={
    "marka" : "Audi",
    "model" : "A5",
    "yil" : 2019,
}

# DEĞERLERE ERİŞME
# sonuc = arabaAudi["marka"]
# sonuc = arabaAudi.get("marka")
# 

# SORGULAMA İŞLEMİ 
# sonuc = "marka" in arabaAudi
# sonuc = len(arabaAudi)
# print(sonuc)


# EKLEME İŞLEMİ

# arabaAudi["renk"]= "siyah"
# print(arabaAudi)

# SİLME İŞLEMİ  

#arabaAudi.pop("yil")
# print(arabaAudi)

#arabaAudi.popitem() #son elemanı siliyor 

#del arabaAudi["marka"]   

#del arabaAudi #obje olduğu gibi siliniyor


#arabaAudi.clear()  # obje duruyor içindekiler siliniyor


  #OBJEYİ KULLANMAK

# araba = arabaAudi.copy()
# araba["marka"]= "mersedes"



  # DEĞER GÜNCELLEME
# arabaAudi.update({
#     "marka":"BMV",
#     "renk":"beyaz"
# })


print(arabaAudi)

