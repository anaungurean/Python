import unittest
import Homework_04


class MyHomeworkTestCase(unittest.TestCase):
    def test_Ex01(self):

        stack = Homework_04.Stack()
        self.assertEqual(stack.pop(),None)
        self.assertEqual(stack.pop(),None)
        self.assertTrue(stack.is_empty())
        stack.push(1)
        stack.push(2)
        stack.push((1, 2, 3))
        stack.push({'a': [1, 2, 3], 'b': 2})
        stack.push({'a': {'x': [1, 2, 3], 'y': 4}, 'b': 2})
        self.assertEqual(stack.get_items(),[1, 2, (1, 2, 3), {'a': [1, 2, 3], 'b': 2}, {'a': {'x': [1, 2, 3], 'y': 4}, 'b': 2}])
        self.assertEqual(stack.get_size(),5)
        stack.push(99)
        self.assertEqual(stack.peek(),99)
        self.assertEqual(stack.pop(),99)
        print(stack.get_items())

    def test_Ex02(self):
        queue = Homework_04.Queue()
        self.assertEqual(queue.pop(), None)
        self.assertEqual(queue.pop(), None)
        self.assertTrue(queue.is_empty())
        queue.push(('a', 'b', 'c'))
        queue.push(2)
        queue.push((1, 2, 3))
        queue.push({'a': [1, 2, 3], 'b': 2})
        queue.push({'a': {'x': [1, 2, 3], 'y': 4}, 'b': 2})
        print(queue.get_items())
        self.assertEqual(queue.get_items(),
                         [('a', 'b', 'c'), 2, (1, 2, 3), {'a': [1, 2, 3], 'b': 2},
                          {'a': {'x': [1, 2, 3], 'y': 4}, 'b': 2}]
                         )
        self.assertEqual(queue.get_size(), 5)
        queue.push(99)
        self.assertEqual(queue.peek(), ('a', 'b', 'c'))
        self.assertEqual(queue.pop(), ('a', 'b', 'c'))
        print(queue.get_items())

    def test_Ex03(self):
        matrix_1 = Homework_04.Matrix(3, 4)
        matrix_1.set_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
        matrix_2 = Homework_04.Matrix(4, 3)
        matrix_2.set_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2]])

        self.assertEqual(matrix_1.get_matrix(), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
        self.assertEqual(matrix_1.get_rows(), 3)
        self.assertEqual(matrix_1.get_columns(), 4)
        self.assertEqual(matrix_1.get_element(1, 2), 7)
        matrix_1.set_element(2, 3, 5)
        self.assertEqual(matrix_1.get_element(2, 3), 5)

        transposed_matrix_1 = matrix_1.transpose()
        expected_transposed = [[1, 5, 9], [2, 6, 0], [3, 7, 1], [4, 8, 5]]
        self.assertEqual(transposed_matrix_1.get_matrix(), expected_transposed)

        multiplied_matrix = matrix_1 * matrix_2
        expected_multiplied = [[30, 40, 50], [78, 104, 130], [16, 31, 46]]
        self.assertEqual(multiplied_matrix.get_matrix(), expected_multiplied)

        matrix_1.apply(lambda x: x + 1)
        expected_applied = [[2, 3, 4, 5], [6, 7, 8, 9], [10, 1, 2, 6]]
        self.assertEqual(matrix_1.get_matrix(), expected_applied)

        self.assertEqual(str(matrix_1), '[[2, 3, 4, 5], [6, 7, 8, 9], [10, 1, 2, 6]]')




if __name__ == '__main__':
    unittest.main()
