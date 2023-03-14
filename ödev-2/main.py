#öğrenci kayit otomasyonu


ogrenciler = []

def ogrencibilgisi():
   ad = input("lütfen adınızı giriniz")
   soyad=input("lütfen soyadınızı giriniz")
   if not ad.isalpha() and not soyad.isalpha():
      print("12345")
      return""
   return(ad + " " +soyad)
        
def ogrenciekle():
   ogrenci=ogrencibilgisi()
   if ogrenci == " ":
      print("ogrenci eklenmedi")
   else:
      ogrenciler.append(ogrenci)
      print("öğrenci eklendi")

ogrenciekle()

def cokluogrenci():
   sayi=int(input("eklemek istediğinizi öğrenci sayısını giriniz"))
   for i in range(sayi):
      yeniOgrenciAd=input("yeni öğrenci adını giriniz")
      yeniOgrenciSoyad=input("yeni ogrenci soyadını giriniz")
      if yeniOgrenciAd=="" and yeniOgrenciSoyad=="":
        print("bos deger girdiginiz için öğrenci eklenmedi")
      else:
         ogrenciekle()
cokluogrenci()

def ogrenciYazdir():
   for ogrencitoplam in ogrenciler:
    print(ogrencitoplam)
ogrenciYazdir()


#aynı öğrencileri silme
def ayniogrenciSil():
   name_surname=ogrencibilgisi()
   if name_surname not in ogrenciler:
      print("ogrenci mevcut değil")
      return
   ogrenciler.remove(name_surname)
   print("aynı olan ogrenci silindi")
ayniogrenciSil()
         

#ogrenci numarası öğrenme
def ogrenciNumarasi():
   number=ogrencibilgisi()
   if number not in ogrencibilgisi():
      print("böyle bir öğrenci yok")
   else:
      print(f"Öğrenci numarası : + {str(ogrencibilgisi.index(number))}")
    

#coklu silme
def coklukayitsil():
   i=0
   silmeadedi=int(input("silmek istenilen ogrenci sayisi giriniz"))
   while i<silmeadedi:
      ogrenciler.remove(i)
      i+=1
   return ogrenciler()
   






    
    