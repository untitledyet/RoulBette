import psycopg2 as pg
############################     SQL - Connect         ####################################################
create_bets_history_table_query = '''CREATE TABLE IF NOT EXISTS bets_history
                        (id BIGSERIAL PRIMARY KEY NOT NULL,
                         number INT NOT NULL,
                         red VARCHAR(10),
                         black VARCHAR(10),
                         odd VARCHAR(10),
                         even VARCHAR(10),
                         low VARCHAR(10),
                         high VARCHAR(10),
                         col1 VARCHAR(20),
                         col2 VARCHAR(20),
                         col3 VARCHAR(20),
                         sector1 VARCHAR(20),
                         sector2 VARCHAR(20),
                         sector3 VARCHAR(20));  
                      '''



insert_bets_query= """ INSERT INTO bets_history (number, red, black, odd, even, low, high, col1, col2, col3, sector1, sector2, sector3)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
################################################################################

check_number = []
check_colors = []
check_odd_even = []
check_low_high = []
check_line = []
check_sector = []



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




def create_bets_history_table_if_not_exists():                              #  შექმნის თეიბლს ცხრილში, თუ არ არსებობს
    conn = get_conn()                                         #   გამოიძახებს ზედა ფუნქციას get_conn და შექმნის კავშირს ბაზასთან
    cursor = conn.cursor()                                   #
    try:                                                    #
        cursor.execute(create_bets_history_table_query)      #   ფაილში აღწერილი მონაცემების მიხედვით შექმნის ბაზას
        conn.commit()                                     #
    finally:                                             #
        conn.close()                                    #
        cursor.close()     




def insert_bets(bets_dict):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(insert_bets_query, [bets_dict['number'], bets_dict['red'], bets_dict['black'], bets_dict['odd'], bets_dict['even'], bets_dict['low'], bets_dict['high'],  bets_dict['col1'],  bets_dict['col2'],  bets_dict['col3'],  bets_dict['sec1'],  bets_dict['sec2'], bets_dict['sec3']])
        conn.commit()
    finally:
        conn.close()
        cursor.close()



create_bets_history_table_if_not_exists()



droebiti_cvladi = {
    "number" : 0,
    "red":0,
    "black":0,
    "odd":0,
    "even":0,
    "low":0,
    "high":0,
    "col1":0,
    "col2":0,
    "col3":0,
    "sec1":0,
    "sec2":0,
    "sec3":0

}


#############################################################################################################################################

try:
   connection = pg.connect(user="postgres",
                                  password="B00bsmakemesm1le",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Roulette")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from roulette"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from links table using cursor.fetchall")
   mobile_records = cursor.fetchall() 
   
   

   print("Print each row and it's columns values")
   for row in mobile_records[:-27:-1]:
       check_number.append(row[1])
       check_colors.append(row[2])
       check_odd_even.append(row[3])
       check_low_high.append(row[4])
       check_line.append(row[5])
       check_sector.append(row[6])

except (Exception, pg.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


droebiti_cvladi["number"]= check_number[0]




x3_bets = {
    "x3_bet10":-1.0,
    "x3_bet11":-2.0,
    "x3_bet12":-3.0,
    "x3_bet13":-4.0
}

x2_bets = {
    "x2_bet10":-1.0,
    "x2_bet11":-2.0,
    "x2_bet12":-4.0,
    "x2_bet13":-8.0
}



def check_red(check_color):
    global droebiti_cvladi
    for i in range (10, len(check_color)):
        try: 
            if check_color[0] == "red" and "red" not in check_color[1:i+1] and check_color[i+1]=="red":
                droebiti_cvladi["red"] = round(float(x2_bets["x2_bet"+str(i)])*(-2), 2)
            elif "red" not in check_color[0:i] and check_color[i]=="red":
                    droebiti_cvladi["red"]= x2_bets["x2_bet"+str(i)]
        except: 
            if "red" not in check_color[0:i] and check_color[i]=="red":
                    droebiti_cvladi["red"]= x2_bets["x2_bet"+str(i)]
                    print ("dade fsoni red", i+1)


def check_black(check_color):
    global droebiti_cvladi
    for i in range (10, len(check_color)):
        try: 
            if check_color[0] == "black" and "black" not in check_color[1:i+1] and check_color[i+1]=="black":
                 droebiti_cvladi["black"] = round(float(x2_bets["x2_bet"+str(i)])*(-2), 2)
            elif "black" not in check_color[0:i] and check_color[i]=="black":
                    droebiti_cvladi["black"]= x2_bets["x2_bet"+str(i)]
        except: 
            if "black" not in check_color[0:i] and check_color[i]=="black":
                    droebiti_cvladi["black"]= x2_bets["x2_bet"+str(i)]
                    print ("dade fsoni black", i+1)

def check_odd(check_odd_even):
    global droebiti_cvladi
    for i in range (10, len(check_odd_even)):
        try: 
            if check_odd_even[0] == "odd" and "odd" not in check_odd_even[1:i+1] and check_odd_even[i+1]=="odd":
                droebiti_cvladi["odd"] = round(float(x2_bets["x2_bet"+str(i)])*(-2), 2)
            elif "odd" not in check_odd_even[0:i] and check_odd_even[i]=="odd":
                    droebiti_cvladi["odd"]= x2_bets["x2_bet"+str(i)]
        except:
            if "odd" not in check_odd_even[0:i] and check_odd_even[i]=="odd":
                    droebiti_cvladi["odd"]= x2_bets["x2_bet"+str(i)]
                    print ("dade fsoni odd", i+1)

def check_even(check_odd_even):
    global droebiti_cvladi
    for i in range (10, len(check_odd_even)):
        try:
            if check_odd_even[0] == "even" and "even" not in check_odd_even[1:i+1] and check_odd_even[i+1]=="even":
                droebiti_cvladi["even"] = round(float(x2_bets["x2_bet"+str(i)])*(-2), 2)
            elif "even" not in check_odd_even[0:i] and check_odd_even[i]=="even":
                    droebiti_cvladi["even"]= x2_bets["x2_bet"+str(i)]
        except:
            if "even" not in check_odd_even[0:i] and check_odd_even[i]=="even":
                    droebiti_cvladi["even"]= x2_bets["x2_bet"+str(i)]
                    print ("dade fsoni even", i+1)
        
def check_low(check_low_high):
    global droebiti_cvladi
    for i in range (10, len(check_low_high)):
        try:
            if check_low_high[0] == "1/18" and "1/18" not in check_low_high[1:i+1] and check_low_high[i+1] == "1/18":
                droebiti_cvladi["low"] = round(float(x2_bets["x2_bet"+str(i)])*(-2), 2)
            elif "1/18" not in check_low_high[0:i] and check_low_high[i]=="1/18":
                    droebiti_cvladi["low"]= x2_bets["x2_bet"+str(i)]
        except:
            if "1/18" not in check_low_high[0:i] and check_low_high[i]=="1/18":
                    droebiti_cvladi["low"]= x2_bets["x2_bet"+str(i)]
                    print ("dade fsoni low", i+1)
        
def check_high(check_low_high):
    global droebiti_cvladi
    for i in range (10, len(check_low_high)):
        try:
            if check_low_high[0] == "19/36" and "19/36" not in check_low_high[1:i+1] and check_low_high[i+1] == "19/36":
                droebiti_cvladi["high"] = round(float(x2_bets["x2_bet"+str(i)])*(-2), 2)
            elif "19/36" not in check_low_high[0:i] and check_low_high[i]=="19/36":
                    droebiti_cvladi["high"]= x2_bets["x2_bet"+str(i)]
        except:
            if "19/36" not in check_low_high[0:i] and check_low_high[i]=="19/36":
                    droebiti_cvladi["high"]= x2_bets["x2_bet"+str(i)]
                    print ("dade fsoni high", i+1)


def check_col1 (check_line):
    global droebiti_cvladi
    for i in range (10, len(check_line)):
        try:
            if check_line[0] == "line1" and "line1" not in check_line[1:i+1] and check_line[i+1] == "line1":
                droebiti_cvladi["col1"] = round(float(x3_bets["x3_bet"+str(i)])*(-3), 2)
            elif "line1" not in check_line[0:i] and check_line[i]=="line1":
                    droebiti_cvladi["col1"]= x3_bets["x3_bet"+str(i)]
        except:
            if "line1" not in check_line[0:i] and check_line[i]=="line1":
                    droebiti_cvladi["col1"]= x3_bets["x3_bet"+str(i)]
                    print ("dade fsoni col1", i+1)

def check_col2 (check_line):
    global droebiti_cvladi
    for i in range (10, len(check_line)):
        try:
            if check_line[0] == "line2" and "line2" not in check_line[1:i+1] and check_line[i+1] == "line2":
                droebiti_cvladi["col2"] = round(float(x3_bets["x3_bet"+str(i)])*(-3), 2)
            elif "line2" not in check_line[0:i] and check_line[i]=="line":
                    droebiti_cvladi["col2"]= x3_bets["x3_bet"+str(i)]
        except:
            if "line2" not in check_line[0:i] and check_line[i]=="line2":
                    droebiti_cvladi["col2"]= x3_bets["x3_bet"+str(i)]
                    print ("dade fsoni col2", i+1)


def check_col3 (check_line):
    global droebiti_cvladi
    for i in range (10, len(check_line)):
        try:
            if check_line[0] == "line3" and "line3" not in check_line[1:i+1] and check_line[i+1] == "line3":
                droebiti_cvladi["col3"] = round(float(x3_bets["x3_bet"+str(i)])*(-3), 2)
            elif "line3" not in check_line[0:i] and check_line[i]=="line3":
                    droebiti_cvladi["col3"]= x3_bets["x3_bet"+str(i)]
            
        except:
            if "line3" not in check_line[0:i] and check_line[i]=="line3":
                    droebiti_cvladi["col3"]= x3_bets["x3_bet"+str(i)]
                    print ("dade fsoni col3", i+1)



def check_sector1(check_sector):
    global droebiti_cvladi
    for i in range (10, len(check_sector)):
        try:
            if check_sector[0] == "sector1" and "sector1" not in check_sector[1:i+1] and check_sector[i+1]== "sector1":
                droebiti_cvladi["sec1"] = round(float(x3_bets["x3_bet"+str(i)])*(-3), 2)
            elif "sector1" not in check_sector[0:i] and check_sector[i] == "sector1":
                droebiti_cvladi["sec1"]= x3_bets["x3_bet"+str(i)]
        except:
            if "sector1" not in check_sector[0:i] and check_sector[i] == "sector1":
                droebiti_cvladi["sec1"]= x3_bets["x3_bet"+str(i)]
                print ("dade fsoni sector1", i+1)

def check_sector2(check_sector):
    global droebiti_cvladi
    for i in range (10, len(check_sector)):
        try:
            if check_sector[0] == "sector2" and "sector2" not in check_sector[1:i+1] and check_sector[i+1] == "sector2":
                droebiti_cvladi["sec2"] = round(float(x3_bets["x3_bet"+str(i)])*(-3), 2)
            elif "sector2" not in check_sector[0:i] and check_sector[i] == "sector2":
                droebiti_cvladi["sec2"]= x3_bets["x3_bet"+str(i)]
        except:
            if "sector2" not in check_sector[0:i] and check_sector[i] == "sector2":
                droebiti_cvladi["sec2"]= x3_bets["x3_bet"+str(i)]
                print ("dade fsoni sector2", i+1)

def check_sector3(check_sector):
    global droebiti_cvladi
    for i in range (10, len(check_sector)):
        try:
            if check_sector[0] == "sector3" and "sector3" not in check_sector[1:i+1] and check_sector[i+1]== "sector3":   ###########3wz
                droebiti_cvladi["sec3"] = round(float(x3_bets["x3_bet"+str(i)])*(-3), 2)
            elif "sector3" not in check_sector[0:i] and check_sector[i] == "sector3":
                droebiti_cvladi["sec3"]= x3_bets["x3_bet"+str(i)]
        except:
            if "sector3" not in check_sector[0:i] and check_sector[i] == "sector3":
                droebiti_cvladi["sec3"]= x3_bets["x3_bet"+str(i)]
                print ("dade fsoni sector3", i+1)



print (check_red(check_colors))
print (check_black(check_colors))
print (check_odd(check_odd_even))
print (check_even(check_odd_even))
print (check_low(check_low_high))
print (check_high(check_low_high))
print (check_col1(check_line))
print (check_col2(check_line))
print (check_col3(check_line))
print (check_sector1(check_sector))
print (check_sector2(check_sector))
print (check_sector3(check_sector))

insert_bets(droebiti_cvladi)



print (check_colors)
print (check_odd_even)
print (check_low_high)
print (check_line)
print (check_sector)



print (droebiti_cvladi)


