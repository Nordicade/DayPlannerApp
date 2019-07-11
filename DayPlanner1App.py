# Nicholas Nord
# created on July 7, 2019

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

class UnderlyingGridLayout(GridLayout):
    def __init__(self, **keywordArgs):
        super(UnderlyingGridLayout, self).__init__(**keywordArgs)
        self.cols = 1
        self.rows = 3
        #self.add_widget(Label(text="Name: "))
        #self.add_widget(Label(text="Age: "))
        #self.add_widget(BottomButton())

class CustomWidgets(Widget):
    pass

class CustomAnchorLayout(AnchorLayout):
    pass

class DayPlanner1App(App):
    def build(self):
        return CustomWidgets()


if __name__ == "__main__":
    DayPlanner1App().run()
