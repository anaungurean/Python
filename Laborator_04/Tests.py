import unittest
import Homework_04


class MyHomeworkTestCase(unittest.TestCase):
    def test_Ex01(self):

        stack = Homework_04.Stack()
        self.assertTrue(stack.is_empty())
        with self.assertRaises(Exception):
            stack.pop()
        with self.assertRaises(Exception):
            stack.peek()
        stack.push(10)
        stack.push(20.5)
        stack.push("Ana")
        stack.push((1, 2, 3))
        stack.push(True)
        stack.push([1, 2, 3])
        stack.push({1,2,3})
        stack.push({'a': {'x': 1, 'y': 2}, 'b': 2})
        self. assertEqual(8, stack.get_size())
        self.assertEqual( {'a': {'x': 1, 'y': 2}, 'b': 2}, stack.peek(),)
        self.assertEqual( {'a': {'x': 1, 'y': 2}, 'b': 2}, stack.pop(),)
        self.assertEqual( 7, stack.get_size(),)
        self.assertEqual( {1, 2, 3}, stack.peek(),)
        item = stack.peek()
        item.add(4)
        self.assertEqual( {1, 2, 3}, stack.peek())
        queue = Homework_04.Queue()
        queue.push({'c': {'d': 1, 'e': 2}, 'f': 2})
        queue.push({10, 20, 30})
        queue.push([11, 22, 33])
        stack.push(queue)
        # self.assertEqual([{'c': {'d': 1, 'e': 2}, 'f': 2}, {10, 20, 30}, [11, 22, 33]],stack.peek().get_items())



    def test_Ex02(self):

        queue = Homework_04.Queue()
        self.assertTrue(queue.is_empty())
        with self.assertRaises(Exception):
            queue.pop()
        with self.assertRaises(Exception):
            queue.peek()
        queue.push({'a': {'x': 1, 'y': 2}, 'b': 2})
        queue.push({1, 2, 3})
        queue.push([1, 2, 3])
        queue.push((1, 2, 3))
        queue.push(10)
        queue.push(20.5)
        queue.push("Ana")
        queue.push(True)
        self.assertEqual(8, queue.get_size())
        self.assertEqual( {'a': {'x': 1, 'y': 2}, 'b': 2}, queue.peek(),)
        self.assertEqual( {'a': {'x': 1, 'y': 2}, 'b': 2}, queue.pop(),)
        self.assertEqual(7, queue.get_size(), )
        self.assertEqual( {1, 2, 3}, queue.peek(),)
        item = queue.peek()
        item.add(4)
        self.assertEqual( {1, 2, 3}, queue.peek(),)
        stack = Homework_04.Stack()
        stack.push({'c': {'d': 1, 'e': 2}, 'f': 2})
        stack.push({10, 20, 30})
        stack.push([11, 22, 33])
        queue_1 = Homework_04.Queue()
        queue_1.push(stack)
        self.assertEqual([{'c': {'d': 1, 'e': 2}, 'f': 2}, {10, 20, 30}, [11, 22, 33]], queue_1.peek().get_items())


    def test_Ex03(self):
        matrix_1 = Homework_04.Matrix(3, 4)
        matrix_1.set_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
        matrix_2 = Homework_04.Matrix(4, 3)
        matrix_2.set_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2]])

        self.assertEqual( [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]], matrix_1.get_matrix(),)
        self.assertEqual(3, matrix_1.get_rows())
        self.assertEqual(4, matrix_1.get_columns())
        self.assertEqual( 7, matrix_1.get_element(1, 2),)
        matrix_1.set_element(2, 3, 5)
        self.assertEqual(5, matrix_1.get_element(2, 3) )

        transposed_matrix_1 = matrix_1.transpose()
        expected_transposed = [[1, 5, 9], [2, 6, 0], [3, 7, 1], [4, 8, 5]]
        self.assertEqual(expected_transposed, transposed_matrix_1.get_matrix())

        multiplied_matrix = matrix_1 * matrix_2
        expected_multiplied = [[30, 40, 50], [78, 104, 130], [16, 31, 46]]
        self.assertEqual(expected_multiplied, multiplied_matrix.get_matrix())

        matrix_1.apply(lambda x: x + 1)
        expected_applied = [[2, 3, 4, 5], [6, 7, 8, 9], [10, 1, 2, 6]]
        self.assertEqual(expected_applied, matrix_1.get_matrix(),)

        with self.assertRaises(Exception):
            matrix_1.apply(lambda x : x / 0)

        with self.assertRaises(Exception):
            matrix_1.apply(lambda x : x + "Ana")

        with self.assertRaises(TypeError):
            matrix_1.set_element(1, 1, "Ana")

        with self.assertRaises(TypeError):
            matrix_1.set_element(1, 1, [1, 2, 3])

        with self.assertRaises(ValueError):
            matrix_1.set_element(-1, -2,  22)

        with self.assertRaises(ValueError):
            matrix_1.set_matrix([[1, 2], [5, 6], [9, 0, 1, 2]])

        matrix_3 = Homework_04.Matrix(3, 2)
        matrix_3.set_matrix([[1, 2], [5, 6], [9, 0]])
        with self.assertRaises(Exception):
            multiplied_matrix = matrix_1 * matrix_3





if __name__ == '__main__':
    unittest.main()
