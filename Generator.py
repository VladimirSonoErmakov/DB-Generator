import psycopg2
from config import host, user, password, db_name

# Процкедура встваки в базу

def InsertUserToDatabase(first_name, nick_name):
    pass

def NameGenerator(Namenumbeers):
    pass

def CreateTableFromConfig():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name        
        )
        connection.autocommit = True
            
            
            # создаем таблицу    
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE users(
                    id serial PRIMARY KEY,
                    first_name varchar(50) NOT NULL,
                    nick_name varchar(50) NOT NULL);"""
            )
            print("[INFO] Table created successfully")
            
        
    except Exception as _ex:
        print('[info]: PostgreSQL error:', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL cottection closed')
            
def InsertDataToTable():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name        
        )
        connection.autocommit = True
            
        #вставляем данные
        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO users (first_name, last_name) VALUES
                ('Oleg','Barracuda');"""
            )
            print("[INFO] Data inserted")
        
    except Exception as _ex:
        print('[info]: PostgreSQL error:', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL cottection closed')
           