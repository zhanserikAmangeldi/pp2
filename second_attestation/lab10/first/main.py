from sql_query import *
import psycopg2
from config import config


while True:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    action = int(input("""
        send 1 for create table
        send 2 for add information
        send 3 for update data
        send 4 for querying data
        send 5 for delete data
        send 6 for clear table
        send 0 for quit
        
        YOUR ANSWER --> """))

    if action == 1:
        print(1)
        cur.execute(sql_create_table)
        conn.commit()
    if action == 2:
        action = int(input("""
            send 1 for upload from csv
            send 2 for entering from console (sample: "[name], [number]")
            
            YOUR ANSWER --> """))
        if action == 1:
            path = input("Write path (without spaces) --> ")
            cur.execute(sql_upload_from_csv, (path, ))
            conn.commit()
        if action == 2:
            print("write 'end' for quit mode")
            while True:
                name = input("contact name --> ")
                if name == 'end':
                    break
                number = input("contact number --> ")
                if name == 'end':
                    break
                cur.execute(sql_entering_from_csv, (name, str(number)))
                conn.commit()
                print("new contact created")
    if action == 3:
        action = int(input("""
            send 1 for updating by id
            send 2 for updating by name
            send 3 for updating by phone
        
            YOUR ANSWER --> """))
        if action == 1:
            id = input("id: ")
            action = int(input("send 1 for change name\nsend 2 for change number\nYOUR ANSWER --> "))
            if action == 1:
                new_name = input("new name: ")
                cur.execute(sql_change_name_by_id, (new_name, id))
            if action == 2:
                new_number = input("new number: ")
                cur.execute(sql_change_phone_by_id, (new_number, id))
        if action == 2:
            name = input("name: ")
            action = int(input("send 1 for change name\nsend 2 for change number\nYOUR ANSWER --> "))
            if action == 1:
                new_name = input("new name: ")
                cur.execute(sql_check_exist_by_name, (name, ))
                count = cur.fetchone()[0]
                if count > 1:
                    print("there is two contact: ")
                    cur.execute(sql_select_by_name, (name, ))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_change_name_by_id, (new_name, id))
                elif count == 1:
                    cur.execute(sql_change_name_by_name, (new_name, name ))
                else:
                    print("this contact do not exist")
            if action == 2:
                new_number = input("new number: ")
                cur.execute(sql_select_by_name, (name,))
                count = cur.fetchone()[0]
                if count > 1:
                    print("there are contact: ")
                    cur.execute(sql_select_by_name, (name, ))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_change_name_by_id, (new_number, id))
                elif cur.fetchone()[0] == 1:
                    cur.execute(sql_change_name_by_name, (new_number, name))
                else:
                    print("this contact do not exist")
        if action == 3:
            number = input("number: ")
            action = int(input("send 1 for change name\nsend 2 for change number\nYOUR ANSWER --> "))
            if action == 1:
                new_name = input("new name: ")
                cur.execute(sql_check_exist_by_phone, (number, ))
                count = cur.fetchone()[0]
                if count > 1:
                    print("there are contact: ")
                    cur.execute(sql_select_by_phone, (number, ))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_change_name_by_id, (new_name, id))
                elif count == 1:
                    cur.execute(sql_change_name_by_phone, (new_name, number))
                else:
                    print("this contact do not exist")
            if action == 2:
                new_number = input("new number: ")
                cur.execute(sql_check_exist_by_phone, (number, ))
                count = cur.fetchone()[0]
                if count > 1:
                    print("there are contact: ")
                    cur.execute(sql_select_by_phone, (number, ))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_change_name_by_id, (new_number, id))
                elif count == 1:
                    cur.execute(sql_change_name_by_phone, (new_number, number))
                else:
                    print("this contact do not exist")
        conn.commit()
    if action == 4:
        while True:
            filter_id = int(input("1 for turn on, 0 for turn off id\nans: "))
            filter_name = int(input("1 for turn on, 0 for turn off name\nans: "))
            filter_phone = int(input("1 for turn on, 0 for turn off phone\nans: "))

            if filter_id:
                if filter_name:
                    if filter_phone:
                        cur.execute(sql_select_filter_id_phone_name)
                    else:
                        cur.execute(sql_select_filter_name_id)
                elif filter_phone:
                    cur.execute(sql_select_filter_id_phone)
                else:
                    cur.execute(sql_select_filter_id)
            elif filter_name:
                if filter_phone:
                    cur.execute(sql_select_filter_name_phone)
                else:
                    cur.execute(sql_select_filter_name)
            else:
                cur.execute(sql_select_filter_phone)
            temp = cur.fetchall()
            print(len(temp[0]))
            if len(temp[0]) == 3:
                for first, second, third in temp:
                    print(first, second, third)
            elif len(temp[0]) == 2:
                for second, third in temp:
                    print(second, third)

            end = int(input("1 for end, 0 for continue"))
            if end:
                break
    if action == 5:
        while True:
            name = input("name or end for end: ")
            cur.execute(sql_check_exist_by_name, (name,))
            count = cur.fetchone()[0]
            if count > 1:
                print("there are contact: ")
                cur.execute(sql_select_by_name, (name,))
                for id_query, contact, phone in cur.fetchall():
                    print(id_query, contact, phone)
                id = input("id: ")
                cur.execute(sql_delete_by_id, (id, ))
            elif count == 1:
                cur.execute(sql_delete_by_name, (name, ))
            else:
                print("this contact do not exist")
            conn.commit()
            end = int(input("1 for end, 0 for continue"))
            if end:
                break
    if action == 6:
        cur.execute(sql_clear_all)
        conn.commit()
    if action == 0:
        break