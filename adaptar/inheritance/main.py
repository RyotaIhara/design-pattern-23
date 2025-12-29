# main.py
from print_banner import PrintBanner


def main():
    print_banner = PrintBanner("Hello")
    print(print_banner.print_weak())
    print(print_banner.print_strong())


if __name__ == "__main__":
    main()
