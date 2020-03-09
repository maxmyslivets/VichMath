from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from math import trunc
from kivymd.toast.kivytoast.kivytoast import toast

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        id: toolbar
        title: 'Vich Math'
        md_bg_color: app.theme_cls.primary_color
        elevation: 10
        right_action_items: [['media/visibility_off.png', lambda x: app.hide_press()]]
        pos_hint: {'top': 1}

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        padding: '10dp'

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            spacing: '10dp'
            orientation: "vertical"

            MDTextField:
                id: field_ur1
                hint_text: "Уравнение 1"
                helper_text: "Например: 2x+1y=7"
                helper_text_mode: "on_focus"
                pos_hint: {'center_x': .5, 'top': 1}
                #text: '2x+1y=7'
            
            MDTextField:
                id: field_ur2
                hint_text: "Уравнение 2"
                helper_text: "Например: 1x+3y=11"
                helper_text_mode: "on_focus"
                pos_hint: {'center_x': .5, 'bottom': 1}
                #text: '1x+3y=11'

    MDTabs:
        id: android_tabs
        tab_bar_height: toolbar.height


<Tab1>:
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'

            MDLabel:
                size_hint_y: None
                font_style: 'Subtitle2'
                theme_text_color: 'Primary'
                text: '1. На основе нижнего эквивалентного преобразования Шура получить последнее решение системы уравнений'

        ScrollView:
            id: scrl
            bar_width: '10dp'

            BoxLayout:
                size_hint_y: None
                height: root.height
            
                Image:
                    size_hint_x: None
                    width: self.parent.width
                    source: 'media/1.png'

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'
            spacing: '20dp'

            MDLabel:
                id: t1
                text: 'Вычислить...'
                font_style: 'Caption'

            MDFloatingActionButton:
                md_bg_color: app.theme_cls.primary_color
                elevation_normal: 10
                icon: 'media/swap_horiz.png'
                user_font_size: "24sp"
                pos_hint: {'center_y': .5, 'center_x': .5}
                on_release: t1.text = app.result(app.root.ids.field_ur1.text, app.root.ids.field_ur2.text, 1)

<Tab2>:
    BoxLayout:
        id: tb2
        orientation: 'vertical'

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'

            MDLabel:
                size_hint_y: None
                font_style: 'Subtitle2'
                theme_text_color: 'Primary'
                text: '2. На основе верхнего эквивалентного преобразования Шура получить первое решение системы уравнений'

        ScrollView:
            id: scrl
            bar_width: '10dp'

            BoxLayout:
                size_hint_y: None
                height: root.height
            
                Image:
                    size_hint_x: None
                    width: self.parent.width
                    source: 'media/2.png'
                
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'
            spacing: '20dp'

            MDLabel:
                id: t2
                text: 'Вычислить...'
                font_style: 'Caption'

            MDFloatingActionButton:
                md_bg_color: app.theme_cls.primary_color
                elevation_normal: 10
                icon: 'media/swap_horiz.png'
                user_font_size: "24sp"
                pos_hint: {'center_y': .5, 'center_x': .5}
                on_release: t2.text = app.result(app.root.ids.field_ur1.text, app.root.ids.field_ur2.text, 2)

<Tab3>:
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'

            MDLabel:
                size_hint_y: None
                font_style: 'Subtitle2'
                theme_text_color: 'Primary'
                text: 'На основе нижнего или верхнего эквивалентного преобразования Шура получить первое и второе решение системы уравнений'

        ScrollView:
            id: scrl
            bar_width: '10dp'

            BoxLayout:
                size_hint_y: None
                height: root.height
            
                Image:
                    size_hint_x: None
                    width: self.parent.width
                    source: 'media/3.png'
                
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'
            spacing: '20dp'

            MDLabel:
                id: t3
                text: 'Вычислить...'
                font_style: 'Caption'

            MDFloatingActionButton:
                md_bg_color: app.theme_cls.primary_color
                elevation_normal: 10
                icon: 'media/swap_horiz.png'
                user_font_size: "24sp"
                pos_hint: {'center_y': .5, 'center_x': .5}
                on_release: t3.text = app.result(app.root.ids.field_ur1.text, app.root.ids.field_ur2.text, 3)

<Tab4>:
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'

            MDLabel:
                size_hint_y: None
                font_style: 'Subtitle2'
                theme_text_color: 'Primary'
                text: 'На основе нижнего эквивалентного преобразования Жордана-Гаусса получить последний диагональный элемент обратной матрицы'

        ScrollView:
            id: scrl
            bar_width: '10dp'

            BoxLayout:
                size_hint_y: None
                height: root.height
            
                Image:
                    size_hint_x: None
                    width: self.parent.width
                    source: 'media/4.png'
                
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'
            spacing: '20dp'

            MDLabel:
                id: t4
                text: 'Вычислить...'
                font_style: 'Caption'

            MDFloatingActionButton:
                md_bg_color: app.theme_cls.primary_color
                elevation_normal: 10
                icon: 'media/swap_horiz.png'
                user_font_size: "24sp"
                pos_hint: {'center_y': .5, 'center_x': .5}
                on_release: t4.text = app.result(app.root.ids.field_ur1.text, app.root.ids.field_ur2.text, 4)

<Tab5>:
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'

            MDLabel:
                size_hint_y: None
                font_style: 'Subtitle2'
                theme_text_color: 'Primary'
                text: 'На основе верхнего эквивалентного преобразования Жордана-Гаусса получить первый диагональный элемент обратной матрицы'

        ScrollView:
            id: scrl
            bar_width: '10dp'

            BoxLayout:
                size_hint_y: None
                height: root.height
            
                Image:
                    size_hint_x: None
                    width: self.parent.width
                    source: 'media/5.png'
                
        BoxLayout: 
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'
            spacing: '20dp'

            MDLabel:
                id: t5
                text: 'Вычислить...'
                font_style: 'Caption'

            MDFloatingActionButton:
                md_bg_color: app.theme_cls.primary_color
                elevation_normal: 10
                icon: 'media/swap_horiz.png'
                user_font_size: "24sp"
                pos_hint: {'center_y': .5, 'center_x': .5}
                on_release: t5.text = app.result(app.root.ids.field_ur1.text, app.root.ids.field_ur2.text, 5)

<Tab6>:
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'

            MDLabel:
                size_hint_y: None
                font_style: 'Subtitle2'
                theme_text_color: 'Primary'
                text: 'На основе двойного эквивалентного преобразования Жордана-Гаусса получить все элементы обратной матрицы'

        ScrollView:
            id: scrl
            bar_width: '10dp'

            BoxLayout:
                size_hint_y: None
                height: root.height
            
                Image:
                    size_hint_x: None
                    width: self.parent.width
                    source: 'media/6.png'
                
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: '5dp'
            spacing: '20dp'

            MDLabel:
                id: t6
                text: 'Вычислить...'
                font_style: 'Caption'

            MDFloatingActionButton:
                md_bg_color: app.theme_cls.primary_color
                elevation_normal: 10
                icon: 'media/swap_horiz.png'
                user_font_size: "24sp"
                pos_hint: {'center_y': .5, 'center_x': .5}
                on_release: t6.text = app.result(app.root.ids.field_ur1.text, app.root.ids.field_ur2.text, 6)
'''


class Tab1(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
class Tab2(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
class Tab3(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
class Tab4(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
class Tab5(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
class Tab6(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class VichMatKR1App(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.android_tabs.add_widget(Tab1(text="1"))
        self.root.ids.android_tabs.add_widget(Tab2(text="2"))
        self.root.ids.android_tabs.add_widget(Tab3(text="3"))
        self.root.ids.android_tabs.add_widget(Tab4(text="4"))
        self.root.ids.android_tabs.add_widget(Tab5(text="5"))
        self.root.ids.android_tabs.add_widget(Tab6(text="6"))
    
    def result(self, ur, ur1, method):

        b1 = float(ur.split('=')[1])
        b2 = float(ur1.split('=')[1])
        N11 = float(ur[:ur.index('x')])
        N21 = float(ur1[:ur1.index('x')])
        N12 = float(ur[ur.index('x')+1:ur.index('y')])
        N22 = float(ur1[ur1.index('x')+1:ur1.index('y')])

        k = [N11, N12, N21, N22, b1, b2]

        for i in range(len(k)):
            if k[i]-trunc(k[i]) == 0:
                k[i] = int(k[i])
        
        if method == 1: return self.method_1(k[0], k[1], k[2], k[3], k[4], k[5])
        if method == 2: return self.method_2(k[0], k[1], k[2], k[3], k[4], k[5])
        if method == 3: return self.method_3(k[0], k[1], k[2], k[3], k[4], k[5])
        if method == 4: return self.method_4(k[0], k[1], k[2], k[3], k[4], k[5])
        if method == 5: return self.method_5(k[0], k[1], k[2], k[3], k[4], k[5])
        if method == 6: return self.method_6(k[0], k[1], k[2], k[3], k[4], k[5])


    def method_1(self, N11, N12, N21, N22, b1, b2):
        """На основе нижнего эквивалентного преобразования Шура
        получить последнее решение системы уравнений"""
        
        y = ((-N21/N11)*b1+1*b2) / ((-N21/N11)*N12+1*N22)

        if y-trunc(y) == 0:
            y = int(y)
        else:
            y = round(y, 3)
        
        if N21 >= 0:
            return 'y = ((-%s/%s)*%s+1*%s) / ((-%s/%s)*%s+1*%s) = %s' % (N21, N11, b1, b2, N21, N11, N12, N22, y)
        if N21 < 0:
            return 'y = ((%s/%s)*%s+1*%s) / ((%s/%s)*%s+1*%s) = %s' % (-N21, N11, b1, b2, -N21, N11, N12, N22, y)


    def method_2(self, N11, N12, N21, N22, b1, b2):
        """На основе верхнего эквивалентного преобразования Шура
        получить первое решение системы уравнений"""
        
        x = (1*b1+(-N12/N22)*b2) / (1*N11+(-N12/N22)*N21)

        if x-trunc(x) == 0:
            x = int(x)
        else:
            x = round(x, 3)

        if N22 >= 0:
            return 'x = (1*%s+(-%s/%s)*%s) / (1*%s+(-%s/%s)*%s) = %s' % (b1, N12, N22, b2, N11, N12, N22, N21, x)
        if N22 < 0:
            return 'x = (1*%s+(%s/%s)*%s) / (1*%s+(%s/%s)*%s) = %s' % (b1, -N12, N22, b2, N11, -N12, N22, N21, x)


    def method_3(self, N11, N12, N21, N22, b1, b2):
        """На основе нижнего или верхнего эквивалентного преобразования Шура
        получить первое и второе решение системы уравнений"""

        y = ((-N21/N11)*b1+1*b2) / ((-N21/N11)*N12+1*N22)

        if y-trunc(y) == 0:
            y = int(y)
        else:
            y = round(y, 3)
        
        x = (1/N11)*(b1-N12*y)

        if x-trunc(x) == 0:
            x = int(x)
        else:
            x = round(x, 3)
        
        return 'x = (1/%s)*(%s-%s*%s) = %s' % (N11, b1, N12, y, x)


    def method_4(self, N11, N12, N21, N22, b1, b2):
        """На основе нижнего эквивалентного преобразования Жордана-Гаусса
        получить последний диагональный элемент обратной матрицы"""
        
        q22 = (-N21/N11*N12+1*N22)**(-1)

        if q22-trunc(q22) == 0:
            q22 = int(q22)
        else:
            q22 = round(q22, 3)

        if N21 >= 0:
            return 'q22 = (-%s/%s*%s+%s)^-1 = %s' % (N21, N11, N12, N22, q22)
        if N21 < 0:
            return 'q22 = (%s/%s*%s+%s)^-1 = %s' % (-N21, N11, N12, N22, q22)


    def method_5(self, N11, N12, N21, N22, b1, b2):
        """На основе верхнего эквивалентного преобразования Жордана-Гаусса
        получить первый диагональный элемент обратной матрицы"""

        q11 = (1*N11-(N12/N22)*N21)**(-1)

        if q11-trunc(q11) == 0:
            q11 = int(q11)
        else:
            q11 = round(q11, 3)

        return 'q11 = (1*%s-(%s/%s)*%s)^-1 = %s' % (N11, N12, N22, N21, q11)

    def method_6(self, N11, N12, N21, N22, b1, b2):
        """На основе двойного эквивалентного преобразования Жордана-Гаусса
        получить все элементы обратной матрицы"""
        
        q22 = ((-N21/N11)*N12+1*N22)**(-1)

        if q22-trunc(q22) == 0:
            q22 = int(q22)
        else:
            q22 = round(q22, 3)
        
        q11 = (1*N11-(N12/N22)*N21)**(-1)

        if q11-trunc(q11) == 0:
            q11 = int(q11)
        else:
            q11 = round(q11, 3)
        
        q12 = (N12*q22) / -N11

        if q12-trunc(q12) == 0:
            q12 = int(q12)
        else:
            q12 = round(q12, 3)
        
        q21 = (1-N11*q11) / N12

        if q21-trunc(q21) == 0:
            q21 = int(q21)
        else:
            q21 = round(q21, 3)
        
        if N11 >= 0:
            return 'Q12 = (%s*%s) / -%s = %s\nQ21 = (1-%s*%s) / %s = %s\nQ11 = %s\nQ22 = %s' % (N12, q22, N11, q12, N11, q11, N12, q21, q11, q22)
        if N11 < 0:
            return 'Q12 = (%s*%s) / -%s = %s\nQ21 = (1-%s*%s) / %s = %s\nQ11 = %s\nQ22 = %s' % (N12, q22, -N11, q12, -N11, q11, N12, q21, q11, q22)

    def hide_press(self):
        toast('Удачно списать =)')


if __name__ == "__main__":
    VichMatKR1App().run()
