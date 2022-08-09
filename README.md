# kafka-postgresql-demo-stream
![image](https://user-images.githubusercontent.com/77932366/183484548-b7c05257-b846-4fd7-8933-5b30dc8e80be.png)

## Introduction
This repository targets junior data engineers/developers who are interested in creating a kafka streaming datapipline for test or practice purposes.

This repository is perfect for developers who are new to kafka and want to explore kafka beyond the basics mentioned here: https://kafka-python.readthedocs.io/en/master/

This repository is a step-by-step documentation on how to develop a streaming data pipeline locally with kafka-python (https://kafka-python.readthedocs.io/en/master/usage.html).

For this demo stream the default kafka docker-compose.yml file is used & extendend by a postgresql database and a WebUI. 

## Prerequisites
- Windows is used for developing
- Python (https://www.python.org/downloads/) | (https://www.python.org/downloads/windows/)
- Docker & docker-compose (https://docs.docker.com/compose/install/)

## Get started
### Set up development environment
Create a project directory & virtual environment with use of the python package 'virtualenv' (https://pypi.org/project/virtualenv/):
```
mkdir kafka
cd kafka

pip install virtualenv
py -m venv kafka_env
.\kafka_env\Scripts\activate

cls
```
After executing all commands the terminal should look similar like this:
```
(kafka_env) C:\Users\Nikesh\kafka>
```

### Validate installation of Docker
Start Docker Desktop on your computer.

Open the terminal and run the command:
```
docker ps
```
If Docker is not installed correctly the following error message will be displayed:
```
'docker' is not recognized as an internal or external command, operable program or batch file.
```
If Docker is installed correctly the following output will be displayed:
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

```

### Install required python packages
```
pip install python-kafka
pip install postgres
pip install psycopg2
```
### Run Docker containers in detached mode
```
docker-compose up -d
```
The output should look like this:
```
Creating network "kafka_default" with the default driver
Creating zookeeper       ... done
Creating pgstreamdb      ... done
Creating pgadminWebUI    ... done
Creating broker          ... done
```
Check if all containers are up and running (use one of the commands below):
```
docker container ls
docker ps
```
The output should look like this:
```
CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS         PORTS                           NAMES
5b552bf28d58   confluentinc/cp-kafka:7.0.0       "/etc/confluent/dock…"   3 seconds ago   Up 1 second    0.0.0.0:9092->9092/tcp          broker
d646cd845f53   confluentinc/cp-zookeeper:7.0.0   "/etc/confluent/dock…"   6 seconds ago   Up 3 seconds   2181/tcp, 2888/tcp, 3888/tcp    zookeeper
d0b38bf1105f   postgres:13                       "docker-entrypoint.s…"   6 seconds ago   Up 3 seconds   0.0.0.0:5432->5432/tcp          pgstreamdb
5f9473d035a3   dpage/pgadmin4                    "/entrypoint.sh"         6 seconds ago   Up 3 seconds   443/tcp, 0.0.0.0:8080->80/tcp   pgadminWebUI
```
### Open pgadmin WebUI & connect to local postgresql database
Open `localhost:8080` in your browser to access pgadmin WebUI:

![image](https://user-images.githubusercontent.com/77932366/183634105-b86d0ebf-5356-402c-b687-0672e7e964c0.png)

Log in with username and password, mentioned in the docker-compose.yml file:
```
User: admin@admin.com
Password: root
```
Now follow these steps:
1. Right-click on 'Server'
2. Hover over 'Register', then choose 'Server'
3. Choose any 'Name' & navigate to the 'Connection' tab
4. Fill in the required fields

![image](https://user-images.githubusercontent.com/77932366/183637136-17a4d70c-234b-493a-a742-62dff3510aa0.png)

The required fields can be found in the docker-compose.yml file

![image](https://user-images.githubusercontent.com/77932366/183638052-7ad07b5b-ba47-4f88-a954-047c793f4e17.png)

5. In the pgadmin Browser navigate to 'Tables'. Later, the created table will be located.

![image](https://user-images.githubusercontent.com/77932366/183638965-b49fa941-a82b-45d3-b472-3b44ecaa3832.png)

## Kafka streaming pipeline
### producer.py
Note that kafka is used for handling real-time data feeds. A .csv file is static data so in this script the data will be read line by line to simulate real-time data.

Because of that approach the 'del-fuction' is used to delete already existing data in the dictonary.

### consumer.py
The consumer takes the generated kafka message and uploads the values into a postgresql database.

psycopg2 is used for the database connection

### Validate if data stream works
The 'Query Tool' in pgadmin WebUI can be used to query the data (Right-click on 'Tables' --> 'Query Tool').

To validate if real-time data is uploaded to the postgresql database run the following query in pgadmin WebUI multiple times:
```
SELECT * from table1
```
