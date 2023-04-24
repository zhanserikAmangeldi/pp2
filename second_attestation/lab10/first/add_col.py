import psycopg2
from config import config

def create_table():
    sql = """
    CREATE TABLE phonebook (
        human_id SERIAL PRIMARY KEY,
        human_name text not null ,
        phone_num text NOT NULL 
    )
    """
    conn = None

    params = config()

    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute(sql)

    cur.close()

    conn.commit()



if __name__ == '__main__':
    create_table()