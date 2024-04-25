import dbconn

def delete_empl(empid):
    # get connection
    conn = dbconn.get_connection()

    # form a query
    query = f"delete from persons where empid = %s;"
    val = (empid, )

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



delete_empl(2)













