import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print('A')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'sdkkjf'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please Enter Number")

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please Enter Number")

    def tearDown(self) -> None:
        print('C')


if __name__ == '__main__':
    unittest.main()
