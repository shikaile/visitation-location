import sqlite3

connect = sqlite3.connect('visitors.db')

grab = connect.cursor()

# grab.execute("""CREATE TABLE visits(
#             name text,
#             location text  
#             )""")
# grab.execute("INSERT INTO visits VALUES ('Marry', 'Michigan')")


# grab.execute("SELECT * FROM visits WHERE location = 'Michigan'")

# print(grab.fetchall())

# connect.commit()
# connect.close() 

