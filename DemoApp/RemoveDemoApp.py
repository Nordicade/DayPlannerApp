#File name: DemoApp.py

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

class CustomGridLayout(GridLayout):

    def add_list_item(self):
        print("add list item - CustomGridLayout")
        self.ids['list_layout'].add_widget(CustomWidgets())

    def remove_list_item(self):
        print("remove list item - CustomGridLayout")
        self.ids['list_layout'].remove_widget(CustomWidgets())

    pass

class CustomWidgets(Widget):
    def bump_activity(self):
        print("add list item - CustomWidgets")

    def remove_list_item(self):
        print("add list item - CustomGridLayout")
        self.ids['list_layout'].remove_widget(CustomWidgets())

    pass

class DemoApp(App):
    def build(self):
        underlying_layout = CustomGridLayout()
        return underlying_layout

if __name__ == "__main__":
    DemoApp().run()
