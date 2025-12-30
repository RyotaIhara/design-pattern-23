# main.py
from singleton import Singleton


def main():
    singleton = Singleton()
    singleton2 = Singleton()

    if singleton is singleton2:
        print("2つのインスタンスは同じです")
    else:
        print("2つのインスタンスは異なります")

if __name__ == "__main__":
    main()
