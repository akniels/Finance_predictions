from __future__ import print_function
import numpy
import psycopg2
import datetime
from math import ceil
import bs4


try:
    conn = psycopg2.connect("dbname=securities user=andrewnielson")
    cur = conn.cursor()
except Exception as e: 
        print(e)
 
## remember to input the cursor
class create_tables():
    def __init__(self, cur):
         self.cur = cur
           
    def create_exchange(self):
        sql_query = """CREATE TABLE exchange (id SERIAL PRIMARY KEY NOT NULL, 
       abbrev varchar(32) NOT NULL,
       name varchar(255) NOT NULL,
       city varchar(255) NULL,
       country varchar(255) NULL,
       ‘currency‘ varchar(64) NULL, 
       ‘timezone_offset‘ time NULL, 
       ‘created_date‘ date NOT NULL,
       ‘last_updated_date‘ date NOT NULL)"""
        try:
            cur.execute(sql_query)
            print("Exchange query successfull")
        except Exception as e:
            print("Exchange Query Unsuccessful")
            print(e)
    def delete_exchange(self):
        sql_query = """DELETE TABLE exchange"""
        try:
            cur.execute(sql_query)
            print("Exchange query delete successfull")
        except Exception as e:
            print("Exchange Query delete Unsuccessful")
            print(e)
    def create__data_vendor(self):
        sql_querydv = """CREATE TABLE data_vendor(
        id SERIAL PRIMARY KEY NOT NULL,
        name varchar(64) NOT NULL,
        website_url varchar(255) NULL,
        support_email varchar(255) NULL,
        created_date datetime NOT NULL,
        last_updated_date datetime NOT NULL,
    )
        """
        try:
            cur.execute(sql_querydv)
            print("Deta Vendor Query Successful")
        except Exception as e:
            print("Data Vendor Query unsuccessfull")
            print(e)
    def delete_data_vendor(self):
        sql_query = """DELETE TABLE data_vendor"""
        try:
            cur.execute(sql_query)
            print("data vendor query delete successfull")
        except Exception as e:
            print("data vendor Query delete Unsuccessful")
            print(e)
    def create_symbol(self):
        sql_query = """CREATE TABLE symbol (
id int PRIMARY KEY NOT NULL AUTO_INCREMENT, 
exchange_id int  REFERENCES exchange(id) NULL,
ticker varchar(32) NOT NULL, 
instrument varchar(64) NOT NULL, 
name varchar(255) NULL,
sector varchar(255) NULL,
currency varchar(32) NULL, 
created_date datetime NOT NULL,
last_updated_date datetime NOT NULL, 
)"""
        try:
            cur.execute(sql_query)
            print("Deta Vendor Query Successful")
        except Exception as e:
            print("Data Vendor Query unsuccessfull")
            print(e)
    def create_daily_price(self):
        sql_query = """CREATE TABLE daily_price (
        id SERIAL PRIMARY KEY NOT NULL, 
        data_vendor_id int REFERENCES data_vendor(id) NOT NULL,
        symbol_id int REFERENCES symbol(id) NOT NULL,
        price_date datetime NOT NULL,
         created_date datetime NOT NULL, 
        last_updated_date datetime NOT NULL, 
        open_price decimal(19,4) NULL,
        high_price decimal(19,4) NULL,
        low_price decimal(19,4) NULL,
        close_price decimal(19,4) NULL,
        adj_close_price decimal(19,4) NULL, 
        volume bigint NULL
        )"""   
        try:
            cur.execute(sql_query)
            print("Daily Price Query Successful")
        except Exception as e:
            print("Daily Price Query unsuccessfull")
            print(e)  
create_tables.create_exchange(cur)
create_tables.delete_exchange(cur)
create_tables.create__data_vendor(cur)
create_tables.delete_data_vendor(cur)