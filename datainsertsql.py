import psycopg2 as pg   #პოსტგრესთან სამუშაო ბიბლიოთეკა
import os 

create_table_query = '''CREATE TABLE IF NOT EXISTS roulette
                        (id BIGSERIAL PRIMARY KEY NOT NULL,
                         number INT NOT NULL,
                         color VARCHAR(10),
                         odd_even VARCHAR(4),
                         low_high VARCHAR(5),
                         col VARCHAR(20),
                         sector VARCHAR(20));  
                      '''

insert_query = """ INSERT INTO roulette (number, color, odd_even, low_high, col, sector)
                   VALUES (%s,%s,%s,%s,%s,%s);"""


fetch_query = ''' SELECT * FROM  roulette;'''

fetch_last = ''' SELECT * FROM  roulette ORDER BY id DESC LIMIT %s;'''







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

#############################################################################
def create_table_if_not_exists():                              #  შექმნის თეიბლს ცხრილში, თუ არ არსებობს
    conn = get_conn()                                         #   გამოიძახებს ზედა ფუნქციას get_conn და შექმნის კავშირს ბაზასთან
    cursor = conn.cursor()                                   #
    try:                                                    #
        cursor.execute(create_table_query)      #   sql_access.py ფაილში აღწერილი მონაცემების მიხედვით შექმნის ბაზას
        conn.commit()                                     #
    finally:                                             #
        conn.close()                                    #
        cursor.close()                                 #
#####################################################################################





def get_all():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(fetch_query)
        data = cursor.fetchall()
        return map_to_view(data)
    finally:
        conn.close()
        cursor.close()

def get_last(count):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(fetch_last, str(count))
        data = cursor.fetchall()
        return map_to_view(data)
    finally:
        conn.close()
        cursor.close()

def insert(dict):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(insert_query, [dict['number'], dict['color'], dict['odd_even'], dict['low_high'], dict['col'], dict['sector']])
        conn.commit()
    finally:
        conn.close()
        cursor.close()



def map_to_view(db_set):
    data = []
    for i in db_set:
        data.append({
            "number" :   i[1],
            "color" :    i[2],
            "odd_even" : i[3],
            "low_high" : i[4],
            "col" :      i[5],
            "sector" :   i[6]
        })
    return data




###############################################
create_table_if_not_exists()  #თეიბლს შექმნის თუ არ არსებობს 1ხელ გამოიძახებ პროგრამის დასაწყისში და მეტგან არაა საჭირო

"""
insert({                      #insert() dictionary-ს იღებს პარამეტრად და აინსერტებს  
    "number" : 0,
    "color" : " ",
    "odd_even" : " ",
    "low_high" : " ",
    "col" : " ",
    "sector" :  " "
})
"""

alldata = get_all()           #ყველა მონაცემის ლისტს აბრუნებს რაც წერია ბაზაში
lastFive = get_last(5)        #ბოლო დამატებულებს აბრუნებს მაგ: get_last(5)- ბოლო ჩამატებულ 5ს, get_last(10)- ბოლო ჩამატებულ 10-ს

#print(alldata)
print(lastFive)

