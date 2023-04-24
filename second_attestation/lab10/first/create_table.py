import psycopg2
from config import config

def create_table():
    sql = """
    CREATE TABLE phonebook (
        human_id SERIAL PRIMARY KEY,
        first_name text not null,
        second_name text not null,
        phone_num text NOT NULL,
        email text not null
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