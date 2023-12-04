from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
Window.size = (720,1280)


class Pg_login (Screen):
    def database (self):
        user = ['admin',]
        pswd = ['key',]
        return user, pswd
    
    def data_scr (self):
        userName = self.ids.usrnme.text
        password = self.ids.pswd.text

        result = self.search(userName, password)

        if result != -1:
            pass
    
    def search (self, array, key):
        for i in range (len(array)):
            if array[i] == key:
                return i
        return -1

    
            
            

class Pg_main (Screen): 
    pass

class ManageSCR (ScreenManager):
    pass

class RecollectionApp (App):
    pass

RecollectionApp().run()