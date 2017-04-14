import sys
import os

message = 'Usage:   python3 planner.py [input_filename] [output_filename]'


class WeedingPlanner:
    """a Class to take right tables for guests with enemy and firend pairs
    Firends must have seat in same table
    Enemies must have seat in diffrend table
    and Every guest must have seat only in one table"""

    def __init__(self):
        """Data instances:
            relations = a list to store pairs with bad or good relations
                example: [[guest1, guest2, 'E'], [guest3, guest4, 'F'], ...]   E as enemy and F as firend

            tables = a dictionary to keep tables` number as key and guests who have seat on it as values
            guests = a dictionary to keep guests` number as key, a list as value contains [firends` numbers, enemies` number, table]
                firends` numbers and enemies` numbers are lists and table is the guest`s table, 0 if the guest haven`t any table yet

            GUEST_QT = amount of guests, given in input file
            TABLE_QT = amount of tables, given in input file
            _answer = private bool, False if input relations doesn`t have any possible plan, default True"""

        self.relations = list()
        self.tables = dict()
        self.guests = dict()
        self.GUEST_QT = int()
        self.TABLE_QT = int()
        self.answer = True

    def read_input(self, filename):
        """Read input file to make relations
        first number of first line as GUEST_QT and second number as TABLE_QT
        other lines will be splitted to three data as a pair of guests and thier relation
        save every three data in a list and append it to relations list

        Args:
            filename = the input file address, default is 'input.txt'

        Raises:
            FileNotFoundError = if OSError or IOError occured during the input file openning process"""

        filename = str(filename)
        try:
            with open(filename) as input_file:
                self.GUEST_QT, self.TABLE_QT = input_file.readline().strip(' \n').split(' ')
                self.GUEST_QT = int(self.GUEST_QT)
                self.TABLE_QT = int(self.TABLE_QT)

                while True:
                    line = input_file.readline()
                    if line == '':
                        break
                    g1, g2, rt = line.strip('\n').split(' ')
                    self.relations.append([int(g1), int(g2), str(rt)])
        except FileNotFoundError:
            pass

    def make_relations(self):
        """Make guests as a list contains [set(firends), set(enemies), int(table)]
        then add every guest firends and enemies into it`s list
        and add every guest`s table to guests list"""
        for rel in self.relations:
            if rel[0] not in self.guests.keys():
                self.guests[rel[0]] = [set(), set(), int()]
            if rel[1] not in self.guests.keys():
                self.guests[rel[1]] = [set(), set(), int()]

            if rel[2] == 'E':
                self.guests[rel[0]][1].add(rel[1])
                self.guests[rel[1]][1].add(rel[0])
            elif rel[2] == 'F':
                self.guests[rel[0]][0].add(rel[1])
                self.guests[rel[1]][0].add(rel[0])

        for i in range(1, self.GUEST_QT + 1):
            if i not in self.guests.keys():
                self.guests[i] = [set(), set(), int()]

    def give_table_freeusers(self):
        """Give right table to guests who doesn`t found their table to seat before main changes
        and after changes, they doesn`t found an opportunity to find the table.the

        This method conditions are easier.
        If a firend found in table and no one of enemies was in table, seat in that table."""

        for tb in self.tables.keys():
            for gt in self.guests.keys():
                if self.guests[gt][2] != int():
                    continue

                for enemy in self.guests[gt][1]:
                    if enemy in self.tables[tb]:
                        break
                else:
                    if len(self.guests[gt][0]) > 0:
                        for firend in self.guests[gt][0]:
                            if firend in self.tables[tb] or self.guests[firend][2] == int():
                                self.tables[tb].add(gt)
                                self.guests[gt][2] = tb
                                break
                    else:
                        self.tables[tb].add(gt)
                        self.guests[gt][2] = tb
                        break

    def give_table(self):
        """Find the right table for a guest depends on three condition:
            firends must be in the table
            enemies must not be in the table
            firends of enemies must not be in the table"""

        for tb in range(1, self.TABLE_QT + 1):
            self.tables[tb] = set()

            for gt in self.guests.keys():
                if self.guests[gt][2] != int():
                    continue

                if self.tables[tb] == set():
                    for i in range(1, tb):
                        for firend in self.guests[gt][0]:
                            if firend in self.tables[i]:
                                break
                        else:
                            continue
                        break
                    else:
                        self.tables[tb].add(gt)
                        self.guests[gt][2] = tb

                else:
                    for enemy in self.guests[gt][1]:
                        if enemy in self.tables[tb]:
                            break
                        for enemy_firend in self.guests[enemy][0]:
                            if enemy_firend in self.tables[tb]:
                                break
                        else:
                            continue
                        break
                    else:
                        for firend in self.guests[gt][0]:
                            if firend in self.tables[tb]:
                                self.tables[tb].add(gt)
                                self.guests[gt][2] = tb
                                break

        self.give_table_freeusers()

    def get_answer(self):
        """Find the posibility of plan`s answer, with comparing the relations and tables that guests seated on.

        Returns:
            _answer = private bool, False if input relations doesn`t have any possible plan, default True """
        for tb in self.tables.keys():
            for gt in self.guests.keys():
                if self.guests[gt][2] == int():
                    self.answer = False

            for guest in self.tables[tb]:
                for enemy in self.guests[guest][1]:
                    if enemy in self.tables[tb]:
                        self.answer = False
                for firend in self.guests[guest][0]:
                    if firend not in self.tables[tb]:
                        self.answer = False

        return self.answer

    def make_output(self, filename):
        """Create an output file and save the plan into it, if a plan found for the guests.
        It will takes the _answer by the get_answer() method
        and write 'yes' + plan if _answer was True and 'no' if _answer was False

        Args:
            filename = the output file address, default is 'output.txt'

        Raises:
            FileNotFoundError = if OSError or IOError occured during the output file openning process"""

        filename = str(filename)
        with open(filename, 'w') as output_file:
            if self.get_answer() is True:
                output_file.write('yes' + '\n')
                for guest in self.guests.keys():
                    output_file.write('{guest} {table}\n'.format(guest=guest, table=self.guests[guest][2]))

            elif self.get_answer() is False:
                output_file.write('no')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(message)
    else:
        if not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2]):
            sys.exit(message)
    try:
        plan = WeedingPlanner()
        plan.read_input(sys.argv[1])
        plan.make_relations()
        plan.give_table()
        plan.make_output(sys.argv[2])
    except Exception as err:
        sys.exit(str(err))
    else:
        print('Done!')
        sys.exit()
