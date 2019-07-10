# Nicholas Nord
# created on July 7, 2019

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout

class MyGrid(GridLayout) :
    def __init__(self, **keywordArgs):
        super(MyGrid, self).__init__(**keywordArgs)
        self.cols = 2
        self.rows = 2
        self.add_widget(Label(text="Name: "))
        self.add_widget(Label(text="Name: "))
        self.add_widget(Label(text="Name: "))
        self.add_widget(Label(text="Name: "))

class MyStack(StackLayout) :
    def __init__(self, **keywordArgs):
        super(MyStack, self).__init__(**keywordArgs)
        self.cols = 2
        self.rows = 2
        self.add_widget(Label(text="Name: "))
        self.add_widget(Label(text="Age: "))

class MyBox(BoxLayout) :
    def __init__(self, **keywordArgs):
        super(MyBox, self).__init__(**keywordArgs)
        self.cols = 2
        self.rows = 2
        self.add_widget(Label(text="Name: "))
        self.add_widget(Label(text="Age: "))

class UnderlyingGridLayout(GridLayout):
    pass

class DayPlannerApp(App):
    def build(self):
        return UnderlyingGridLayout()

if __name__ == "__main__":
    DayPlannerApp().run()
