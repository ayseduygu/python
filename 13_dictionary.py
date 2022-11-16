# 34 = İstanbul
# 35 = İzmir

# sehirler = ["İstanbul","İzmir"]
# plakalar =[34,35]


# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

# print(plakalar[sehirler.index("İstanbul")])
# print(plakalar[sehirler.index("İzmir")])

# key - value
 
# plakalar = {"İzmir": 35,"İstanbul":34}

# print(plakalar["İzmir"])
# print(plakalar["İstanbul"])

# plakalar["Eskişehir"] = 26
# plakalar["Bursa"] = 16
# print(plakalar)


urunler={
    100:{
        "urunadi": "Monitör",
        "urunaciklamasi": "16 inç",
        "garantiSuresi": 3,
        "fiyat" :[800,944]
    },
    101:{
        "urunadi": "SSD",
        "urunaciklamasi": "256 GB",
        "garantiSuresi": 2,
        "fiyat" :[1500,1770]
    }
}

sonuc = urunler[100]["fiyat"]

tutar = urunler[100]["fiyat"][1] + urunler[101]["fiyat"][1]
print(tutar)

