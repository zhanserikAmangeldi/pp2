import psycopg2
from config import config

conn = None
try:
    # read database configuration
    params = config()
    # connect to the PostgreSQL database
    conn = psycopg2.connect(**params)
    # create a cursor object for execution
    cur = conn.cursor()

    name = input('contact name: ')
    phone = input('phone: ')

    # call a stored procedure
    cur.execute('CALL insert(%s,%s)', (name, phone))

    # commit the transaction
    conn.commit()

    # close the cursor
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()