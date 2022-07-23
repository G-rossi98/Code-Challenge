import os, re, csv, json
import psycopg2
from config import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

def connect():
    connection = None
    try:
        params = config()
        print("Connection to the database step2 ... ")
        connection = psycopg2.connect(**params)

        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE
        cur = connection.cursor()

        cur.execute('DROP DATABASE dbstep2')
        #Create db
        cur.execute("SELECT * FROM pg_catalog.pg_database WHERE datname = 'dbstep2'")
        exists = cur.fetchone()
        print(exists)
        if not exists:
            pass
            #cur.execute('CREATE DATABASE dbstep2')

        
        # rest of the script
        return
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.commit()
            cur.close()
            connection.close()
            print("Database connection finished.")

connect()