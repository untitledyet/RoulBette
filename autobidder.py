import psycopg2 as pg
import time

fetch_last_row = ''' SELECT * FROM  bets_history ORDER BY id DESC LIMIT %s;'''


port = 5432
dbname = 'Roulette'
host = '127.0.0.1'
username = 'postgres'
password = 'B00bsmakemesm1le'

###########################################################
def get_conn():                                          #
        return pg.connect(database = dbname,            #     ბაზასთან დასაქონექთებელი მონაცემები 
                          host=host,                   #        
                          user = username,            #
                          password = password,       #
                          port = port               #
                )                                  #
#####################################################################################

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
            "number" :   float(i[1]),
            "red" :      float(i[2]),
            "black" :    float(i[3]),
            "odd" :      float(i[4]),
            "even" :     float(i[5]),
            "low" :      float(i[6]),
            "high" :     float(i[7]),
            "col1":      float(i[8]),
            "col2":      float(i[9]),
            "col3":      float(i[10]),
            "sec1":      float(i[11]),
            "sec2":      float(i[12]),
            "sec3":      float(i[13])


        })
    return data


droebiti_cvladi = (get_last(1)[0])
print (droebiti_cvladi)

jamuri_fsoni = 0
dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)


 
if droebiti_cvladi["red"] < 0:
    jamuri_fsoni += droebiti_cvladi["red"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[46]").click()
            print ("red_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
            
        except: 
            pass


if droebiti_cvladi["black"] < 0:
    jamuri_fsoni += droebiti_cvladi["black"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[47]").click()
            print ("black_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
            
        except: 
            pass


if droebiti_cvladi["odd"] < 0:
    jamuri_fsoni += droebiti_cvladi["odd"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[48]").click()
            print ("odd_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
            
        except: 
            pass


if droebiti_cvladi["even"] < 0:
    jamuri_fsoni += droebiti_cvladi["even"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[45]").click()
            print ("even_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
            
        except: 
            pass





if droebiti_cvladi["low"] < 0:
    jamuri_fsoni += droebiti_cvladi["low"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[44]").click()
            print ("low_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
            
        except: 
            pass



if droebiti_cvladi["high"] < 0:
    jamuri_fsoni += droebiti_cvladi["high"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[49]").click()
            print ("high_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
            
        except: 
            pass





if droebiti_cvladi["col1"] < 0:
    jamuri_fsoni += droebiti_cvladi["col1"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[38]").click()
            print ("col1_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
            
        except: 
            pass


if droebiti_cvladi["col2"] < 0:
    jamuri_fsoni += droebiti_cvladi["col2"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[39]").click()
            print ("col2_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
            
        except: 
            pass



if droebiti_cvladi["col3"] < 0:
    jamuri_fsoni += droebiti_cvladi["col3"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[40]").click()
            print ("col3_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
            
        except: 
            pass




if droebiti_cvladi["sec1"] < 0:
    jamuri_fsoni += droebiti_cvladi["sec1"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[41]").click()
            print ("sec1_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        except: 
            pass



if droebiti_cvladi["sec2"] < 0:
    jamuri_fsoni += droebiti_cvladi["sec2"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[42]").click()
            print ("sec2_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        except: 
            pass


if droebiti_cvladi["sec3"] < 0:
    jamuri_fsoni += droebiti_cvladi["sec3"]*(-1)
    while dadebuli_fsoni < jamuri_fsoni:
        try:
            driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[2]/div[2]/div/div[1]/div[43]").click()
            print ("sec3_ze dadebuli", dadebuli_fsoni)
            print ("jamuri", jamuri_fsoni)
            dadebuli_fsoni = float(driver.find_element_by_xpath("//*[@id='TopLevelEvents']/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/span[2]/span[1]").text)
            time.sleep(0.1)
        except: 
            pass