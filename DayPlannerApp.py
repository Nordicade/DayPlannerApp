# Nicholas Nord
# created on July 7, 2019

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.config import Config
from kivy.core.window import Window

class UnderlyingGridLayout(GridLayout):
    pass

class DayPlannerApp(App):
    def build(self):
        return UnderlyingGridLayout()

Config.set('graphics','resizable',0)
Config.write()
Window.size = (600, 800)


if __name__ == "__main__":
    DayPlannerApp().run()
