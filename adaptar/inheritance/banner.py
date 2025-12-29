# banner.py


class Banner:

    def __init__(self, text: str):
        self.text = text

    def show_with_paren(self) -> str:
        return f"({self.text})"

    def show_with_aster(self) -> str:
        return f"*{self.text}*"
