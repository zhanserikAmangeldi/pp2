import psycopg2
from config import config
def update_vendor(vendor_id, vendor_name):
    """ insert multiple vendors into the vendors table"""
    sql = """UPDATE vendors SET vendor_name = %s WHERE vendor_id = %s"""
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql, (vendor_name, vendor_id))

        conn.commit()

        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    update_vendor(1, "3M Corp")