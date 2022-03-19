from enum import ENUM


class IntervalType(ENUM):
    WORK = 1
    REST = 2


class Interval:
    def __init__(self, seconds, type):
        self.seconds = seconds
        self.type = type
