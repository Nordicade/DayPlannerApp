# Nicholas Nord
# created on July 7, 2019

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior

#if you ctrl+z to this point, you've gone too far

widget_count = 0
mouse_down = False
color_array = [[128/255, 0 , 0, 0], [0, 128/255, 0, 0], [0, 128/255, 128/255, 0], [1, 1, 0, 0],
 [128/255, 0, 128/255, 0], [1, 0, 0, 0], [0, 0, 1, 0]]

color_array_bold = [[0, 1 , 1, 1], [0, 128/255, 0, 1], [192/255, 192/255, 192/255, 1], [1, 1, 0, 1],
 [128/255, 0, 128/255, 1], [1, 0, 0, 1], [0, 0, 1, 1]]

c_label_arr = []

class CustomWidgets(StackLayout):
    def __init__(self, activity_text):
        StackLayout.__init__(self)
        self.textInput = activity_text
    def bump_activity(self):
        CustomGridLayout.display_activity(self)
        grid_layout = self.parent
        grid_layout.remove_widget(self)

    def remove_activity(self):
        grid_layout = self.parent
        grid_layout.remove_widget(self)
        print("remove_activity")

    pass

class CustomLabels(Label):
    mouse_down_x = 0
    def __init__(self, activity_text, widget_number, am):
        Label.__init__(self)
        self.text = activity_text
        self.number = widget_number
        self.am = am
        print(self.width)
        self.pos = (0,0)
        duration_arr = [12,1,2,3,4,5,6,7,8,9,10,11]
        self.duration = (duration_arr[(widget_number - 1)% 12], duration_arr[(widget_number) % 12])
        print("widget#: "+str(widget_number)+" pos: "+str(self.pos)+" size: "+str(self.size))


    global widget_count
    global mouse_down
    widget_number = widget_count
    def build(self, activity_text):
        lbl = CustomLabels(text = activity_text)
        self.add_widget(lbl)


    def on_touch_move(self, touch):
#        if self.collide_point(*touch.pos):
        if mouse_down is not None:
            global mouse_down_pos
            print(mouse_down_pos)
            print("move() touch:" +str(touch.pos[0]) +" to new pos: "+ str(touch.pos))
            mouse_offset_from_pos = (mouse_down_pos) - self.pos[0]
            change_in_x = touch.pos[0] - (mouse_down_pos)
            self.pos = (touch.pos[0] + change_in_x, 0)
            #check for offscreen
            print(self.parent.parent.parent.parent.width)
            if (self.pos[0] < 0):
                self.pos = (0,0)
            if (self.pos[0] + self.width >= self.parent.parent.parent.parent.width):
                self.pos = (800 - self.width, 0)
            return True

    def on_touch_up(self, touch):
        global mouse_down
        mouse_down = None

    def on_touch_down(self, touch):
        global widget_count
        global mouse_down_pos
        global mouse_down
        print(mouse_down)
        if self.collide_point(*touch.pos):
            mouse_down = self
            print("the text of the label that SHOULD move is: "  + str(self.text))
            if not(touch.is_double_tap):
                print("on_touch_down: " +str(self) +" to new pos: "+ str(touch.pos))
                mouse_down_pos = (touch.pos[0])
                print(mouse_down_pos)
                #return True
            else:
                print("on_touch_double_click: " + str(touch.pos) + " removing: " + str(self))
                print(self.text)
                activity_list_layout = self.parent.parent.parent.parent.ids['activity_list_layout']
                widget = CustomWidgets(self.text)
                activity_list_layout.add_widget(widget)
                widget.ids['partB'].text = self.text
                self.parent.remove_widget(self)
                widget_count = widget_count - 1
                return True
        else:
            print("self:" + str(self) + " pos: " + str(self.pos))

class CustomGridLayout(GridLayout):
    def add_activity(self):
        self.ids['activity_list_layout'].add_widget(CustomWidgets(" "))
        print("add_activity")

    def display_activity(self):
        global widget_count
        widget_count = widget_count + 1
        activity_text = self.ids['partB'].text
        underlying_layout = self.parent.parent.parent
        am_layout = underlying_layout.ids['am_layout']
        pm_layout = underlying_layout.ids['pm_layout']
        # add check to see whether am or pm (true or false)
        lbl = CustomLabels(activity_text, widget_count, True)
#        drag = DragLabel(lbl)
        am_layout.add_widget(lbl)
        if(len(c_label_arr) == 0):
            c_label_arr.append(lbl)
        else:
            for c_label in c_label_arr:
                x = c_label.duration
                print(x)

#class DragLabel(Label, DragBehavior):
#    def __init__(self,Label):
#       super(DragLabel, self).__init__()
#       self.drag_rect_width = self.x
#       self.drag_rect_height = self.y
#       self.drag_timeout = 10000000
#       self.drag_distance = 0
#    pass

class DayPlannerApp(App):
    def build(self):
        underlying_layout = CustomGridLayout()
        return underlying_layout


if __name__ == "__main__":
    DayPlannerApp().run()
