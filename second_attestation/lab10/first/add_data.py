import csv
import psycopg2
from config import config






def add_row_from_csv():
    with open('50-contacts.csv', 'r') as file:
        file_reader = csv.reader(file)

        sql = """
            INSERT INTO phonebook (contact, phone_num)
            VALUES (%s, %s);
        """
        conn = None

        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        temp = 0
        for row in file_reader:
            if temp == 0:
                temp += 1
                continue
            cur.execute(sql, (row[0], row[1], row[2], row[3]))
        cur.close()

        conn.commit()

def add_row_from_console():

    sql = """
        INSERT INTO phonebook (first_name, second_name, phone_num, email)
        VALUES (%s, %s, %s, %s);
    """
    conn = None

    params = config()

    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    temp = 0


    data = ''
    while True:
        data = input()
        if data == 'end':
            break
        dates = data.split(sep=',')
        for i in range(len(dates)):
            dates[i] = dates[i].strip()
        cur.execute(sql, (dates[0], dates[1], dates[2], dates[3]))

    cur.close()

    conn.commit()


if __name__ == '__main__':
    add_row_from_csv()


