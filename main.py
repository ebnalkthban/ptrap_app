from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import ThreeLineListItem, TwoLineListItem, OneLineListItem
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import controllers.logic as logic

KV = '''
ScreenManager:
    LoginScr:
    DashScr:
    InvScr:
    SalScr:
    SetScr:

<LoginScr>:
    name: 'login'
    MDBoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        spacing: "15dp"
        md_bg_color: 1, 1, 1, 1
        Image:
            source: 'assets/logo.png'
            size_hint: None, None
            size: "120dp", "120dp"
            pos_hint: {"center_x": .5}
        MDLabel:
            text: "PTRAP"
            halign: "center"
            font_style: "H4"
            theme_text_color: "Custom"
            text_color: 0.1, 0.6, 0.1, 1
            bold: True
        MDTextField:
            id: e
            hint_text: app.t('email')
            mode: "rectangle"
        MDTextField:
            id: p
            hint_text: app.t('pass')
            password: True
            mode: "rectangle"
        MDRaisedButton:
            text: app.t('log')
            md_bg_color: 0.1, 0.6, 0.1, 1
            pos_hint: {"center_x": .5}
            size_hint_x: 0.8
            on_release: root.do_l()
        MDFlatButton:
            text: app.t('reg')
            pos_hint: {"center_x": .5}
            on_release: root.do_r()

<DashScr>:
    name: 'dash'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "PTRAP - " + app.t('wel')
            md_bg_color: 0.1, 0.6, 0.1, 1
            left_action_items: [["logout", lambda x: root.logout()]]
        MDGridLayout:
            cols: 2
            padding: "20dp"
            spacing: "20dp"
            MDCard:
                on_release: root.manager.current = 'inv'
                orientation: 'vertical'
                padding: "10dp"
                MDIcon:
                    icon: "package-variant-closed"
                    halign: "center"
                    font_size: "48sp"
                    text_color: 0.1, 0.6, 0.1, 1
                    theme_text_color: "Custom"
                MDLabel:
                    text: app.t('inv')
                    halign: "center"
            MDCard:
                on_release: root.manager.current = 'sal'
                orientation: 'vertical'
                padding: "10dp"
                MDIcon:
                    icon: "cart"
                    halign: "center"
                    font_size: "48sp"
                    text_color: 0.1, 0.6, 0.1, 1
                    theme_text_color: "Custom"
                MDLabel:
                    text: app.t('sal')
                    halign: "center"
            MDCard:
                on_release: root.manager.current = 'set'
                orientation: 'vertical'
                padding: "10dp"
                MDIcon:
                    icon: "cog"
                    halign: "center"
                    font_size: "48sp"
                    text_color: 0.1, 0.6, 0.1, 1
                    theme_text_color: "Custom"
                MDLabel:
                    text: app.t('set')
                    halign: "center"

<InvScr>:
    name: 'inv'
    on_enter: root.load()
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: app.t('inv')
            md_bg_color: 0.1, 0.6, 0.1, 1
            left_action_items: [["arrow-left", lambda x: root.back()]]
            right_action_items: [["plus", lambda x: root.open_add()]]
        MDTextField:
            id: s
            hint_text: "Search..."
            on_text: root.load(self.text)
        ScrollView:
            MDList:
                id: l

<SalScr>:
    name: 'sal'
    on_enter: root.load()
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: app.t('sal')
            md_bg_color: 0.1, 0.6, 0.1, 1
            left_action_items: [["arrow-left", lambda x: root.back()]]
            right_action_items: [["cart-plus", lambda x: root.open_sale()]]
        ScrollView:
            MDList:
                id: l

<SetScr>:
    name: 'set'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: app.t('set')
            md_bg_color: 0.1, 0.6, 0.1, 1
            left_action_items: [["arrow-left", lambda x: root.back()]]
        MDList:
            OneLineListItem:
                text: "العربية"
                on_release: app.set_l('ar')
            OneLineListItem:
                text: "English"
                on_release: app.set_l('en')
            OneLineListItem:
                text: "Español"
                on_release: app.set_l('es')
            OneLineListItem:
                text: "Русский"
                on_release: app.set_l('ru')

<AddPop>:
    orientation: 'vertical'
    spacing: "10dp"
    size_hint_y: None
    height: "350dp"
    MDTextField:
        id: n
        hint_text: "Name"
    MDTextField:
        id: b
        hint_text: "Brand"
    MDTextField:
        id: buy
        hint_text: "Buy Price"
    MDTextField:
        id: sell
        hint_text: "Sell Price"
    MDTextField:
        id: st
        hint_text: "Stock"
    MDTextField:
        id: c
        hint_text: "Compatibility"

<SalePop>:
    orientation: 'vertical'
    spacing: "10dp"
    size_hint_y: None
    height: "200dp"
    MDTextField:
        id: pid
        hint_text: "Product ID"
    MDTextField:
        id: q
        hint_text: "Quantity"
    MDTextField:
        id: d
        hint_text: "Discount"
        text: "0"
'''

class AddPop(BoxLayout): pass
class SalePop(BoxLayout): pass

class LoginScr(Screen):
    def do_l(self):
        ok, msg = logic.login(self.ids.e.text, self.ids.p.text)
        if ok: self.manager.current = 'dash'
        else: Snackbar(text=msg).open()
    def do_r(self):
        ok, msg = logic.register(self.ids.e.text, self.ids.p.text)
        Snackbar(text=msg).open()

class DashScr(Screen):
    def logout(self): self.manager.current = 'login'

class InvScr(Screen):
    d = None
    def back(self): self.manager.current = 'dash'
    def load(self, q=None):
        self.ids.l.clear_widgets()
        for p in logic.get_prods(q):
            self.ids.l.add_widget(ThreeLineListItem(text=f"ID:{p[0]} | {p[1]}", secondary_text=f"{p[2]} | {p[5]}$", tertiary_text=f"Stock:{p[6]} | {p[7]}"))
    def open_add(self):
        self.content = AddPop()
        self.d = MDDialog(title="Add", type="custom", content_cls=self.content, buttons=[MDFlatButton(text="Cancel", on_release=lambda x: self.d.dismiss()), MDFlatButton(text="Save", on_release=self.save)])
        self.d.open()
    def save(self, *a):
        c = self.content
        logic.add_prod(c.ids.n.text, c.ids.b.text, "General", c.ids.buy.text, c.ids.sell.text, c.ids.st.text, c.ids.c.text)
        self.d.dismiss()
        self.load()

class SalScr(Screen):
    d = None
    def back(self): self.manager.current = 'dash'
    def load(self):
        self.ids.l.clear_widgets()
        for s in logic.get_sales():
            self.ids.l.add_widget(TwoLineListItem(text=f"{s[1]} x{s[2]}", secondary_text=f"Total: {s[3]}$ | {s[4]}"))
    def open_sale(self):
        self.content = SalePop()
        self.d = MDDialog(title="Sale", type="custom", content_cls=self.content, buttons=[MDFlatButton(text="Cancel", on_release=lambda x: self.d.dismiss()), MDFlatButton(text="Confirm", on_release=self.confirm)])
        self.d.open()
    def confirm(self, *a):
        c = self.content
        ok, msg = logic.process_sale(c.ids.pid.text, c.ids.q.text, c.ids.d.text)
        self.d.dismiss()
        self.load()
        Snackbar(text=msg).open()

class SetScr(Screen):
    def back(self): self.manager.current = 'dash'

class PTRAPApp(MDApp):
    lc = StringProperty('ar')
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.icon = 'assets/logo.png'
        return Builder.load_string(KV)
    def t(self, k): return logic.get_t(k)
    def set_l(self, c):
        logic.current_lang = c
        self.lc = c
        cur = self.root.current
        self.root.current = 'login'
        self.root.current = cur

if __name__ == '__main__':
    PTRAPApp().run()
