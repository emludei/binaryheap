# binaryheap
This is implementation of binary heap.

## Installing

```
pip install binaryheap
```

## Usage
To create a binary heap with minimum element in the root, use `new_min_heap` function. To create heap with maximum element in the root, use `new_max_heap` function. Each of this functions takes one positional parameter - list of the elements for building heap.
If you pass list of the elements to any of this functions, should remember that list will be use by binary heap. May be better to pass a copy of list.
```python
>>> from binaryheap import new_max_heap 
>>> data = [4, 1, 5, 8, 9, 88, -7]
>>> max_heap = new_max_heap(data)
>>> print(data)
[88, 9, 5, 8, 1, 4, -7]
>>> print([elem for elem in max_heap])
[88, 9, 8, 5, 4, 1, -7]
>>> print(data)
[]
```

Heap objects have following methods:
- `add(self, elem)`: Adds new element.
- `extract_n(self, count) -> list`: Extracts from heap N elements.
- `extract_one(self)`: Extracts one element from heap, if heap is empty, raises `EmptyHeapException` exception.
- `build(self, data)`: Builds binary heap with help of prepared list of elements. After that, this list will be used by heap, may be better to pass a copy of list.
- `clear(self)`: Removes all elements from heap.

```python
>>> from binaryheap import new_min_heap
>>> data = [5, 6, -6, -90, 123, 56]
>>> heap = new_min_heap(data.copy())
>>> print(data)
[5, 6, -6, -90, 123, 56]
>>> print(heap._heap)
[-90, 5, -6, 6, 123, 56]
>>> bool(heap)
True
>>> heap.extract_n(2)
[-90, -6]
>>> heap.add(-50)
>>> heap.extract_one()
-50
>>> heap.clear()
>>> bool(heap)
False
>>> heap.extract_one()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/user/projects/python/test/lib/python3.4/site-packages/binaryheap/core.py", line 46, in extract_one
    raise EmptyHeapException('%s is empty' % self.__class__.__name__)
binaryheap.core.EmptyHeapException: MinHeap is empty
>>> heap.extract_n(4)
[]
```
