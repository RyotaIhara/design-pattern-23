from ui_windows import WindowsUIFactory
from ui_mac import MacUIFactory
from ui_abstract_factory import UIFactory


def render_screen(factory: UIFactory):
    button = factory.create_button()
    textbox = factory.create_textbox()

    button.render()
    textbox.render()

if __name__ == "__main__":
    print("=== Windows UI ===")
    render_screen(WindowsUIFactory())

    print("\n=== Mac UI ===")
    render_screen(MacUIFactory())
