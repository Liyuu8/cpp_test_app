import unittest


class Test(unittest.TestCase):
    def gdbAssertEqual(self, a, expr):
        self.assertEqual(a, gdb.parse_and_eval(expr))

    def gdbStrAssertEqual(self, a, expr):
        self.assertEqual(a, str(gdb.parse_and_eval(expr)))

    def gdbAssertTrue(self, expr):
        self.assertTrue(gdb.parse_and_eval(expr))

    def test_assert_equal(self):
        self.gdbAssertEqual(42, 'add(30, 12)')

    def test_assert_true(self):
        self.gdbAssertTrue('isOdd(3)')

    def test_assert_equal_str(self):
        self.gdbStrAssertEqual('{l = 3, r = 4}', 'make_pair(3, 4)')


gdb.execute('break main')
gdb.execute('run')
unittest.main(verbosity=2)
