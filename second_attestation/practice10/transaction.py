import psycopg2
from config import config

def add_part(part_name, vendor_list):
    insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id"
    assign_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s)"

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(insert_part, (part_name, ))

        part_id = cur.fetchone()[0]

        for vendor_id in vendor_list:
            cur.execute(assign_vendor, (vendor_id, part_id))


        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    add_part('SIM Tray', (1, 2))
    add_part('Speaker', (3, 4))
    add_part('Vibrator', (5, 6))
    add_part('Antenna', (6, 7))
    add_part('Home Button', (1, 5))
    add_part('LTE Modem', (1, 5))