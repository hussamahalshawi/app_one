from kivy.app import App
from kivy.uix.label import Label

class BasicApp(App):
    # build: Initializes the application, it will be called once
    def build(self):
        body_layout = Label(text ="hello hussam")
        return body_layout


if __name__ == "__main__":
    app = BasicApp()
    app.run()
