from random import randint

import time
import beepy


def display_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds), end="\r")


def countdown(seconds):
    if seconds <= 0:
        print("Timer not set properly: seconds must be positive")
    else:
        print("\nTIMER\n-----")
        work_interval = randint(10, 14)
        beepy.beep(sound="ready")
        print("\nWORK")

        while seconds >= 0:
            if work_interval >= 0:

                display_time(work_interval)
                work_interval -= 1
                seconds -= 1
                time.sleep(1.0)

            else:
                beepy.beep(sound="coin")
                print("\nBREAK")

                break_interval = 9

                while break_interval >= 0:
                    display_time(break_interval)
                    time.sleep(1.0)
                    break_interval -= 1

                work_interval = randint(100, 140)
                beepy.beep(sound="ready")
                print("\nWORK")


if __name__ == "__main__":
    sec = 600
    countdown(sec)
