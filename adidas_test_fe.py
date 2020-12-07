from selenium.webdriver import Chrome
from selenium.webdriver.common.alert import Alert

domain = 'https://generator.email/'

def prepare_driver():
    '''Returns a Chrome Webdriver.'''
    driver = Chrome('/Users/zeba/Downloads/chromedriver')
    #Driver Path info is generally available in config file
    return driver

def test_TC1():
    try:
        driver = prepare_driver()
        driver.get("https://www.demoblaze.com/index.html#")

        laptop = driver.find_element_by_link_text("Laptops").click()
        print("Laptop found")
        driver.implicitly_wait(5)
        select_sonyvio = driver.find_element_by_partial_link_text("i5").click()
        print("sonyvio found")
        add_prod_to_cart = driver.find_element_by_xpath('//*[@id="tbodyid"]/div[2]/div/a').click()
        driver.implicitly_wait(5)
        popup = driver.switch_to.alert
        popup.dismiss()

        goback = driver.find_element_by_xpath('//*[@id="navbarExample"]/ul/li[1]/a').click()
        laptop.click()
        select_dell =  driver.find_element_by_xpath('//*[@id="tbodyid"]/div[4]/div/div/h4/a')
        add_prod_to_cart.click()
        popup.accept()

        go_to_cart = driver.find_element_by_xpath('//*[@id="navbarExample"]/ul/li[4]/a').click()

        delete_dell = driver.find_element_by_xpath('//*[@id="tbodyid"]/tr[1]/td[4]/a').click()
        place_order = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div[2]/button').click()

        #fill form
        enter_name = driver.find_element_by_id("name").send_keys("Zeba")
        enter_country = driver.find_element_by_id("country").send_keys("India")
        enter_city = driver.find_element_by_id("city").send_keys("Noida")
        enter_card_details = driver.find_element_by_id("card").send_keys("898787898787")
        enter_month = driver.find_element_by_id("month").send_keys("December")
        enter_year = driver.find_element_by_id("year").send_keys("2020")
        click_purchase = driver.find_element_by_xpath('//*[@id="orderModal"]/div/div/div[3]/button[2]').click()

        #find id and purchase amount
        id = driver.find_element_by_xpath('/html/body/div[10]/p/text()[1]').text
        print(id)
        purchase_amount = driver.find_element_by_xpath('/html/body/div[10]/p/text()[2]').text
        print(purchase_amount)
        ok = driver.find_element_by_xpath('/html/body/div[9]/div[7]/div/button').click()

    except Exception as e:
        print("Test Failed")
    finally:
        if driver:
            driver.quit()

test_TC1()