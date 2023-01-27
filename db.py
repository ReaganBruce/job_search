import sqlite3

def create_conn(local_db):
    connection = None
    try:
        connection = sqlite3.connect(local_db)
        version = sqlite3.version
        print('Connecting to local database: {0} on version: {1}'.format(local_db, version))
        connection.commit()
    except Exception as error:
        print(error)
        connection.close()
    
    return connection