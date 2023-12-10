from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
Window.size = (720,1280)    

class Pg_log (Screen):
    def database (self):
        user = ['admin', 'meta']
        password = ['key', 'yuki']
        return user, password
    
    def search (self, array, key):
        arry_user, arry_pass = self.database()
        
        for i in range (len(arry_user)):
            if arry_user[i] == array and arry_pass[i] == key:
                return i
        return -1
    
    def data (self):
        userName = self.ids.usrnme.text
        passwd = self.ids.pswd.text

        result = self.search(userName, passwd)

        if result != -1:
            self.manager.current = 'Pg_main'
            self.ids.usrnme.text = ''
            self.ids.pswd.text = ''
        else:
            print('Tidak Ada')

class Pg_Siup (Screen):
    pass

class Pg_main (Screen): 
    pass

class ManageSCR (ScreenManager):
    pass

class RecollectionApp (App):
    pass

RecollectionApp().run()