import unittest
from unittest.mock import patch
from cli import main
from io import StringIO


class TestCli(unittest.TestCase):
    @patch('cli.get_input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_two_rectangles_inside(self, mocked_stdout, mocked_input):
        mocked_input.side_effect = ['2', '0 0 10 10', '1 1 9 9']
        result = main()
        self.assertEqual(0, result)
        self.assertEqual(mocked_stdout.getvalue(), "1\n")

    @patch('cli.get_input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_two_same_rectangles_are_overlapping(self, mocked_stdout, mocked_input):
        mocked_input.side_effect = ['2', '0 0 10 10', '0 0 10 10']
        result = main()
        self.assertEqual(1, result)
        self.assertEqual(
            mocked_stdout.getvalue(),
            "Rectangles are overlapping:"
            " Rectangle((Decimal('0'), Decimal('0'))(Decimal('10'), Decimal('10'))),"
            " Rectangle((Decimal('0'), Decimal('0'))(Decimal('10'), Decimal('10')))\n"
        )

    @patch('cli.get_input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_two_rectangles_are_not_overlapping(self, mocked_stdout, mocked_input):
        mocked_input.side_effect = ['2', '2.0 3.5 3.0 4.5', '2.0 2.0 3.0 3.0']
        result = main()
        self.assertEqual(0, result)
        self.assertEqual(mocked_stdout.getvalue(), "2\n")

    @patch('cli.get_input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_two_rectangles_are_overlapping(self, mocked_stdout, mocked_input):
        mocked_input.side_effect = ['2', '0 0 10 10', '5 5 15 15']
        result = main()
        self.assertEqual(1, result)
        self.assertEqual(
            mocked_stdout.getvalue(),
            "Rectangles are overlapping:"
            " Rectangle((Decimal('5'), Decimal('5'))(Decimal('15'), Decimal('15'))),"
            " Rectangle((Decimal('0'), Decimal('0'))(Decimal('10'), Decimal('10')))\n")

    @patch('cli.get_input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_assignment(self, mocked_stdout, mocked_input):
        mocked_input.side_effect = [
            '14',
            '1.0 1.0 10.0 6.0',
            '1.5 1.5 6.0 5.0',
            '2.0 2.0 3.0 3.0',
            '2.0 3.5 3.0 4.5',
            '3.5 2.0 5.5 4.5',
            '4.0 3.5 5.0 4.0',
            '4.0 2.5 5.0 3.0',
            '7.0 3.0 9.5 5.5',
            '7.5 4.0 8.0 5.0',
            '8.5 3.5 9.0 4.5',
            '3.0 7.0 8.0 10.0',
            '5.0 7.5 7.5 9.5',
            '5.5 8.0 6.0 9.0',
            '6.5 8.0 7.0 9.0',
        ]
        result = main()
        self.assertEqual(0, result)
        self.assertEqual(mocked_stdout.getvalue(), "9\n")

    @patch('cli.get_input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_string_as_rectangle_count(self, mocked_stdout, mocked_input):
        mocked_input.side_effect = ['foo']
        result = main()
        self.assertEqual(1, result)
        self.assertEqual(mocked_stdout.getvalue(), "Provided input is not a number: foo\n")

    @patch('cli.get_input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_covered_rectangles(self, mocked_stdout, mocked_input):
        mocked_input.side_effect = [
            '5',
            '1.0 1.0 10.0 10.0',
            '3.0 3.0 4.0 4.0',  # covered
            '5.0 3.0 6.0 4.0',  # covered
            '1.5 1.5 7.0 5.0',  # covering
            '15.0 1.0 20.0 6.0',
        ]
        result = main()
        self.assertEqual(0, result)
        self.assertEqual(mocked_stdout.getvalue(), "4\n")

    @patch('cli.get_input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_data_2(self, mocked_stdout, mocked_input):
        mocked_input.side_effect = ['0']
        result = main()
        self.assertEqual(0, result)
        self.assertEqual(mocked_stdout.getvalue(), "0\n")

    @patch('cli.get_input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_data_3(self, mocked_stdout, mocked_input):
        mocked_input.side_effect = [
            '4',
            '-4.0 -4.0 4.0 4.0',
            '-3.0 -3.0 3.0 3.0',
            '-2.0 -2.0 2.0 2.0',
            '-1.0 -1.0 1.0 1.0',
        ]
        result = main()
        self.assertEqual(0, result)
        self.assertEqual(mocked_stdout.getvalue(), "2\n")

    @patch('cli.get_input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_data_4(self, mocked_stdout, mocked_input):
        mocked_input.side_effect = [
            '14',
            '1.5 1.5 6.0 5.0',
            '2.0 2.0 3.0 3.0',
            '2.0 3.5 3.0 4.5',
            '3.5 2.0 5.5 4.5',
            '4.0 3.5 5.0 4.0',
            '4.0 2.5 5.0 3.0',
            '7.0 3.0 9.5 5.5',
            '7.5 4.0 8.0 5.0',
            '8.5 3.5 9.0 4.5',
            '3.0 7.0 8.0 10.0',
            '5.0 7.5 7.5 9.5',
            '5.5 8.0 6.0 9.0',
            '6.5 8.0 7.0 9.0',
            '1.0 1.0 10.0 6.0',
        ]
        result = main()
        self.assertEqual(0, result)
        self.assertEqual(mocked_stdout.getvalue(), "9\n")
