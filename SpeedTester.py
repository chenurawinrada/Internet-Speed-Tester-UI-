# from kivy.config import Config
# Config.set('graphics', 'resizable', False)
import time
import speedtest
import threading
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class SpeedTest(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        Window.size = [500, 600]
        screen = MDScreen()
        self.toolbar = MDToolbar(
                        title=""
                        )
        self.toolbar.pos_hint = {"top": 1}
        screen.add_widget(self.toolbar)
        lbl = MDLabel(
                    text="SPEED TEST",
                    halign="center",
                    theme_text_color="Custom",
                    text_color=(0, 1, 1, 1),
                    font_style="H1",
                    pos_hint={'center_x': 0.5, 'center_y': 0.7}
                    )
        screen.add_widget(lbl)
        self.lbl2 = MDLabel(
                        text="Download",
                        halign="center",
                        pos_hint={'center_x': 0.5, 'center_y': 0.45}
                        )
        screen.add_widget(self.lbl2)
        self.dmb = MDLabel(
                        halign="center",
                        pos_hint={'center_x': 0.5, 'center_y': 0.42}
                        )
        screen.add_widget(self.dmb)
        self.lbl3 = MDLabel(
                        text="Upload",
                        halign="center",
                        pos_hint={'center_x': 0.5, 'center_y': 0.35}
                        )
        screen.add_widget(self.lbl3)
        self.umb = MDLabel(
                        halign="center",
                        pos_hint={'center_x': 0.5, 'center_y': 0.32}
                        )
        screen.add_widget(self.umb)
        self.btn = MDRoundFlatButton(
                        text="Test",
                        font_style="H5",
                        pos_hint={'center_x': 0.5, 'center_y': 0.2},
                        on_release=self.thrfunc
                        )
        screen.add_widget(self.btn)

        return screen

    def thrfunc(self, obj):
        threading.Thread(target=self.butnfunc).start()

    def mbt(self, bytes):
        KB = 1024
        MB = KB * 1024
        return int(bytes/MB)

    def butnfunc(self):
        self.toolbar.title="Please Wait...."
        self.dmb.text = ''
        self.umb.text = ''
        time.sleep(1)
        try:
            self.toolbar.title = "Checking Download Speed...."
            self.dmb.text = str(f"{self.mbt(speedtest.Speedtest().download())} MB")
            self.toolbar.title = "Checking Upload Speed...."
            self.umb.text = str(f"{self.mbt(speedtest.Speedtest().upload())} MB")
            self.toolbar.title = "Done"
            time.sleep(2)
            lbt1 = self.dmb.text
            lbt2 = lbt1.replace(" MB", "")
            lbt3 = self.umb.text
            lbt4 = lbt3.replace(" MB", "")
            if int(lbt2) >= int(lbt4):
                self.toolbar.title = "Connection is fast!"
            else:
                self.toolbar.title = "Connection is low"
            self.btn.text = "Test Again"
            time.sleep(5)
            self.toolbar.title = ''
        except Exception as e:
            self.toolbar.title="[ERROR] " + str(e)
            self.btn.text = "Test Again"

if __name__ == '__main__':
    SpeedTest().run()
