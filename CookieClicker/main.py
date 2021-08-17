from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
shop_list = ["Cursor", "Grandma", "Factory", "Mine", "Shipment", "Alchemy lab", "Portal", "Time machine"]
shop = []
shop_amount = []
five_min = time.time() + 300


def refresh():
    global shop, shop_amount
    shop = [driver.find_element_by_id(f"buy{name}") for name in shop_list]
    shop_amount = [int(driver.find_element_by_xpath(f'//*[@id="buy{name}"]/b').text.split()[-1].replace(',', ''))
                   for name in shop_list]


refresh()

while True:
    amount = int(driver.find_element_by_id("money").text)
    cookie.click()
    for i in range(len(shop)):
        if amount >= shop_amount[i]:
            shop[i].click()
            time.sleep(0.1)  # To prevent selenium exception
            refresh()
            break
    if time.time() > five_min:
        cookies_per_s = driver.find_element_by_id("cps").text
        print(cookies_per_s)
        break

driver.quit()
# cookies per second for 5 minutes: 44.6 cookies
