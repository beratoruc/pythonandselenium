#---HTML---#
HTML (HyperText Markup Language), web sayfalarının yapısını ve içeriğini belirlemek
için kullanılan bir işaretleme dilidir. HTML kodları, web sayfasındaki metin, 
resim, bağlantılar, form elemanları ve diğer öğelerin yerleştirilmesini ve düzenlenmesini sağlar. 
Bu kodlar web tarayıcısı tarafından yorumlanarak sayfanın görüntülenmesini sağlar.


HTML kodları etiketlerden oluşur. 
Etiketler, < > işaretleriyle tanımlanır ve öğelerin başlangıcını ve sonunu belirtir. 
Örneğin, bir başlık etiketi <h1> etiketi ile başlar ve </h1> etiketi ile sona erer.

<!DOCTYPE html> <!-- HTML belgesi olduğunu belirtir -->
<html> <!-- HTML belgesinin başlangıcını belirtir -->
  <head> <!-- HTML belgesinin başlık bölümünü belirtir -->
    <title>Web Sayfa Başlığı</title> <!-- Sayfa başlığını belirtir -->
  </head>
  <body> <!-- HTML belgesinin gövde bölümünü belirtir -->
    <h1>Başlık</h1> <!-- Büyük bir başlık belirtir -->
    <p>Paragraf</p> <!-- Paragraf belirtir -->
    <a href="https://www.google.com">Google</a> <!-- Bağlantı oluşturur -->
    <img src="resim.jpg" alt="Resim Açıklaması"> <!-- Resim ekler -->
    <ul> <!-- Sırasız liste oluşturur -->
      <li>Öğe 1</li> <!-- Liste öğesi -->
      <li>Öğe 2</li>
      <li>Öğe 3</li>
    </ul>
    <ol> <!-- Sıralı liste oluşturur -->
      <li>Öğe 1</li>
      <li>Öğe 2</li>
      <li>Öğe 3</li>
    </ol>
    <form> <!-- Form oluşturur -->
      <input type="text" name="ad" placeholder="Adınız"> <!-- Girdi alanı -->
      <input type="email" name="email" placeholder="E-posta adresiniz">
      <input type="submit" value="Gönder"> <!-- Gönderme butonu -->
    </form>
  </body>
</html> <!-- HTML belgesinin sonunu belirtir -->


#-----HTML Locators------#

HTML Locators, web sayfalarındaki HTML öğelerinin belirlenmesi(class,ıd) için kullanılan yöntemlerdir. 
Web sayfalarında öğeler, genellikle HTML etiketleri ve özellikleri kullanılarak tanımlanır. 
HTML locators, öğeleri tanımlama yöntemleri olarak kullanılır ve web sayfaları test otomasyonu (Selenium), 
işlemlerinde sıklıkla kullanılır.

HTML locators, web sayfasındaki bir öğenin benzersiz olarak tanımlanmasına yardımcı olur. 
Test otomasyon araçları gibi programlar tarafından kullanılabilir, 
böylece doğru öğe veya öğeleri belirleyebilirler. 

#web sayfalarında ogeleri tanımlamak için kullanılan yontemler:
1)ID
2)class
3)Tag Name (<h1>selenium</h1>)
4)Name (<input type="text" name="username">)
5)XAPTH(XPath, bir öğenin konumunu belirlemek için kullanılır.)




#------Selenium Aksiyonlar------#
click(): Bir elementin üzerine tıklama işlemi yapar.
send_keys(): Bir input alanına değer yazmak için kullanılır.
clear(): Bir input alanını temizler.
submit(): Bir formu göndermek için kullanılır.
get(): Bir URL'yi tarayıcıda açmak için kullanılır.
back(): Tarayıcıda bir önceki sayfaya geri dönmek için kullanılır.
forward(): Tarayıcıda bir sonraki sayfaya gitmek için kullanılır.
refresh(): Sayfayı yenilemek için kullanılır.
get_attribute(): Bir elementin belirli bir özelliğini (örneğin, "href" veya "value") almak için kullanılır.
is_displayed(): Bir elementin görüntülenip görüntülenmediğini kontrol etmek için kullanılır.