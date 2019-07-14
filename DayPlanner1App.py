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

widget_count = 0

class CustomWidgets(StackLayout):
    def bump_activity(self):
        CustomGridLayout.bump_activity(self)

    def on_parent(self, screen, parent):
        #print("rows: " + str(parent.rows))  #Rows = None, despite it adding for each new Custom Widget...?
        x = parent.parent
        pass

    pass

class CustomGridLayout(GridLayout):
    def bump_activity(self):
        # keep in mind, self is the CustomWidget
        global widget_count
        widget_count = widget_count - 1

        # set the height of ScrollView/GridLayout to be (widget_count * 100) + label_height
        grid_layout = self.parent
        grid_layout.height = (widget_count * 120) + 20  
        #list = self.ids['activity_list_layout']
        #scroll = list.ids['scroller']

        self.remove_widget(self.children[0])
        self.remove_widget(self.children[0])
        self.remove_widget(self.children[0])
        #x = CustomGridLayout.ids['activity_list_layout']
        print("bump_activity")

    def add_activity(self):
        # keep in mind, self is the CustomGridLayout
        global widget_count
        widget_count = widget_count + 1
        self.ids['activity_list_layout'].add_widget(CustomWidgets())
        print("add_activity")

    def modify_activity(self):
        print("modify_activity")

    pass

class DayPlanner1App(App):
    def build(self):
        underlying_layout = CustomGridLayout()
        return underlying_layout


if __name__ == "__main__":
    DayPlanner1App().run()
