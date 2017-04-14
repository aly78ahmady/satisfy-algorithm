import unittest
import os
import planner


class WeedingPlannerTest(unittest.TestCase):
    """TestCase for WeedingPlanner Class in planner module"""

    def setUp(self):
        self.plan = planner.WeedingPlanner()

    def tearDown(self):
        del self.plan

    def test_init_generating(self):
        """Test class object initalizer"""
        self.assertEqual(self.plan.relations, list())
        self.assertEqual(self.plan.tables, dict())
        self.assertEqual(self.plan.guests, dict())
        self.assertEqual(self.plan.GUEST_QT, int())
        self.assertEqual(self.plan.TABLE_QT, int())
        self.assertTrue(self.plan.answer)

    def test_read_input_first(self):
        """Test reading content of first example input1.txt"""
        self.plan.read_input(os.path.join('test', 'input1.txt'))
        self.assertEqual(self.plan.GUEST_QT, 4)
        self.assertEqual(self.plan.TABLE_QT, 1)
        self.assertEqual(self.plan.relations, [[1, 2, 'F'],
                                               [2, 3, 'F'],
                                               [3, 4, 'F']])

    def test_read_input_second(self):
        """Test reading content of second example input2.txt"""

        self.plan.read_input(os.path.join('test', 'input2.txt'))
        self.assertEqual(self.plan.GUEST_QT, 5)
        self.assertEqual(self.plan.TABLE_QT, 1)
        self.assertEqual(self.plan.relations, [[1, 3, 'E'],
                                               [1, 2, 'F'],
                                               [4, 5, 'F']])

    def test_read_input_third(self):
        """Test reading content of third example input3.txt"""

        self.plan.read_input(os.path.join('test', 'input3.txt'))
        self.assertEqual(self.plan.GUEST_QT, 8)
        self.assertEqual(self.plan.TABLE_QT, 10)
        self.assertEqual(self.plan.relations, [[1, 2, 'E'],
                                               [2, 5, 'E'],
                                               [6, 7, 'E'],
                                               [7, 8, 'E']])

    def test_read_input_fourth(self):
        """Test reading content of fourth example input4.txt"""

        self.plan.read_input(os.path.join('test', 'input4.txt'))
        self.assertEqual(self.plan.GUEST_QT, 6)
        self.assertEqual(self.plan.TABLE_QT, 2)
        self.assertEqual(self.plan.relations, [[1, 2, 'F'],
                                               [2, 4, 'F'],
                                               [4, 6, 'F'],
                                               [1, 6, 'E']])

    def test_read_input_fifth(self):
        """Test reading content of fifth example input5.txt"""

        self.plan.read_input(os.path.join('test', 'input5.txt'))
        self.assertEqual(self.plan.GUEST_QT, 9)
        self.assertEqual(self.plan.TABLE_QT, 3)
        self.assertEqual(self.plan.relations, [[1, 2, 'E'],
                                               [1, 3, 'F'],
                                               [1, 8, 'F'],
                                               [2, 4, 'F'],
                                               [3, 7, 'E'],
                                               [5, 6, 'F'],
                                               [6, 9, 'F'],
                                               [8, 9, 'E']])

    def test_read_input_bad_file(self):
        """Test reading content of examples with bad file names"""

        self.assertRaises(FileNotFoundError, self.plan.read_input('input.dat'))
        self.assertRaises(FileNotFoundError, self.plan.read_input('input'))
        self.assertRaises(FileNotFoundError, self.plan.read_input(123))
        self.assertRaises(FileNotFoundError, self.plan.read_input(os.path.join('test', 'world')))

    def test_make_relations_first(self):
        """Test making guests` relations with read data for first example input1.txt"""
        self.plan.read_input(os.path.join('test', 'input1.txt'))
        self.plan.make_relations()
        self.assertEqual(self.plan.guests, {1: [{2}, set(), int()],
                                            2: [{1, 3}, set(), int()],
                                            3: [{2, 4}, set(), int()],
                                            4: [{3}, set(), int()]})

    def test_make_relations_second(self):
        """Test making guests` relations with read data for second example input2.txt"""
        self.plan.read_input(os.path.join('test', 'input2.txt'))
        self.plan.make_relations()
        self.assertEqual(self.plan.guests, {1: [{2}, {3}, int()],
                                            2: [{1}, set(), int()],
                                            3: [set(), {1}, int()],
                                            4: [{5}, set(), int()],
                                            5: [{4}, set(), int()]})

    def test_make_relations_third(self):
        """Test making guests` relations with read data for third example input3.txt"""
        self.plan.read_input(os.path.join('test', 'input3.txt'))
        self.plan.make_relations()
        self.assertEqual(self.plan.guests, {1: [set(), {2}, int()],
                                            2: [set(), {5, 1}, int()],
                                            3: [set(), set(), int()],
                                            4: [set(), set(), int()],
                                            5: [set(), {2}, int()],
                                            6: [set(), {7}, int()],
                                            7: [set(), {6, 8}, int()],
                                            8: [set(), {7}, int()]})

    def test_make_relations_fourth(self):
        """Test making guests` relations with read data for fourth example input4.txt"""
        self.plan.read_input(os.path.join('test', 'input4.txt'))
        self.plan.make_relations()
        self.assertEqual(self.plan.guests, {1: [{2}, {6}, int()],
                                            2: [{1, 4}, set(), int()],
                                            3: [set(), set(), int()],
                                            4: [{2, 6}, set(), int()],
                                            5: [set(), set(), int()],
                                            6: [{4}, {1}, int()]})

    def test_make_relations_fifth(self):
        """Test making guests` relations with read data for fifth example input5.txt"""
        self.plan.read_input(os.path.join('test', 'input5.txt'))
        self.plan.make_relations()
        self.assertEqual(self.plan.guests, {1: [{3, 8}, {2}, int()],
                                            2: [{4}, {1}, int()],
                                            3: [{1}, {7}, int()],
                                            4: [{2}, set(), int()],
                                            5: [{6}, set(), int()],
                                            6: [{5, 9}, set(), int()],
                                            7: [set(), {3}, int()],
                                            8: [{1}, {9}, int()],
                                            9: [{6}, {8}, int()]})

    def test_give_table_first(self):
        """Test giving right table to guests for first input example input1.txt"""
        self.plan.read_input(os.path.join('test', 'input1.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        for guest in self.plan.guests.keys():
            self.assertEqual(self.plan.guests[guest][2], 1)

    def test_give_table_second(self):
        """Test giving right table to guests for second input example input2.txt"""
        self.plan.read_input(os.path.join('test', 'input2.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        for guest in self.plan.guests.keys():
            if guest != 3:
                self.assertEqual(self.plan.guests[guest][2], 1)

    def test_give_table_third(self):
        """Test giving right table to guests for third input example input3.txt"""
        self.plan.read_input(os.path.join('test', 'input3.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        for i in range(1, 9):
            self.assertEqual(self.plan.guests[i][2], i)

    def test_give_table_fourth(self):
        """Test giving right table to guests for fourth input example input4.txt"""
        self.plan.read_input(os.path.join('test', 'input4.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        for guest in self.plan.guests.keys():
            if guest == 3:
                self.assertEqual(self.plan.guests[guest][2], 2)
            elif guest == 6:
                continue
            else:
                self.assertEqual(self.plan.guests[guest][2], 1)

    def test_give_table_fifth(self):
        """Test giving right table to guests for fifth input example input5.txt"""
        self.plan.read_input(os.path.join('test', 'input5.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.tables = [table for table in self.plan.tables.values()]
        self.assertIn({1, 3, 8}, self.tables)
        self.assertIn({2, 4, 7}, self.tables)
        self.assertIn({5, 6, 9}, self.tables)

    def test_get_answer_first(self):
        """Test possibility of a plan for first example input1.txt"""
        self.plan.read_input(os.path.join('test', 'input1.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.assertTrue(self.plan.get_answer())

    def test_get_answer_second(self):
        """Test possibility of a plan for second example input2.txt"""
        self.plan.read_input(os.path.join('test', 'input2.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.assertFalse(self.plan.get_answer())

    def test_get_answer_third(self):
        """Test possibility of a plan for third example input3.txt"""
        self.plan.read_input(os.path.join('test', 'input3.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.assertTrue(self.plan.get_answer())

    def test_get_answer_fourth(self):
        """Test possibility of a plan for fourth example input4.txt"""
        self.plan.read_input(os.path.join('test', 'input4.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.assertFalse(self.plan.get_answer())

    def test_get_answer_fifth(self):
        """Test possibility of a plan for fifth example input5.txt"""
        self.plan.read_input(os.path.join('test', 'input5.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.assertTrue(self.plan.get_answer())

    def test_make_output_first(self):
        """Test output file making for first example input1.txt"""
        self.plan.read_input(os.path.join('test', 'input1.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.plan.make_output(os.path.join('test', 'output1.txt'))
        with open(os.path.join('test', 'output1.txt')) as output_file:
            self.assertEqual(output_file.readline().strip('\n'), 'yes')
            for line in output_file:
                line = line.strip(' \n').split(' ')
                self.assertIn(int(line[0]), self.plan.guests)
                self.assertEqual(int(line[1]), self.plan.guests[int(line[0])][2])

    def test_make_output_second(self):
        """Test output file making for second example input2.txt"""
        self.plan.read_input(os.path.join('test', 'input2.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.plan.make_output(os.path.join('test', 'output2.txt'))
        with open(os.path.join('test', 'output2.txt')) as output_file:
            self.assertEqual(output_file.readline().strip('\n'), 'no')

    def test_make_output_third(self):
        """Test output file making for third example input3.txt"""
        self.plan.read_input(os.path.join('test', 'input3.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.plan.make_output(os.path.join('test', 'output3.txt'))
        with open(os.path.join('test', 'output3.txt')) as output_file:
            self.assertEqual(output_file.readline().strip('\n'), 'yes')
            for line in output_file:
                line = line.strip(' \n').split(' ')
                self.assertIn(int(line[0]), self.plan.guests)
                self.assertEqual(int(line[1]), self.plan.guests[int(line[0])][2])

    def test_make_output_fourth(self):
        """Test output file making for fourth example input4.txt"""
        self.plan.read_input(os.path.join('test', 'input4.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.plan.make_output(os.path.join('test', 'output4.txt'))
        with open(os.path.join('test', 'output4.txt')) as output_file:
            self.assertEqual(output_file.readline().strip('\n'), 'no')

    def test_make_output_fifth(self):
        """Test output file making for fifth example input5.txt"""
        self.plan.read_input(os.path.join('test', 'input5.txt'))
        self.plan.make_relations()
        self.plan.give_table()
        self.plan.make_output(os.path.join('test', 'output5.txt'))
        with open(os.path.join('test', 'output5.txt')) as output_file:
            self.assertEqual(output_file.readline().strip('\n'), 'yes')
            for line in output_file:
                line = line.strip(' \n').split(' ')
                self.assertIn(int(line[0]), self.plan.guests)
                self.assertEqual(int(line[1]), self.plan.guests[int(line[0])][2])


if __name__ == '__main__':
    unittest.main()
