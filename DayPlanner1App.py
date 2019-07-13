# Nicholas Nord
# created on July 7, 2019

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

class CustomWidgets(Widget):
    pass

class CustomGridLayout(GridLayout):    
    def bump_activity(self):
        print("bump_activity")

    def add_activity(self):
        print("add_activity")

    pass

class CustomStackLayout(StackLayout):
    pass

class CustomBoxLayout(BoxLayout):
    pass

class CustomAnchorLayout(AnchorLayout):
    pass

class DayPlanner1App(App):
    def build(self):
        underlying_layout = CustomGridLayout()
        return underlying_layout


if __name__ == "__main__":
    DayPlanner1App().run()
