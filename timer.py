import time
from abc import ABC
import beepy


"""
Stores and decrements a time.
"""


class Timer:
    def __init__(self, seconds=0):
        self.seconds = seconds

    def set_time(self, seconds=0):
        self.seconds = seconds

    def display_time(self):
        minutes, seconds = divmod(self.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds), end="\r")

    def countdown(self):
        if self.seconds <= 0:
            print("Timer not set properly: can't count down.")
        else:
            while self.seconds >= 0:
                self.display_time()
                time.sleep(1.0)
                self.seconds -= 1
            beepy.beep(sound="coin")
            print("Done!")


class TimerSetter(ABC):
    @staticmethod
    def set_time(timer):
        pass


class CLITimerSetter(TimerSetter):
    @staticmethod
    def set_time(timer):
        print("Set the timer:")
        # Get three separate values (hours, minutes, seconds)
        hours = int(input("Hours:   "))
        minutes = int(input("Minutes: "))
        seconds = int(input("Seconds: "))

        # Condense down into a single value (seconds)
        minutes += hours * 60
        seconds += minutes * 60

        timer.set_time(seconds)
