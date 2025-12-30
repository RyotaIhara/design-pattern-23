from ui_abstract_factory import Button, TextBox, UIFactory


class MacButton(Button):
    def render(self):
        print("🍎 Mac風ボタン")

class MacTextBox(TextBox):
    def render(self):
        print("🍎 Mac風テキストボックス")


class MacUIFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_textbox(self):
        return MacTextBox()
