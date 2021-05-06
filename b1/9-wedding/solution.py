from collections import namedtuple, Counter
import operator

Person = namedtuple("Person", ["first", "last"])

class GuestList(object):

    max_at_table = 10

    def __init__(self):
        self.guestlist = {}

    def assign(self, person, table_number):
        if not table_number:
            self.guestlist[person] = 0
        elif len(self.table(table_number)) < 10:
            self.guestlist[person] = table_number
        else:
            raise TableFull('Table is full')
    
    def __len__(self):
        return len(self.guestlist)

    def table(self, table):
        return [person for person, table_number in self.guestlist.items() if table_number == table]

    def unassigned(self):
        return [person for person, table_number in self.guestlist.items() if table_number == 0]

    def free_space(self):
        counter = Counter(list(self.guestlist.values()))
        return {key:GuestList.max_at_table-count for key, count in counter.items()}

    def guests(self):
        # tables = sorted(list(set(self.guestlist.values())))
        return [person for person, table_number in sorted(self.guestlist.items(), key=operator.itemgetter(1))]

    def __repr__(self):
        tables = set(self.guestlist.values())
        # sort(tables)
        for table_number in tables:
            print(table_number)
            for person in sorted(self.table(table_number), key=operator.itemgetter(1)):
                print(person.last, person.first)


class TableFull(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        # self.status = status

