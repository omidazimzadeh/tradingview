import os
import pandas as pd
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import mysql.connector as myssql

def mysql(listed):
    try: 
        mydb = myssql.connect(
            host="localhost",
            user="root",
            password="admin",
            database="tradingview"
        )

        mycursor = mydb.cursor(buffered=True)# buffer is true nabashe misheUnread result found

        mycursor.execute("SHOW TABLES")
        name = 'omidd'
        for table in mycursor:
            if name in table:
                
                price = listed[0]
                print(price)
                price1= listed[1]
                print(price1)
                val = (price,price1)
                mycursor.execute("INSERT INTO omidd (idomid,omidcol)  VALUES (%s,%s)", val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                break
    except (myssql.Error, myssql.Warning) as e:
        print(e)
        return None

def main():

    FireFoxDriverPath = Service(os.path.join(os.getcwd(), 'Driver', 'geckodriver.exe'))
    browser = webdriver.Firefox(service=FireFoxDriverPath)
    browser.implicitly_wait(7)

    url = "https://www.tradingview.com/markets/currencies/rates-all/"
    browser.get(url)

    find=browser.find_element(By.XPATH,'//*[@id="js-screener-container"]/div[4]/table/tbody/tr[2]/td[2]/span')
    prices=[]
    while(True):

        prices=[]
        symbols = ["CADAED","AEDAUD"]
        for symbol in symbols:
            search=browser.find_element(By.XPATH,
            '//*[@id="js-screener-container"]/div[3]/table/thead/tr/th[1]/div/div/div[3]/input')
            search.send_keys(symbol)
            time.sleep(4)
            find=browser.find_element(By.XPATH,
            '//*[@id="js-screener-container"]/div[4]/table/tbody/tr/td[2]/span').text
            print(find)
            prices.append(find)
            browser.find_element(By.XPATH,
            '//*[@id="js-screener-container"]/div[3]/table/thead/tr/th[1]/div/div/div[3]/input').clear()
            time.sleep(5)
        mysql(prices)
        time.sleep(5)
        prices.clear()

if __name__ == '__main__' :
    main()