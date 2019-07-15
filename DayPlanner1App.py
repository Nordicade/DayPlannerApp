# Nicholas Nord
# created on July 7, 2019

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

widget_count = 0

class CustomWidgets(StackLayout):
    def bump_activity(self):
        print(self.parent)

        grid_layout = self.parent
        grid_layout.remove_widget(self)
        print("bump_activity")


    def remove_activity(self):
        grid_layout = self.parent
        grid_layout.remove_widget(self)
        print("remove_activity")

    pass

class CustomGridLayout(GridLayout):
    def add_activity(self):
        global widget_count
        widget_count = widget_count + 1
        self.ids['activity_list_layout'].add_widget(CustomWidgets())
        print("add_activity")
    pass

class DayPlanner1App(App):
    def build(self):
        underlying_layout = CustomGridLayout()
        return underlying_layout


if __name__ == "__main__":
    DayPlanner1App().run()
