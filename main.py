from pywinauto import Application


class App:
    def __init__(self, launch):
        self.launch = launch


class Window(App):
    def __init__(self, launch):
        self.window_exists = None
        super().__init__(launch)


def main():
    app = Window("notepad.exe")
    if app.window_exists:
        pass
    else:
        return Application().start(app.launch)


if __name__ == "__main__":
    main()
