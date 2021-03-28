# coding: UTF-8
import unittest


class Test(unittest.TestCase):

    def gdbStrAssertEqual(self, input, output):
        errMsg = '%s != %s' % (input, output)
        self.assertEqual(str(gdb.parse_and_eval(input)), output, errMsg)

    def test_add_func(self):
        """ This test case tests add method """
        self.gdbStrAssertEqual('add(30, 12)', '42')

    def test_is_odd_func(self):
        """ isOddメソッドのテストケースです """
        expects = {0: 'false', 1: 'true', 2: 'false', 3: 'true'}
        for key, value in expects.items():
            input = 'isOdd(%d)' % key
            output = '%s' % value
            self.gdbStrAssertEqual(input, output)

    def test_make_pair_struct(self):
        """ This test case tests make_pair struct """
        self.gdbStrAssertEqual('make_pair(3, 4)', '{l = 3, r = 4}')


gdb.execute('break main')
gdb.execute('run')
unittest.main(verbosity=2)
