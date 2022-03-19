import time
from abc import ABC
from queue import Queue
import beepy


class Timer:
    """
    A Timer consists of a queue of alternating WORK and REST intervals.

    When the timer is "started", it will dequeue the next interval and start its countdown method.
    Once the countdown method concludes, the next interval in the queue will be dequeued, and so on
    until the queue is empty and the timer is finished.
    """

    def __init__(self):
        current = None
        intervals = Queue()

    def setup_timer(self):
        pass

    def start(self):
        """
        If current is None:
            dequeue()
        Else:
            resume()
        """
        pass

    def stop(self):
        """
        End timer completely and exit the program.
        """
        pass

    def resume(self):
        """
        Resume the current interval.
        """
        pass

    def pause(self):
        """
        Pause the current interval.
        """
        pass
