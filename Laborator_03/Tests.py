import unittest
import Homework_03


class MyHomeworkTestCase(unittest.TestCase):
    def test_Ex1(self):
        a = [1, 2, 3, 4]
        b = [3, 4, 5, 6]
        result = Homework_03.ex_01(a, b)
        self.assertEqual(result[0], {3, 4})  # Intersecția
        self.assertEqual(result[1], {1, 2, 3, 4, 5, 6})  # Reuniunea
        self.assertEqual(result[2], {1, 2})  # Diferența a - b
        self.assertEqual(result[3], {5, 6})  # Diferența b - a

    def test_Ex2(self):
        a = "Ana has apples."
        result = Homework_03.ex_02(a)
        expected_result = {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
        self.assertEqual(expected_result, result)
        self.assertEqual(Homework_03.ex_02(""), {})
        self.assertEqual(Homework_03.ex_02("aaa"), {'a': 3})

    def test_Ex3(self):

        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'b': 2, 'a': 1, 'c': 3}
        self.assertTrue(Homework_03.ex_03(d1, d2))

        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': 1, 'c': 4, 'b': 2}
        self.assertFalse(Homework_03.ex_03(d1, d2))

        d1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
        d2 = {'a': 1, 'b': {'x': 10, 'y': 20}}
        self.assertTrue(Homework_03.ex_03(d1, d2))

        d1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
        d2 = {'a': 1, 'b': {'x': 10, 'y': 21}}
        self.assertFalse(Homework_03.ex_03(d1, d2))

        d1 = {'a': [1, 2, 3], 'b': 2}
        d2 = {'a': [1, 4, 3], 'b': 2}
        self.assertFalse(Homework_03.ex_03(d1, d2))

        d1 = {'a': {1, 2, 3}, 'b': 2}
        d2 = {'a': {1, 2, 3}, 'b': 2}
        self.assertTrue(Homework_03.ex_03(d1, d2))

        d1 = {'a': [1, {'x': 10}], 'b': (2, 3)}
        d2 = {'a': [1, {'x': 10}], 'b': (2, 3)}
        self.assertTrue(Homework_03.ex_03(d1, d2))

        d1 = {'a': [1, {'x': 10}], 'b': (2, 3)}
        d2 = {'a': [1, {'x': 10}], 'b': (2, 3)}
        self.assertTrue(Homework_03.ex_03(d1, d2))

        d1 = {'a': [1, [2, 3]], 'b': 2}
        d2 = {'a': [1, [2, 3]], 'b': 2}
        self.assertTrue(Homework_03.ex_03(d1, d2))

        d1 = {'a': [1, [2, 3]], 'b': 2}
        d2 = {'a': [1, [2, 4]], 'b': 2}
        self.assertFalse(Homework_03.ex_03(d1, d2))

        d1 = {'a': {(1, 2), (3, 4)}, 'b': 2}
        d2 = {'a': {(3, 4), (1, 2)}, 'b': 2}
        self.assertTrue(Homework_03.ex_03(d1, d2))

        d1 = {'a': {(1, 2), (3, 4)}, 'b': 2}
        d2 = {'a': {(1, 2), (3, 5)}, 'b': 2}
        self.assertFalse(Homework_03.ex_03(d1, d2))

        d1 = {'a': [1, {'x': 10, 'y': 20}], 'b': 2}
        d2 = {'a': [1, {'y': 20, 'x': 10}], 'b': 2}
        self.assertTrue(Homework_03.ex_03(d1, d2))

        d1 = {'a': [1, {'x': 10, 'y': 20}], 'b': 2}
        d2 = {'a': [1, {'x': 10, 'y': 21}], 'b': 2}
        self.assertFalse(Homework_03.ex_03(d1, d2))

        d1 = {'a': {'x': [1, 2, 3], 'y': 4}, 'b': 2}
        d2 = {'a': {'y': 4, 'x': [1, 2, 3]}, 'b': 2}
        self.assertTrue(Homework_03.ex_03(d1, d2))

        d1 = {'a': {'x': [1, 2, 3], 'y': 4}, 'b': 2}
        d2 = {'a': {'y': 4, 'x': [1, 2, 4]}, 'b': 2}
        self.assertFalse(Homework_03.ex_03(d1, d2))

    def test_Ex4(self):
        result = Homework_03.ex_04("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
        expected_result = '<a href="http://python.org" class="my-link" id="someid">Hello there</a>'
        self.assertEqual(result, expected_result)

        result = Homework_03.ex_04("p", "This is a paragraph.")
        expected_result = '<p>This is a paragraph.</p>'
        self.assertEqual(result, expected_result)

        result = Homework_03.ex_04("img", "", src="image.png")
        expected_result = '<img src="image.png">'
        self.assertEqual(result, expected_result)

        inner_result = Homework_03.ex_04("b", "bold text")
        result = Homework_03.ex_04("p", "This is a paragraph with " + inner_result)
        expected_result = '<p>This is a paragraph with <b>bold text</b></p>'
        self.assertEqual(result, expected_result)

        result = Homework_03.ex_04("p", "5 > 4 and 3 < 5")
        expected_result = '<p>5 > 4 and 3 < 5</p>'
        self.assertEqual(result, expected_result)

    def test_Ex5(self):
        self.assertFalse(Homework_03.ex_05({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                                           {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))

        self.assertTrue(Homework_03.ex_05({("key1", "", "inside", ""), ("key2", "start", "middle", "end")},
                                          {"key1": "come inside, it's too cold out",
                                           "key2": "start something middle end"}))

        self.assertTrue(Homework_03.ex_05({("key1", "", "", ""), ("key2", "", "", "")}, {"key1": "", "key2": ""}))
        self.assertFalse(Homework_03.ex_05({("key1", "", "middle", "")}, {"key1": "middle at the start"}))
        self.assertFalse(Homework_03.ex_05({("key1", "", "middle", "")}, {"key1": "at the end middle"}))
        self.assertFalse(Homework_03.ex_05({("key1", "a", "aba","a")}, {"key1":"aba"}))
        self.assertTrue(Homework_03.ex_05({("key1", "a", "aba","a")}, {"key1":"aabaa"}))
        self.assertTrue(Homework_03.ex_05({("key1", "a", "aba","ba")}, {"key1":"aababa"}))
        self.assertTrue(Homework_03.ex_05({("key1", "", "", ""), ("key2", "", "", "")}, {"key1": "Hello", "key2": "Ana"}))
        self.assertFalse(Homework_03.ex_05({("key1", "", "middle", "")}, {"key1": "middlevalue"}))
        self.assertFalse(Homework_03.ex_05({("key1", "", "middle", "")}, {"key1": "valuemiddle"}))
        self.assertTrue(Homework_03.ex_05({("key1", "start", "", "end")}, {"key1": "startsomethingend"}))
        self.assertTrue(Homework_03.ex_05({("key1", "abc", "bcd", "cde")}, {"key1": "abcbcdcde"}))
        self.assertTrue(Homework_03.ex_05({("key1", "abc", "bcd", "cde")}, {"key1": "abcxxxbcdcde"}))
        self.assertTrue(Homework_03.ex_05({("key1", "", "@#$%", "")}, {"key1": "value@#$%value"}))
        self.assertTrue(Homework_03.ex_05({("key1", "abc", "ab", "de")}, {"key1": "abcxxabde"}))
        self.assertTrue(Homework_03.ex_05({("key1", "", "", "")}, {"key1": "anything"}))
        self.assertTrue(Homework_03.ex_05({("key1", "", "middle", "")}, {"key1": "valuemiddlevaluemiddlevalue"}))

    def test_Ex6(self):
        self.assertEqual(Homework_03.ex_06([1, 2, 3, 1, 2, 4, 3]), (4, 3))
        self.assertEqual(Homework_03.ex_06([1, 2, 3, 4, 5]), (5, 0))
        self.assertEqual(Homework_03.ex_06([1, 1, 1, 1, 1]), (1, 4))
        self.assertEqual(Homework_03.ex_06([]), (0, 0))
        self.assertEqual(Homework_03.ex_06([1, 2, 3, 4, 1, 2, 3, 4, 5]), (5, 4))
        self.assertEqual(Homework_03.ex_06(["apple", "banana", "cherry", "apple", "cherry"]), (3, 2))
        self.assertEqual(Homework_03.ex_06([1, 2, 3, "apple", 4, "banana"]), (6, 0))

    def test_Ex7(self):
        result = Homework_03.ex_07({1, 2}, {2, 3})
        expected = {
            "{1, 2} | {2, 3}": {1, 2, 3},
            "{1, 2} & {2, 3}": {2},
            "{1, 2} - {2, 3}": {1},
            "{2, 3} - {1, 2}": {3}
        }
        self.assertEqual(result, expected)

        result = Homework_03.ex_07({1, 2}, {2, 3}, {3, 4})
        expected = {
            "{1, 2} | {2, 3}": {1, 2, 3},
            "{1, 2} & {2, 3}": {2},
            "{1, 2} - {2, 3}": {1},
            "{2, 3} - {1, 2}": {3},
            "{1, 2} | {3, 4}": {1, 2, 3, 4},
            "{1, 2} & {3, 4}": set(),
            "{1, 2} - {3, 4}": {1, 2},
            "{3, 4} - {1, 2}": {3, 4},
            "{2, 3} | {3, 4}": {2, 3, 4},
            "{2, 3} & {3, 4}": {3},
            "{2, 3} - {3, 4}": {2},
            "{3, 4} - {2, 3}": {4},
        }
        self.assertEqual(result, expected)

        result = Homework_03.ex_07(set(), {1, 2})
        expected = {
            "{} | {1, 2}": {1, 2},
            "{} & {1, 2}": set(),
            "{} - {1, 2}": set(),
            "{1, 2} - {}": {1, 2}
        }
        self.assertEqual(result, expected)

    def test_Ex08(self):
        self.assertEqual(
            Homework_03.ex_08({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}),
            ['a', '6', 'z', '2']
        )

        self.assertEqual(
            Homework_03.ex_08({'start': 'a', 'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'a'}),
            ['a', 'b', 'c', 'd', 'e']
        )

        self.assertEqual(
            Homework_03.ex_08({'start': 'x', 'x': 'y', 'y': 'z', 'z': 'x'}),
            ['x', 'y', 'z']
        )

        self.assertEqual(
            Homework_03.ex_08({'start': '1', '1': '2', '2': '3', '3': '4', '4': '1'}),
            ['1', '2', '3', '4']
        )

        self.assertEqual(
            Homework_03.ex_08({'start': 'a', 'a': 'start'}),
            ['a']
        )

    def test_Ex09(self):
        self.assertEqual(Homework_03.ex_09(1, 2, 3, 4, x=1, y=2, z=3, w=5), 3)
        self.assertEqual(Homework_03.ex_09(1, 2, 3, 4, x=5, y=6, z=7, w=8), 0)
        self.assertEqual(Homework_03.ex_09(1, 2, 'a', 'b', x='a', y='b', z='c', w='d'), 2)
        self.assertEqual(Homework_03.ex_09(), 0)
        self.assertEqual(Homework_03.ex_09(1, 2, 3, x=4, y=5, z=6), 0)
        self.assertEqual(Homework_03.ex_09(1, 2, 3, x=1, y=2, z=3, a=4, b=5), 3)
        self.assertEqual(Homework_03.ex_09(1, 2, 3, 4, 5, x=1, y=2, z=3, w=5, v=4), 5)
        self.assertEqual(Homework_03.ex_09('a', 'b', 'c', x=1, y=2, z=3), 0)


if __name__ == '__main__':
    unittest.main()
