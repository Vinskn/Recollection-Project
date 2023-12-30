from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.image import Image
#--------------------------------------------------------------------
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
#--------------------------------------------------------------------
from AppData import login as log
from AppData import signup as siup
#--------------------------------------------------------------------
Window.size = (720, 1280)


class Awal (Screen):
    pass

class Pg_log(Screen):
     def log_user (self):
        nama = self.ids.usrnme.text
        password = self.ids.pswd.text

        test = log(nama, password)
        if test != -1:
            self.manager.current = "Pg_main"
            self.ids.usrnme.text = ""
            self.ids.pswd.text = ""
        else:
            Pop_NF().open()
            self.ids.usrnme.text = ""
            self.ids.pswd.text = ""

class Pop_NF(MDDialog):
    pass

class Pg_Siup(Screen):
    def enter_data (self):
        ambil_user = self.ids.su_usrnm.text
        ambil_pswd = self.ids.su_pswd.text
        ambil_email = self.ids.email.text

        siup(ambil_user, ambil_pswd, ambil_email)
        Dialog_siup().open()
        self.manager.current = "Pg_log"

        self.ids.su_usrnm.text = ""
        self.ids.su_pswd.text = ""

class Dialog_siup(MDDialog):
    pass

class Pg_main(Screen):
    pass
    
class Pg_product(Screen):
    def pop_apre (self):
        Dialog_apre().open()

class Dialog_apre(MDDialog):
    pass

class Pg_acc(Screen):
    pass

class ManageSCR(ScreenManager):
    pass

class RecollectionApp(MDApp):
    pass


RecollectionApp().run()
