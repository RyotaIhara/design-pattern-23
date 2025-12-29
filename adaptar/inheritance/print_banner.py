# print_banner.py
from print import Print
from banner import Banner


class PrintBanner(Print, Banner):
    def __init__(self, text: str):
        Banner.__init__(self, text)

    def print_weak(self) -> str:
        return self.show_with_paren()

    def print_strong(self) -> str:
        return self.show_with_aster()
