import visitation_records

visitor = visitation_records

class Visitors:

    def visit(self):
        visitor.grab.execute("INSERT INTO visits VALUES ('Marcus', 'Michigan')")

logvisit = Visitors()
# logvisit.visit()
visitor.grab.execute("SELECT * FROM visits WHERE location = 'Michigan'")

visitor.connect.commit()

visitor.grab.execute("SELECT COUNT(location) AS visits_from FROM visits WHERE location = 'michigan'")

print(visitor.grab.fetchall())

visitor.connect.commit()
visitor.connect.close() 
