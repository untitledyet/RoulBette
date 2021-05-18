from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import threading
import os
from numdescription import ricxvis_agwera
from datainsertsql import insert
import psycopg2 as pg
import time

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# ქვედა 1 ხაზი ემსახურება ლინკის გახსნას, შემდეგი 3 ავტორიზაციას
driver.get("https://www.adjarabet.com/en/Casino/All/All")
Username = driver.find_element_by_css_selector(
    "body > my-app > adj-item._s_position-top--left-0._cs_z-111._cs_size-w--full > adj-grid > div:nth-child(1) > adj-grid > adj-grid > adj-grid._cs_m-left--auto._cs_position-r > adj-grid > adj-login > div > form > div._css_block--full._css_flex._css_flex--align-start.form_login._cs_scrolledFlex-none.scrolled-hidden > div._cs_flex._cs_position-r._cs_m-right--sm > my-df-formitem > div > input").send_keys(
    "teonateo77")
Password = driver.find_element_by_css_selector(
    "body > my-app > adj-item._s_position-top--left-0._cs_z-111._cs_size-w--full > adj-grid > div:nth-child(1) > adj-grid > adj-grid > adj-grid._cs_m-left--auto._cs_position-r > adj-grid > adj-login > div > form > div._css_block--full._css_flex._css_flex--align-start.form_login._cs_scrolledFlex-none.scrolled-hidden > div:nth-child(2) > my-df-formitem > div > input").send_keys(
    "B00bsmakemesm1le")
LoginButton = driver.find_element_by_css_selector(
    "body > my-app > adj-item._s_position-top--left-0._cs_z-111._cs_size-w--full > adj-grid > div:nth-child(1) > adj-grid > adj-grid > adj-grid._cs_m-left--auto._cs_position-r > adj-grid > adj-login > div > form > div._css_flex._css_margin--left-md > button").click()
time.sleep(1)

# ავტორიზაციის შემდეგ იხსნება რულეტკა

driver.get("https://www.adjarabet.com/en/ingame?id=101680&gameId=6053&pid=73&type=Casino")
time.sleep(2)
driver.switch_to.frame(
    driver.find_element_by_tag_name("iframe"))  # ფოკუსირებას აკეთებს არა მთლიანად გვერდზე, არამედ რულეტკის ფანჯარაზე
time.sleep(2)

# ___________________________________________________________________________________________________________________________________________
fetch_last_row = ''' SELECT * FROM  bets_history ORDER BY id DESC LIMIT %s;'''  # bets_history ს ბოლო ჩანაწერის წამოღება ფსონების დასადებად

port = 5432
dbname = 'Roulette'
host = '127.0.0.1'
username = 'postgres'
password = 'B00bsmakemesm1le'


############################################################################################################
def get_conn():  # #
    return pg.connect(database=dbname,  # ბაზასთან დასაქონექთებელი მონაცემები        #
                      host=host,  # #
                      user=username,  # #
                      password=password,  # #
                      port=port  # #
                      )  # #


####################################################################################################


#####################################################------------------მთავარი ძრავი-----------######################################################

zerobet = 0
LastSpinID = ""


def printit():
    threading.Timer(10.0, printit).start()
    global LastSpinID
    global LastNumber
    global zerobet

    spinID = driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[3]/span[1]/span[2]").text

    if LastSpinID != spinID:
        LastSpinID = spinID
        LastNumber = driver.find_element_by_xpath(
            "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[2]/div[1]/div/div[1]/div").text
        print("bolos amosuli ricxvi", LastNumber)
        insert(ricxvis_agwera("Num" + str(LastNumber)))

        os.system('python logically.py')
        time.sleep(2)

        def get_last(count):
            conn = get_conn()
            cursor = conn.cursor()
            try:
                cursor.execute(fetch_last_row, str(count))
                data = cursor.fetchall()
                return map_to_view(data)
            finally:
                conn.close()
                cursor.close()

        def map_to_view(db_set):
            data = []
            for i in db_set:
                data.append({
                    "number": float(i[1]),
                    "red": float(i[2]),
                    "black": float(i[3]),
                    "odd": float(i[4]),
                    "even": float(i[5]),
                    "low": float(i[6]),
                    "high": float(i[7]),
                    "col1": float(i[8]),
                    "col2": float(i[9]),
                    "col3": float(i[10]),
                    "sec1": float(i[11]),
                    "sec2": float(i[12]),
                    "sec3": float(i[13])

                })
            return data

        droebiti_cvladi = (get_last(1)[0])
        print(droebiti_cvladi)

        jamuri_fsoni = 0
        dadebuli_fsoni = float(driver.find_element_by_xpath(
            "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)

        if droebiti_cvladi["red"] < 0:
            jamuri_fsoni += droebiti_cvladi["red"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[46]").click()
                    print("red_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)

                except:
                    pass

        if droebiti_cvladi["black"] < 0:
            jamuri_fsoni += droebiti_cvladi["black"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[47]").click()
                    print("black_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)

                except:
                    pass

        if droebiti_cvladi["odd"] < 0:
            jamuri_fsoni += droebiti_cvladi["odd"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[48]").click()
                    print("odd_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)

                except:
                    pass

        if droebiti_cvladi["even"] < 0:
            jamuri_fsoni += droebiti_cvladi["even"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[45]").click()
                    print("even_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)

                except:
                    pass

        if droebiti_cvladi["low"] < 0:
            jamuri_fsoni += droebiti_cvladi["low"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[44]").click()
                    print("low_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)

                except:
                    pass

        if droebiti_cvladi["high"] < 0:
            jamuri_fsoni += droebiti_cvladi["high"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[49]").click()
                    print("high_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)

                except:
                    pass

        if droebiti_cvladi["col1"] < 0:
            jamuri_fsoni += droebiti_cvladi["col1"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[38]").click()
                    print("col1_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)

                except:
                    pass

        if droebiti_cvladi["col2"] < 0:
            jamuri_fsoni += droebiti_cvladi["col2"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[39]").click()
                    print("col2_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)

                except:
                    pass

        if droebiti_cvladi["col3"] < 0:
            jamuri_fsoni += droebiti_cvladi["col3"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[40]").click()
                    print("col3_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)

                except:
                    pass

        if droebiti_cvladi["sec1"] < 0:
            jamuri_fsoni += droebiti_cvladi["sec1"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[41]").click()
                    print("sec1_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)
                except:
                    pass

        if droebiti_cvladi["sec2"] < 0:
            jamuri_fsoni += droebiti_cvladi["sec2"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[42]").click()
                    print("sec2_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)
                except:
                    pass

        if droebiti_cvladi["sec3"] < 0:
            jamuri_fsoni += droebiti_cvladi["sec3"] * (-1)
            while dadebuli_fsoni < jamuri_fsoni:
                try:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[43]").click()
                    print("sec3_ze dadebuli", dadebuli_fsoni)
                    print("jamuri", jamuri_fsoni)
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    time.sleep(0.1)
                except:
                    pass

        if jamuri_fsoni == 0:
            zerobet += 1
            if zerobet == 10:
                while dadebuli_fsoni < 0.1:
                    driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[1]").click()
                    dadebuli_fsoni = float(driver.find_element_by_xpath(
                        "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
                    zerobet = 0

        else:
            zerobet = 0


printit()
