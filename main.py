from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

chrome_driver_path = "C:\Development\chromedriver.exe"
service_path = webdriver.chrome.service.Service(chrome_driver_path)

driver = webdriver.Chrome(service=service_path)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")


def click_cookie(times):
    """clicks the cookie button"""
    for _ in range(times):
        cookie_object = driver.find_element(By.ID, "cookie")
        cookie_object.click()
        time.sleep(0.1)  # Add a small delay after clicking the cookie button


def click_object(n):
    clicker = driver.find_element(By.ID, f"buy{n}")
    clicker.click()


def get_price(n):
    """gets the price of the things in the right-hand panel in the cookie game"""
    text = driver.find_element(By.ID, f"buy{n}").text
    x = text.split("-")
    y = x[1].split("\n")[0].strip()
    if "," in y:
        z = y.split(",")
        number = int(z[0] + z[1])
    else:
        number = int(y)
    return number


list_of_objects = ["Cursor", "Grandma", "Factory", "Mine", "Shipment", "Alchemy lab", "Portal", "Time machine"]

while True:
    click_cookie(random.randint(80, 180))
    time.sleep(0.1)
    money = int(driver.find_element(By.ID, "money").text)

    for object in list_of_objects:
        if money < get_price(object):
            index = list_of_objects.index(object)
            click_object(list_of_objects[index - 1])
            time.sleep(0.1)  # Add a small delay after clicking the object button
            money = int(driver.find_element(By.ID, "money").text)  # Re-locate the money element

# here money is being changed inside for loop as we are purchasing right-hand panel things, so it's giving stale error means
# previous money is no longer valid reassign money
