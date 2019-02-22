import mysql.connector

db_name = 'trafficstatscollector'
db_user = 'root'
db_password = ''
db_host = 'localhost'


def init_db():
    conn = mysql.connector.connect(user=db_user, password=db_password,
                                   host=db_host, database=db_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS trafficstats (id int primary key, time text, 
                    protocol text, count int, size int)''')
    cursor.close()
    conn.close()


def add_record(record_time, record_protocol, record_count, record_size):
    conn = mysql.connector.connect(user=db_user, password=db_password,
                                   host=db_host, database=db_name)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO trafficstats(time, protocol, count, size) VALUES(%s, %s, %s, %s)',
                 (record_time, record_protocol, record_count, record_size))
    conn.commit()
    cursor.close()
    conn.close()


def insert_records(records_list):
    list_len = int(len(records_list)/4)
    # print(list_len)
    j = 0
    for i in range(1, list_len+1):
        add_record(records_list[j], records_list[j+1], records_list[j+2], records_list[j+3])
        j = j + 4
