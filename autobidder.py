import psycopg2 as pg
import time
from selenium.webdriver.common.by import By

from Adjara import driver
from logically import droebiti_cvladi

fetch_last_row = ''' SELECT * FROM  bets_history ORDER BY id DESC LIMIT %s;'''

port = 5432
dbname = 'Roulette'
host = '127.0.0.1'
username = 'postgres'
password = 'B00bsmakemesm1le'


###########################################################
def get_conn():  #
    return pg.connect(database=dbname,  # ბაზასთან დასაქონექთებელი მონაცემები
                      host=host,  #
                      user=username,  #
                      password=password,  #
                      port=port  #
                      )  #


#####################################################################################

if droebiti_cvladi["red"] < 0:
    jamuri_fsoni += droebiti_cvladi["red"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[46]").click()
            print("red_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["black"] < 0:
    jamuri_fsoni += droebiti_cvladi["black"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[47]").click()
            print("black_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["odd"] < 0:
    jamuri_fsoni += droebiti_cvladi["odd"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[48]").click()
            print("odd_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["even"] < 0:
    jamuri_fsoni += droebiti_cvladi["even"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[45]").click()
            print("even_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["low"] < 0:
    jamuri_fsoni += droebiti_cvladi["low"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[44]").click()
            print("low_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["high"] < 0:
    jamuri_fsoni += droebiti_cvladi["high"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[49]").click()
            print("high_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["col1"] < 0:
    jamuri_fsoni += droebiti_cvladi["col1"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[38]").click()
            print("col1_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["col2"] < 0:
    jamuri_fsoni += droebiti_cvladi["col2"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[39]").click()
            print("col2_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["col3"] < 0:
    jamuri_fsoni += droebiti_cvladi["col3"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[40]").click()
            print("col3_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["sec1"] < 0:
    jamuri_fsoni += droebiti_cvladi["sec1"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[41]").click()
            print("sec1_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["sec2"] < 0:
    jamuri_fsoni += droebiti_cvladi["sec2"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[42]").click()
            print("sec2_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass

if droebiti_cvladi["sec3"] < 0:
    jamuri_fsoni += droebiti_cvladi["sec3"] * (-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[43]").click()
            print("sec3_ze dadebuli", dadebuli_fsoni)
            print("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element(By.XPATH,
                                                       "//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        finally:
            pass
