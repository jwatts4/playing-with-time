from copy import deepcopy


class Queue:
    """Queue implemented with a python list"""

    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, data):
        self._queue.append(data)

    def dequeue(self):
        assert len(self._queue) > 0
        datum = self._queue.pop(0)
        return datum

    def is_empty(self):
        return len(self._queue) == 0

    def peek(self):
        assert len(self._queue) > 0
        datum = deepcopy(self._queue[0])
        return datum
