import time


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
        print("{:02d}:{:02d}".format(minutes, seconds), end='\r')

    def countdown(self):
        if self.seconds <= 0:
            print("Timer not set properly: can't count down.")
        else:
            while self.seconds >= 0:
                self.display_time()
                time.sleep(1.0)
                self.seconds -= 1
            print("Done!")
