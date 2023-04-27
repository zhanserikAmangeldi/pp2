import psycopg2
from config import config

def get_parts(code, word):
    code = int(input('''
    return 1 for filter by name
    return 2 for filter by phone
    return 3 for filter by id
    '''))
    word = input()
    conn = None
    by_name = "SELECT * FROM phonebook WHERE contact ILIKE %s"
    by_phone = "SELECT * FROM phonebook WHERE phone_num LIKE %s"
    by_id = "SELECT * FROM phonebook WHERE human_id = %s"
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if code == 1:
            cur.execute(by_name, ('%' + word + '%',))
        if code == 2:
            cur.execute(by_phone, ('%' + word + '%', ))
        if code == 3:
            cur.execute(by_id, (word, ))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

get_parts(1, 'Zha')
