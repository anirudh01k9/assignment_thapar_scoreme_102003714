import unittest
from main import longest_path

class TestLongestPath(unittest.TestCase):
    def test_graph1(self):
        graph1 = [
            [(1, 3), (2, 2)],
            [(3, 4)],
            [(3, 1)],
            []
        ]
        self.assertEqual(longest_path(graph1), 7)

    def test_graph2(self):
        graph2 = [
            [(1, 2), (2, 1)],
            [(3, 1)],
            [(3, 5)],
            []
        ]
        self.assertEqual(longest_path(graph2), 6)

    def test_graph3(self):
        graph3 = [
            [(1, 10)],
            [(2, 10)],
            [(3, 10)],
            []
        ]
        self.assertEqual(longest_path(graph3), 30)

    def test_graph4(self):
        graph4 = [
            [(1, 1), (2, 1)],
            [(3, 1)],
            [(3, 1)],
            []
        ]
        self.assertEqual(longest_path(graph4), 2)  

if __name__ == '__main__':
    unittest.main()
