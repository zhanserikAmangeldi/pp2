import psycopg2
from config import config
def update_vendor(code, old, id):
    """ insert multiple vendors into the vendors table"""
    change_first_name = """UPDATE phonebook SET first_name = %s WHERE human_id = %s"""
    change_second_name = """UPDATE phonebook SET second_name = %s WHERE human_id = %s"""
    change_phone = """UPDATE phonebook SET phone_num = %s WHERE human_id = %s"""
    change_email = """UPDATE phonebook SET email = %s WHERE human_id = %s"""
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if code == 1:
            cur.execute(change_first_name, (old, id))
        elif code == 2:
            cur.execute(change_second_name, (old, id))
        elif code == 3:
            cur.execute(change_phone, (old, id))
        elif code == 4:
            cur.execute(change_email, (old, id))

        conn.commit()

        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    code = int(input('''
        RETURN 1 FOR CHANGE FIRST NAME
        RETURN 2 FOR CHANGE SECOND NAME
        RETURN 3 FOR CHANGE PHONE
        RETURN 4 FOR CHANGE EMAIL
    '''))
    old = input()
    id = input()
    update_vendor(code, old, id)
