from timer import Timer, CLITimerSetter


def main():
    t = Timer()
    CLITimerSetter.set_time(t)
    t.countdown()


if __name__ == "__main__":
    main()
