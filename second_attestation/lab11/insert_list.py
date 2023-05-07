import psycopg2
import re
from config import config

conn = None
try:
    # read database configuration
    params = config()
    # connect to the PostgreSQL database
    conn = psycopg2.connect(**params)
    # create a cursor object for execution
    cur = conn.cursor()
    names = []
    phones = []
    error = []
    while True:
        contacts = input()
        if len(contacts) == 0:
            break
        name = contacts.split(sep=',')[0].strip()
        phone = contacts.split(sep=',')[1].strip()
        if name.isspace() or len(re.findall(r'[0-9]+', phone)) != 1:
            error += [name + ', ' + phone]
        else:
            names.append(name)
            phones.append(phone)


    # call a stored procedure
    cur.execute('CALL insert_by_console(%s,%s)', (names, phones))
    print(error)
    # commit the transaction
    conn.commit()

    # close the cursor
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()