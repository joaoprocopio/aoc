import os

path = "/".join([os.path.dirname(__file__), "./input.txt"])
text = open(path, "r").read().split()


def main():
    return 0


if __name__ == "__main__":
    print(main())
