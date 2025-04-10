import sqlite3

def main():
    # connect to the database
    conn =sqlite3.connect('testDB.db')

    # get a cursor
    cur = conn.cursor()

    # add the contacts table
    cur.execute('''CREATE TABLE Contacts (Contact ID INTEGER PRIMARY KEY NOT NULL,
                                            Name TEXT,
                                            Email TEXT)''')
    
    # commit the changes
    conn.commit()

    # close the connection
    conn.close()


# execute the main function
if __name__ == '__main__':
    main()
