import sqlite3
from visitor_log import Visitor

db = sqlite3.connect(':memory:')
grab = db.cursor()

grab.execute("""CREATE TABLE visits(
            name text,
            location text  
            )""")

def insert_visitor(visitor):
    with db:
        grab.execute("INSERT INTO visits VALUES (:name, :location)", {'name':visitor.name, 'location': visitor.location})
        return (visitor.gratitude)


def visit_log(location):
    grab.execute("SELECT COUNT(location) AS visits_from FROM visits WHERE location = :location", {'location': 'Michigan'})
    return grab.fetchall()


visit1 = Visitor('Tom', 'Michigan') 
visit2 = Visitor('Jim', 'Michigan') 

insert_visitor(visit1)
insert_visitor(visit2)

visit = visit_log('Michigan')
print(visit)

db.close() 
