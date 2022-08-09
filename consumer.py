from kafka import KafkaConsumer
import json
import psycopg2


consumer = KafkaConsumer('testvalue')

con = psycopg2.connect(database='streamdb', user='admin', password='admin', host='127.0.0.1', port='5432')
cursor = con.cursor()
try:
    cursor.execute("""CREATE TABLE table1 (Country CHAR(50), ItemType CHAR(50), UnitsSold INT)""")
except:
    print('Table already exists')
con.commit()

for message in consumer:
    record = json.loads(message.value)
    country = record['Country']
    itype = record['Item Type']
    usold = record['UnitsSold']

    cursor.execute("""INSERT INTO table1 (Country, ItemType, UnitsSold) VALUES (%(one)s, %(two)s, %(three)s)""", {'one': record['Country'], 'two': record['Item Type'], 'three': record['UnitsSold']})
    con.commit()

con.close()
cursor.close()

