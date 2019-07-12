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
        #top_layout = CustomStackLayout()
        #mid_layout = CustomBoxLayout()
        #bottom_layout = CustomAnchorLayout()
        #underlying_layout.add(top_layout)
        #underlying_layout.add(mid_layout)
        #underlying_layout.add(bottom_layout)
        return underlying_layout

if __name__ == "__main__":
    DayPlanner1App().run()
