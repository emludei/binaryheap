import random
import unittest

from binaryheap import new_max_heap, new_min_heap
from binaryheap.core import EmptyHeapException


class TestHeap(unittest.TestCase):
    def check_heap(self, reverse=False):
        iterations = 1000
        heap_size = random.randint(10, 1000)

        for _ in range(iterations):
            test_list = [random.randint(-999999, 999999) for _ in range(heap_size)]

            if reverse:
                heap = new_max_heap(test_list.copy())
            else:
                heap = new_min_heap(test_list.copy())

            test_list.sort(reverse=reverse)

            for _ in range(heap_size // 2):
                test_item = test_list.pop(0)

                elem = heap.extract_one()

                self.assertEqual(test_item, elem)

            test_n_items = [test_list.pop(0) for _ in range(heap_size // 4)]

            self.assertEqual(test_n_items, heap.extract_n(heap_size // 4))

            self.assertEqual(test_list, [item for item in heap])

            self.assertRaises(EmptyHeapException, heap.extract_one)

    def test_max_heap(self):
        self.check_heap(True)

    def test_min_heap(self):
        self.check_heap()

    def test_clear(self):
        test_list = [random.randint(-99, 99) for _ in range(10)]
        heap = new_max_heap(test_list)
        heap.clear()

        self.assertFalse(heap)
