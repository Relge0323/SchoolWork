import sqlite3

def main():
    conn = sqlite3.connect('testDB.db')

    cur = conn.cursor()

    cur.execute('''UPDATE Contacts
                SET Email = "kbrown@example.com"
                WHERE Name == "Kevin Brown"''')
    
    conn.commit()

    cur.execute('''SELECT * FROM Contacts''')

    results = cur.fetchall()

    for row in results:
        print(f'{row[0]:<5} {row[1]:15} {row[2]:20}')


    conn.close()

if __name__ == '__main__':
    main()
