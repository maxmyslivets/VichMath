from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast.kivytoast.kivytoast import toast
from kivy.uix.screenmanager import Screen, ScreenManager
import os

KV = """
FloatLayout:
    orientation: 'vertical'

    MDTextField:
        id: text_field_error
        size_hint_x: .5
        hint_text: "Eneter key for activated"
        pos_hint: {'top': .7, 'center_x': .5}
    
    MDFloatingActionButton:
        md_bg_color: app.theme_cls.primary_color
        elevation_normal: 10
        icon: 'lock'
        user_font_size: "48sp"
        pos_hint: {'top': .3, 'center_x': .5}
        on_release: app.TestKey(app.root.ids.text_field_error.text)
"""

class ActivateApp(MDApp):

    def build(self):
        
        return Builder.load_string(KV)
    
    def TestKey(self, key):
        
        if key == '365':
            toast('Ok!')
            os.system('VichMath.py')
            ActivateApp().stop()
        else:
            toast('Error!')


if __name__ == "__main__":
    ActivateApp().run()