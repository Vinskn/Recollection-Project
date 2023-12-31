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
import pandas as pd
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

        file_path = 'Database.csv'
        fcsv = pd.read_csv(file_path)
        self.take_user = fcsv['User'][test]
        self.take_mail = fcsv['Email'][test]

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
    def call_p1 (self):
        transfer =  self.manager.get_screen('Pg_product')
        transfer.produk_1()
    
    def call_p2 (self):
        transfer =  self.manager.get_screen('Pg_product')
        transfer.produk_2()

    def call_p3 (self):
        transfer =  self.manager.get_screen('Pg_product')
        transfer.produk_3()
    
class Pg_product(Screen):
    def pop_apre (self):
        Dialog_apre().open()
    
    def produk_1 (self):
        self.manager.current = 'Pg_product'
        self.ids.product_name.text = 'Catatan PRPL'
        self.ids.product_name.pos_hint = {'top': .6, 'center_x': .11}
        self.ids.product_desc.text = 'Ini adalah catatan materi mata kuliah Pengantar Rekayasa Perangkat Lunak \ntahun ajaran 2023 \nsemester satu (1) \nCatatan ini secara garis besar memberikan pemahaman mengenai...'
        self.ids.product_desc.pos_hint = {'top': .4, 'center_x': .5}

    def produk_2 (self):
        self.manager.current = 'Pg_product'
        self.ids.product_name.text = 'Catatan Dasar Pemrograman'
        self.ids.product_name.pos_hint = {'top': .6, 'center_x': .19}
        self.ids.product_desc.text = 'Ini adalah catatan materi mata kuliah Dasar Pemrograman \ntahun ajaran 2023-2024 \nsemester satu (1) \nCatatan ini secara garis besar memberikan pemahaman mengenai lorem ipsum....'
        self.ids.product_desc.pos_hint = {'top': .4, 'center_x': .5}

    def produk_3 (self):
        self.manager.current = 'Pg_product'
        self.ids.product_name.text = 'Catatan Kalkulus'
        self.ids.product_name.pos_hint = {'top': .6, 'center_x': .13}
        self.ids.product_desc.text = 'Ini adalah catatan materi mata kuliah Kalkulus \ntahun ajaran 2023 \nsemester satu (1) \nCatatan ini secara garis besar memberikan pemahaman mengenai lorem ....'
        self.ids.product_desc.pos_hint = {'top': .4, 'center_x': .5}


class Dialog_apre(MDDialog):
    pass

class Pg_acc(Screen):
#    def update_label_text(self):
#         self.ids.user_label.text = f"Username: {self.take_user}"
    pass

class ManageSCR(ScreenManager):
    pass

class RecollectionApp(MDApp):
    pass


RecollectionApp().run()
