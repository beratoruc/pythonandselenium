# 1)Python veri türleri 


int, float, complex #sayılar => tam sayı(int), ondalık sayı(float),karmasık sayılar(complex)

list #diziler => degistirebilir bir sıralı veri türüdür. farklı veri tipleri alabilir

tuple #demetler => değiştirilemez bir sıralı veri türüdür. farklı veri tipleri alabilir

set # =>degistirilebilir elemanları sıralı olmayan bir koleksiyon türüdür 

str #string => metinsel elemanlar için kullanılır.

bool #=> true ya da false değerlerini saklar.


# 2) Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

#öncelikle değişkenin adını belirleyip adın sag tarafına atama işlemi kullanarak deger atamamız gerekiyor ( x = 3)

#kamptaki ilerleme durumunu örnek alabiliriz
#ilk önce dersi izlediysek sonraki aşamaya yani ödevlere yönlendirecektir (dersDurum=0)
#ödevler yapıldı mı (true) ise % olarak ilerleyecek, yapılmadıysa (false) % sabit kalacaktır 
#ilk aşama tamamlandıysa %100(int) olarak tamamlandı yazıp diğer bölüme yönlendirilecektir. (ilerleme=100%)


# 3) python sart blokları örneği
kullaniciadi="kodlamaio"
sifre=12345

kAdi=input("kullanıcı adınızı giriniz")
kSifre = int(input("sifre giriniz"))

if(kullaniciadi==kAdi and sifre==kSifre):
    print("kullanıcı adı ve sifrenin dogrudur hosgeldiniz")
else:
    print("hatalı giriş yaptınız")
