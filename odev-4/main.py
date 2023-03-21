# Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.
# Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.
# Test Caseler
# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class TestCase:
    def test_invalid_login(self): #If username and password are entered blank
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usurnameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        usurnameInput.send_keys("")#If the input value is blank
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Username is required"
        print(f"Test sonucu: {testResult}")

    def password_field(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usurnameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        usurnameInput.send_keys("selenium")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Password is required"
        print(f"Test sonucu: {testResult}")

    def spesipicLogin(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usurnameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        usurnameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"Test sonucu: {testResult}")
    
    def errorIcon(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usurnameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        usurnameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        errorButton=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorButton.click()
        sleep(15)
    
    def login(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usurnameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        usurnameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(10)

    def number_products(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usurnameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        usurnameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        driver.get("https://www.saucedemo.com/inventory.html")
        products=driver.find_element(By.CLASS_NAME,"inventory_list")
        if(len(products) == 6):
            print(f"Toplam Ürün Sayısı Doğru: {products}")
        else:
            print("hatalı ürün sayısı")
        sleep(2)




testcase=TestCase()
testcase.number_products()
while True:
    continue