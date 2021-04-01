# coding: UTF-8
import unittest
import gdb


class Test(unittest.TestCase):

    def setUp(self):
        gdb.Breakpoint('main')
        gdb.execute('run')

    def gdbStrAssertEqual(self, input, output):
        errMsg = '%s != %s' % (input, output)
        self.assertEqual(str(gdb.parse_and_eval(input)), output, errMsg)

    def test_bp_test_func_ret_true(self):
        """ [BP::test ret=true] """
        gdb.Breakpoint('BP::test')
        gdb.execute('n')
        gdb.execute('p n=4')
        gdb.Breakpoint('Calculate::add')
        gdb.execute('c')
        self.gdbStrAssertEqual('a', '4')
        self.gdbStrAssertEqual('b', '5')


gdb.execute('set logging file src/ptest/log/result_bp.log')
gdb.execute('set logging on')
unittest.main(verbosity=2)
gdb.execute('set logging off')
