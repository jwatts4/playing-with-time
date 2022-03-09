from timer import Timer



def main():
    t = Timer()
    num_seconds = int(input("Enter starting time (seconds): "))
    t.set_time(num_seconds)
    t.countdown()


if __name__ == "__main__":
    main()