import datetime

while True:
    kullanıcı=[]
    Ad=input("Adınızı Giriniz:")
    Soyad=input("Soaydınızı Giriniz:")
    Dogum_gunu=input("Doğum yılınızı Giriniz:")
    bugunun_tarihi=datetime.date.today()
    yas=bugunun_tarihi.year - int(Dogum_gunu)
    kullancıdict={"Ad": Ad,
                  "Soyad": Soyad,
                  "Doğum günü":Dogum_gunu,
                  "Yaş":yas}
    kullanıcı.append(kullancıdict)
    print(kullanıcı)

   
    




































