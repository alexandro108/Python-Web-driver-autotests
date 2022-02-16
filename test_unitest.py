import unittest
from selenium import webdriver
import time
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        

        link = " http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Код, который заполняет обязательные поля
    
        input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")
    
        input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        input2.send_keys("Ivanov")
    
        input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
        input3.send_keys("Ivanovich")
    
    # Отправляется заполненная форма
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    
        
    def test_abs2(self):
        

        link = " http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Код, который заполняет обязательные поля
    
        input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")
    
        input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        input2.send_keys("Ivanov")
    
        input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
        input3.send_keys("Ivanovich")
    
    # Отправляется заполненная форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    # Проверяю, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text)
        
if __name__ == "__main__":
    unittest.main()
