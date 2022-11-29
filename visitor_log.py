
class Visitor:

    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    @property
    def gratitude(self):
        return 'Thanks for visiting {} from {}'.format(self.name, self.location)

