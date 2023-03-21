import random


def main():
    maxval = get_random_nums(level())
    while True:
        try:
            user = int(input("Guess: "))
            if user == maxval:
                print("Just right!")
                break
            elif user > maxval:
                print("Too large!")
            elif user < maxval:
                print("Too small!")
        except:
            print("Guess value should be integer")


def level():
    while True:
        try:
            user = int(input("Level: "))
            return user
        except:
            print("Please Add only integer")


def get_random_nums(lvl):
    return random.randint(1, lvl)


if __name__ == "__main__":
    main()
