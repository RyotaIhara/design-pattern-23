from ui_abstract_factory import Button, TextBox, UIFactory


class WindowsButton(Button):
    def render(self):
        print("🪟 Windows風ボタン")

class WindowsTextBox(TextBox):
    def render(self):
        print("🪟 Windows風テキストボックス")


class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_textbox(self):
        return WindowsTextBox()
