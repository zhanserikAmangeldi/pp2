CREATE OR REPLACE PROCEDURE insert(new_contact text, new_phone text) LANGUAGE plpgsql
AS $$
    BEGIN
        perform * from phonebook
        where contact = new_contact;
        if not found then
            INSERT INTO phonebook(contact, phone_num) VALUES (new_contact, new_phone);
        else
            UPDATE phonebook SET phone_num = new_phone WHERE contact = new_contact;
        end if;
    end;
$$;

CREATE OR REPLACE PROCEDURE insert_by_console(new_contact text[], new_phone text[]) LANGUAGE plpgsql
AS $$
    BEGIN
        for counter in 1..array_length(new_contact,1) loop
            perform * from phonebook
            where contact = new_contact[counter];
            if not found then
                INSERT INTO phonebook(contact, phone_num) VALUES (new_contact[counter], new_phone[counter]);
            else
                UPDATE phonebook SET phone_num = new_phone[counter] WHERE contact = new_contact[counter];
            end if;
        end loop;
    end;
$$;


CREATE OR REPLACE PROCEDURE delete_by_name_or_phone( IN cont text)
LANGUAGE plpgsql
AS $$
    BEGIN
        DELETE FROM phonebook
        WHERE (contact = cont) or phone_num = cont;
    END;
$$;

CREATE OR REPLACE PROCEDURE rename_all( IN cont text)
LANGUAGE plpgsql
AS $$
    BEGIN
        UPDATE phonebook SET contact = cont WHERE length(contact) > 0;
    END;
$$;



CREATE OR REPLACE FUNCTION find_by_pattern(patt text)
	RETURNS text
	LANGUAGE plpgsql
AS
$$
DECLARE
	temps text;
BEGIN
	SELECT (human_id, contact, phone_num)
	INTO temps
	FROM phonebook
	WHERE contact LIKE patt;

	return temps;
END;
$$;


CREATE OR REPLACE FUNCTION find_by_pattern(patt text)
	RETURNS text
	LANGUAGE plpgsql
AS
$$
DECLARE
	temps text;
BEGIN
	SELECT human_id as id, contact as con, phone_num as phone
	INTO temps
	FROM phonebook
	WHERE contact LIKE patt;

	return temps;
END;
$$;