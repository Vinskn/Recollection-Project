from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.popup import Popup

from kivymd.app import MDApp

Window.size = (720, 1280)


class Pg_log(Screen):
    def __init__(self, **kwargs):
        super(Pg_log, self).__init__(**kwargs)
        self.database()

    def database(self):
        self.user = ["admin", "meta"]
        self.password = ["key", "yuki"]

    def search(self, array, key):
        for i in range(len(self.user)):
            if self.user[i] == array and self.password[i] == key:
                return i
        return -1

    def data(self):
        userName = self.ids.usrnme.text
        passwd = self.ids.pswd.text

        result = self.search(userName, passwd)

        if result != -1:
            self.manager.current = "Pg_main"
            self.ids.usrnme.text = ""
            self.ids.pswd.text = ""
        else:
            print("Tidak Ada")


class Pg_Siup(Screen):
    def signup(self):
        ambil_user = self.ids.su_usrnm.text
        ambil_pswd = self.ids.su_pswd.text

        pg_log_screen = self.manager.get_screen("Pg_log")
        pg_log_screen.database()
        pg_log_screen.user.append(ambil_user)
        pg_log_screen.password.append(ambil_pswd)

        Pop_siup().open()
        self.manager.current = "Pg_log"

        self.ids.su_usrnm.text = ""
        self.ids.su_pswd.text = ""


class Pop_siup(Popup):
    pass

class Pg_main(Screen):
    pass

class Pg_acc(Screen):
    pass


class ManageSCR(ScreenManager):
    pass


class RecollectionApp(MDApp):
    pass


RecollectionApp().run()
