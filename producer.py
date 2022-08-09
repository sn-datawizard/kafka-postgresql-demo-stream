from kafka import KafkaProducer
from time import sleep
from json import dumps
import pandas as pd

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: dumps(x).encode('utf-8'))


while True:   
    df = pd.read_csv('./data.csv', sep=';', index_col=False)
    for index, row in df.iterrows():
        df_dict = pd.DataFrame.to_dict(df, orient='records')   
        producer.send('testvalue', df_dict[index])    
        del df_dict[index]['Country']
        del df_dict[index]['Item Type']
        del df_dict[index]['UnitsSold']        
        print('Message send & dict reset completed..')
        sleep(5)

producer.flush()
