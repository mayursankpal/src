#!/usr/bin/env python3
import os
import sqlite3
import sys


create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'


class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):          #This method is called when exiting the context
        if hasattr(self, 'cursor'):
            self.cursor.close()                             #Close the cursor if it exists
            print(f'cursor closed: {self.path}')
        else:
            print('cursor not established')                 #If cursor was not established, print a message 

        if hasattr(self, 'connection'):
            self.connection.close()                         #Close the connection to the database
            print(f'connection closed: {self.path}')
        else:
            print('connection not established')             #If connection was not established, print a message
        
        if exc_type is not None:
            print(f'an error occurred: {exc_val}')          #>>> an error occurred: raised exception while fetching data    
            print(exc_tb.tb_frame.f_code.co_filename)       #>>> /home/mayursankpal/src/python/context_manager/custom_class/./database.py
            print(exc_tb.tb_lineno)                         #>>> 36

def main():
    with Database(':memory:') as db:
        db.cursor.execute(create_table_sql_statement)
        db.connection.commit()

        db.cursor.execute(insert_into_table_sql_statement)
        db.connection.commit()

        db.cursor.execute(select_from_table_sql_statement)
        raise Exception('raised exception while fetching data')
        print(db.cursor.fetchall())


if __name__ == '__main__':
    print("Execution Started :>")
    main()

# [('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')]