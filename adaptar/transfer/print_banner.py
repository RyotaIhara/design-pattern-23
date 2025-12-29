# print_banner.py
from print import Print
from banner import Banner


class PrintBanner(Print):
    def __init__(self, text: str):
        self.banner = Banner(text)

    def print_weak(self) -> str:
        return self.banner.show_with_paren()

    def print_strong(self) -> str:
        return self.banner.show_with_aster()
