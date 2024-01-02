from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
#--------------------------------------------------------------------
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
#--------------------------------------------------------------------
from AppData import login as log
from AppData import signup as siup
from AppProduk import download_file as DF
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
            file_path = 'Database.csv'
            fcsv = pd.read_csv(file_path)
            app = App.get_running_app()
            app.take_user = self.take_user = fcsv['User'][test]
            app.take_mail = self.take_mail = fcsv['Email'][test]
            Clock.schedule_once(lambda dt: self.update_main_label(), 0.01)
            Clock.schedule_once(lambda dt: self.update_acc(), 0.01)

        else:
            Pop_NF().open()
            self.ids.usrnme.text = ""
            self.ids.pswd.text = ""
    
     def update_main_label(self):
        app = App.get_running_app()
        get_user = app.take_user
        self.manager.get_screen('Pg_main').ids.nama_main.text = f'Hallo, {get_user}'

     def update_acc (self):
        app = App.get_running_app()
        get_user = app.take_user
        get_mail = app.take_mail
        self.manager.get_screen('Pg_acc').ids.user_label.text = get_user
        self.manager.get_screen('Pg_acc').ids.nama_mail.text = get_mail    

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
        self.ids.Download_file.bind(on_press = self.downl_p1)

    def produk_2 (self):
        self.manager.current = 'Pg_product'
        self.ids.product_name.text = 'Catatan Dasar Pemrograman'
        self.ids.product_name.pos_hint = {'top': .6, 'center_x': .19}
        self.ids.product_desc.text = 'Ini adalah catatan materi mata kuliah Dasar Pemrograman \ntahun ajaran 2023-2024 \nsemester satu (1) \nCatatan ini secara garis besar memberikan pemahaman mengenai lorem ipsum....'
        self.ids.product_desc.pos_hint = {'top': .4, 'center_x': .5}
        self.ids.Download_file.bind(on_press = self.downl_p2)

    def produk_3 (self):
        self.manager.current = 'Pg_product'
        self.ids.product_name.text = 'Catatan Kalkulus'
        self.ids.product_name.pos_hint = {'top': .6, 'center_x': .13}
        self.ids.product_desc.text = 'Ini adalah catatan materi mata kuliah Kalkulus \ntahun ajaran 2023 \nsemester satu (1) \nCatatan ini secara garis besar memberikan pemahaman mengenai lorem ....'
        self.ids.product_desc.pos_hint = {'top': .4, 'center_x': .5}
        self.ids.Download_file.bind(on_press = self.downl_p3)

    def downl_p1 (self, instance):
        src = 'https://raw.githubusercontent.com/Vinskn/Recollection-Project/main/Storage/PRPL.txt'
        DF (src)

    def downl_p2 (self, instance):
        src = 'https://raw.githubusercontent.com/Vinskn/Recollection-Project/main/Storage/DasPro.txt'
        DF(src)

    def downl_p3 (self, instance):
        src = 'https://raw.githubusercontent.com/Vinskn/Recollection-Project/main/Storage/Kalkulus.txt'
        DF (src)

class Dialog_apre(MDDialog):
    pass

class Pg_acc(Screen):
    def balik (self):
        Dialog_exit().open()
        self.manager.current = 'Pg_log'

    def histo (self):
        Dialog_histo().open()

class Dialog_exit(MDDialog):
    pass

class Dialog_histo(MDDialog):
    pass

class ManageSCR(ScreenManager):
    pass

class RecollectionApp(MDApp):
    pass


RecollectionApp().run()
