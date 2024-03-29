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

widget_count = 0
mouse_down_pos = 0
mouse_down = None
mouse_down_orig_hint = 0
multitouch = False
color_array = [[0, 1 , 1, .6], [0, 128/255, 0, .6], [192/255, 192/255, 192/255, .6], [1, 1, 0, .6],
 [128/255, 0, 128/255, .6], [128/255, 0, 0, .6], [0, 0, 1, .6]]

color_array_bold = [[0, 1 , 1, 1], [0, 128/255, 0, 1], [192/255, 192/255, 192/255, 1], [1, 1, 0, 1],
 [128/255, 0, 128/255, 1], [128/255, 0, 0, 1], [0, 0, 1, 1]]

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

class CustomLabels(Label):

    def __init__(self, activity_text, widget_number, am):
        #self.background_color = color_array_bold[widget_number % len(color_array_bold)]
        self.background_color = color_array[widget_number % len(color_array)]
        Label.__init__(self)
        self.text = activity_text
        self.number = widget_number
        self.pos = (0,0)
        print("widget#: "+str(widget_number)+" pos: "+str(self.pos)+" size: "+str(self.size))


    global widget_count
    global mouse_down
    widget_number = widget_count
    def build(self, activity_text):
        lbl = CustomLabels(text = activity_text)
        self.add_widget(lbl)

    def on_touch_move(self, touch):
        global multitouch
        global mouse_down_pos
        global mouse_down_orig_hint
        if multitouch is True:
            fractional_size_change = ( touch.pos[0] - mouse_down_pos ) / mouse_down.parent.parent.width
            new_size_hint = mouse_down_orig_hint + fractional_size_change
            print(new_size_hint)

            #check for offscreen
            if new_size_hint < 0.0128:
                mouse_down.size_hint_x = 0.0128
                return True
            elif mouse_down.pos[0] + (new_size_hint *mouse_down.parent.parent.width) >= mouse_down.parent.parent.width:
                pass
                return True
            else:
                mouse_down.size_hint_x = new_size_hint
                return True

        elif mouse_down is not None and mouse_down.collide_point(*touch.pos):
            print("move() touch:" +str(mouse_down.text) +" to new pos: "+ str(touch.pos[0]))

            #custom drag method ( smooth/accurate drag, but offsets on 1 movement)
            mouse_offset_from_pos = (mouse_down_pos) - mouse_down.pos[0]
            change_in_x = touch.pos[0] - (mouse_down_pos)
            mouse_down.pos = (mouse_down.pos[0] + (change_in_x), 0)
            mouse_down_pos = touch.pos[0]

            #check for offscreen
            if (mouse_down.pos[0] < 0):
                mouse_down.pos = (0,0)
            if (mouse_down.pos[0] + mouse_down.width >= mouse_down.parent.width):
                mouse_down.pos = (mouse_down.parent.width - mouse_down.width, 0)
            return True

    def on_touch_up(self, touch):
        global mouse_down
        global multitouch
        mouse_down = None
        multitouch = False
        print("touch_up")
        return True

    def on_touch_down(self, touch):
        global widget_count
        global mouse_down_pos
        global mouse_down
        global mouse_down_orig_hint
        global multitouch
        print("touch_down")

        if mouse_down is not None and not touch.is_double_tap:
            print("multitouch: self: "+ str(self.text))
            multitouch = True

        if self.collide_point(*touch.pos): #and (mouse_down is None):
            mouse_down = self
            mouse_down_orig_hint = self.size_hint_x
            if not(touch.is_double_tap):
                print("on_touch_down: " +str(self.text) +" current pos: "+ str(touch.pos[0]))
                mouse_down_pos = (touch.pos[0])
                return True

            elif touch.is_double_tap:
                print("double tap")
                activity_list_layout = self.parent.parent.parent.parent.ids['activity_list_layout']
                widget = CustomWidgets(self.text)
                activity_list_layout.add_widget(widget)
                widget.ids['partB'].text = self.text
                self.parent.remove_widget(self)
                mouse_down = None
                #widget_count = widget_count - 1
                return True

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
        lbl = CustomLabels(activity_text, widget_count, True)
        am_layout.add_widget(lbl)

class DayPlannerApp(App):
    def build(self):
        underlying_layout = CustomGridLayout()
        return underlying_layout

if __name__ == "__main__":
    DayPlannerApp().run()
