from sql_query import *
import psycopg2, re
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
        send 7 for querying by pattern
        send 0 for quit
        
        YOUR ANSWER --> """))
    if action == 7:
        pattern = input()
        # phone = "SELECT COUNT(*) FROM phonebook WHERE phone_num LIKE %s"
        offset = 0
        while True:
            cur.execute(sql_search_by_pattern, ('%' + pattern + '%', '%' + pattern + '%', offset))
            info = cur.fetchall()
            for element in info:
                print(element)
            print(int(offset / 5), offset)
            action = int(input('send 1 for next, send 2 for previous, send 0 for break'))
            if not info:
                if action == 1:
                    offset += 5
                if action == 2:
                    if offset - 5 < 0:
                        print('NO')
                    else:
                        offset -= 5
            if action == 0:
                break
    elif action == 1:
        print(1)
        cur.execute(sql_create_table)
        conn.commit()
    elif action == 2:
        action = int(input("""
            send 1 for upload from csv
            send 2 for entering from console (sample: "[name], [number]"
            send 3 for entering from list 
            
            !!! 
                the number must be without any spaces,
                special characters, etc. numbers only,
                
                example --> [87324321332]
                
                example of element of list:
                [Zhanserik, 87324321332]
            
            !!!
            
            YOUR ANSWER --> """))


        if action == 1:
            path = input("Write path (without spaces) --> ")
            cur.execute(sql_upload_from_csv, (path, ))
            conn.commit()
        elif action == 2:
            name = input()
            phone = input()
            cur.execute('call insert(%s, %s)', (name, phone))
        elif action == 3:
            print("write 'end' for quit mode")
            returned_list = ''
            # elements = element.split(sep='\n')
            while True:
                element = input()
                if element == 'end':
                    break
                pattern_name = r'[a-zA-Z]+'
                pattern_phone = r'[0-9]+'
                res_name = re.findall(pattern_name, element)
                res_phone = re.findall(pattern_phone, element)
                name = ''
                phone = ''
                for i in res_name:
                    name += i + ' '
                for j in res_phone:
                    phone += j + ' '
                if len(res_phone) != 1:
                    # print(res_phone)
                    returned_list += f'{name}, {phone}' + '\n'
                else:
                    cur.execute(sql_check_exist_by_name, (name,))
                    if cur.fetchone()[0] != 0:
                        cur.execute(sql_change_phone_by_name, (phone, name))
                    else:
                        cur.execute(sql_entering_from_console, (name, phone))
                    conn.commit()
            print(returned_list)
    elif action == 3:
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
        elif action == 3:
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
            elif action == 2:
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
    elif action == 4:
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
    elif action == 5:
        action = int(input("send 1 for delete by name\nsend 2 for delete by phone\nYOUR ANS -->"))
        if action == 1:
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
        elif action == 2:
            while True:
                name = input("number or end for end: ")
                cur.execute(sql_check_exist_by_phone, (name,))
                count = cur.fetchone()[0]
                if count > 1:
                    print("there are contact: ")
                    cur.execute(sql_select_by_phone, (name,))
                    for id_query, contact, phone in cur.fetchall():
                        print(id_query, contact, phone)
                    id = input("id: ")
                    cur.execute(sql_delete_by_id, (id,))
                elif count == 1:
                    cur.execute(sql_delete_by_phone, (name,))
                else:
                    print("this contact do not exist")
                conn.commit()
                end = int(input("1 for end, 0 for continue"))
                if end:
                    break
    elif action == 6:
        cur.execute(sql_clear_all)
        conn.commit()
    elif action == 0:
        break