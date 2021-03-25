import unittest


class Test(unittest.TestCase):
    def gdbParseEvalAssertEqual(self, a, expr):
        self.assertEqual(a, gdb.parse_and_eval(expr))

    def gdbParseEvalStrAssertEqual(self, a, expr):
        self.assertEqual(a, str(gdb.parse_and_eval(expr)))

    def test_aaaa(self):
        self.gdbParseEvalAssertEqual(42, 'add(30, 12)')

    def test_bbb(self):
        self.gdbParseEvalAssertEqual(0, 'add(0, 0)')

    def test_ccc(self):
        self.gdbParseEvalStrAssertEqual('{l = 3, r = 4}', 'make_pair(3, 4)')


gdb.execute('break main')
gdb.execute('run')
unittest.main(verbosity=2)
