from enum import ENUM
from abc import ABC, abstractmethod


class Interval(ABC):
    """
    Abstract base class for different kinds of time intervals.
    """

    def __init__(self, seconds):
        self.seconds = seconds

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def countdown(self):
        pass


class MicroWorkInterval(Interval):
    pass


class MicroRestInterval(Interval):
    pass


class PomoWorkInterval(Interval):
    pass


class PomoRestInterval(Interval):
    pass
