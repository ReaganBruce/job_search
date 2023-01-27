import pandas as pd
import datetime
import db
import queries
currentDateTime = datetime.datetime.now().date()
connection = db.create_conn('applied_to_jobs.db')
cursor = connection.cursor()


def create_table():
    cursor.execute(queries.create_table)
    
def insert_into_table():
    company = input("Company: ")
    position = input("Position: ")
    location = input("Location: ")
    software = input("Software Stack: ")
    
    cursor.execute(queries.insert_into_applied_jobs, 
                   (company, position, location, software, currentDateTime))
    
    connection.commit()
    
def to_dataframe():
    df = pd.read_sql_query(queries.select_applied_to_jobs, connection)
    print(df)

def main ():
    create_table()
    insert_into_table()
    to_dataframe()
    
main()