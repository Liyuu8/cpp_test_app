# coding: UTF-8
import unittest
import gdb


class Test(unittest.TestCase):

    def gdbStrAssertEqual(self, input, output):
        errMsg = '%s != %s' % (input, output)
        self.assertEqual(str(gdb.parse_and_eval(input)), output, errMsg)

    def test_add_func(self):
        """ [Calculate::add] """
        self.gdbStrAssertEqual('Calculate::add(30, 12)', '42')

    def test_calculate_is_odd_func(self):
        """ [Calculate::isOdd] """
        expects = {0: 'false', 1: 'true', 2: 'false', 3: 'true'}
        for key, value in expects.items():
            input = 'Calculate::isOdd(%d)' % key
            output = '%s' % value
            self.gdbStrAssertEqual(input, output)

    def test_calculate_is_even_func(self):
        """ [Calculate::isEven] """
        expects = {5: 'false', 6: 'true', 7: 'false', 8: 'true'}
        for key, value in expects.items():
            input = 'Calculate::isEven(%d)' % key
            output = '%s' % value
            self.gdbStrAssertEqual(input, output)


gdb.execute('set logging file src/ptest/log/result_calculate.log')
gdb.execute('set logging on')
gdb.Breakpoint('main')
gdb.execute('run')
unittest.main(verbosity=2)
gdb.execute('set logging off')
