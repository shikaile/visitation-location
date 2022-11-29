import sqlite3
from visitor_log import Visitor

db = sqlite3.connect('visitors.db')
grab = db.cursor()

# grab.execute("""CREATE TABLE visits(
#             name text,
#             location text  
#             )""")

visitor = Visitor('Jimmy', 'Michigan') 
# grab.execute("INSERT INTO visits VALUES ('Marcus', 'Michigan')")

grab.execute("SELECT COUNT(location) AS visits_from FROM visits WHERE location = 'Michigan'")

print(grab.fetchall())
print(visitor.gratitude)

db.commit()
db.close() 
