import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close()
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"db/pythonsqlite.db"

    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS users(
                                    id SERIAL,
                                    username VARCHAR NOT NULL,
                                    pass VARCHAR NOT NULL,
                                    UNIQUE(username)
                                );  """

    #create a database connection
    conn = create_connection(database)

    #create table(s)
    if conn is not None:
        create_table(conn, sql_create_projects_table)
        conn.commit()  
    else:
        print("Error! cannot create the database connection.")
    conn.close()

if __name__ == '__main__':
    main()
