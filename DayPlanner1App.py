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
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

class CustomWidgets(Widget):
    c_w = ObjectProperty() #maybe do this for underlying_layout or CustomGridLayout instead of widget
    def bump_activity(self):
        print("bump_activity - CustomWidgets Method")
        #self.ids['activity_list_layout'].add_widget(CustomWidgets())
    pass

class CustomGridLayout(GridLayout):
    def bump_activity(self):
        print("bump_activity")

    def add_activity(self):
        print("add_activity")
        self.ids['activity_list_layout'].add_widget(CustomWidgets())
        #https://stackoverflow.com/questions/46984515/kivy-adding-buttons-in-a-sub-layout-when-a-button-is-pressed-on-release
        #should eventually have CustomGridLayout empty and CustomWidgets should hold these activity functions

    def modify_activity(self):
        print("modify_activity")

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
