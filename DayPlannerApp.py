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

#if you ctrl+z to this point, you've gone too far

widget_count = 0
color_array = [[128/255, 0 , 0, 0], [0, 128/255, 0, 0], [0, 128/255, 128/255, 0], [1, 1, 0, 0],
 [128/255, 0, 128/255, 0], [1, 0, 0, 0], [0, 0, 1, 0]]

color_array_bold = [[128/255, 0 , 0, 1], [0, 128/255, 0, 1], [0, 128/255, 128/255, 1], [1, 1, 0, 1],
 [128/255, 0, 128/255, 1], [1, 0, 0, 1], [0, 0, 1, 1]]

class CustomWidgets(StackLayout):
    def bump_activity(self):
        global widget_count
        widget_count = widget_count + 1
        CustomGridLayout.display_activity(self)
        grid_layout = self.parent
        if widget_count <= 24:
            grid_layout.remove_widget(self)
            print("bump_activity")
        else:
            print("Schedule Full!")

    def remove_activity(self):
        grid_layout = self.parent
        grid_layout.remove_widget(self)
        print("remove_activity")

    pass

class CustomLabels(Label):
    global widget_count
    widget_number = widget_count
    def build(self, activity_text):
        #widget_number = number
        #print("building label: " + activity_text + " onto " + str(self))
        lbl = CustomLabels(text = activity_text, size_hint_x = .083)
        self.add_widget(lbl)

    def on_pos(self, *args):
        print("on_pos= " +str(self) + " is pasted onto " + str(self.parent) + " which has children# = " + str(len(self.parent.children)))
        index = 1
        self.canvas.before.clear()
        with self.canvas.before:
            for c_label in self.parent.children:
                selected_color = color_array_bold[index % len(color_array_bold)]
                r_color = selected_color[0]
                g_color = selected_color[1]
                b_color = selected_color[2]
                Color(r_color, g_color, b_color, .5)
                Rectangle(pos=self.pos, size=self.size)
                #print("recolored for widget#: " + str(index)+ " has a pos of: " + str(self.pos) + " has a size of :" + str(self.size))
                #print("r:" + str(r_color) + " g:"+ str(g_color) + " b:" + str(b_color))
                index = index + 1


    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            print("on_touch_move: " + str(touch.pos))

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if not(touch.is_double_tap):
                print("on_touch_down: " + str(touch.pos))
            else:
                print("on_touch_double_click: " + str(touch.pos) + " removing: " + str(self))
                #self is the custom label
                self.parent.remove_widget(self)

class CustomGridLayout(GridLayout):
    def add_activity(self):
        self.ids['activity_list_layout'].add_widget(CustomWidgets())
        print("add_activity")

    def display_activity(self):
        activity_text = self.ids['partB'].text
        underlying_layout = self.parent.parent.parent
        am_layout = underlying_layout.ids['am_layout']
        pm_layout = underlying_layout.ids['pm_layout']
        if(len(am_layout.children) < 12):
            CustomLabels.build(am_layout, activity_text)
        else:
            if(len(am_layout.children) + len(pm_layout.children) < 24):
                CustomLabels.build(pm_layout, activity_text)

class DayPlannerApp(App):
    def build(self):
        underlying_layout = CustomGridLayout()
        return underlying_layout


if __name__ == "__main__":
    DayPlannerApp().run()
