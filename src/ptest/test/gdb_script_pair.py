# coding: UTF-8
import unittest
import gdb


class Test(unittest.TestCase):

    def gdbStrAssertEqual(self, input, output):
        errMsg = '%s != %s' % (input, output)
        self.assertEqual(str(gdb.parse_and_eval(input)), output, errMsg)

    def test_make_pair_struct(self):
        """ [makePair] """
        self.gdbStrAssertEqual('makePair(3, 4)', '{l = 3, r = 4}')


gdb.execute('set logging file src/ptest/log/result_pair.log')
gdb.execute('set logging on')
gdb.Breakpoint('main')
gdb.execute('run')
unittest.main(verbosity=2)
gdb.execute('set logging off')
