#!/usr/bin/kivy
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import datetime
from kivy.storage.jsonstore import JsonStore
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.config import Config
Config.set('graphics', 'width', '920')
Config.set('graphics', 'height', '800')

class AppLayout(PageLayout):
    stored_data = ObjectProperty(None)
    twelveAM = ObjectProperty()
    _change = StringProperty()

    def __init__(self):

        super(AppLayout, self).__init__()
        self.stored_data = JsonStore('data.json')

    def todaysDate(self):
        return datetime.datetime.now()

    def DayOftheYear(self):
        date = datetime.datetime.strptime(str(self.todaysDate().date()), "%Y-%m-%d")
        jan1 = datetime.datetime.strptime(str(self.todaysDate().year) + "-01-01", "%Y-%m-%d")
        diff = date- jan1
        stringRep = str (diff.days+1)
        return stringRep

    def DaysLeft(self):
        date = datetime.datetime.strptime(str(self.todaysDate().date()), "%Y-%m-%d")
        dec31 = datetime.datetime.strptime(str(self.todaysDate().year) + "-12-31", "%Y-%m-%d")
        diff = dec31 - date
        stringRep = str(diff.days)
        return stringRep

    def DayintheUS(self):
        date = datetime.datetime.strptime(str(self.todaysDate().date()), "%Y-%m-%d")
        entryDate = datetime.datetime.strptime("2017-08-15", "%Y-%m-%d")
        diff = date - entryDate
        stringRep = str(diff.days)
        return stringRep

    def callback(self, evt=None):  # not sure if kivy sends event info so added optional arg just in case
        print(self.twelveAM.text)
        return self.add_widget(Label(text=self.twelveAM.text))


class EpochApp(App):

    time = StringProperty()
    date = StringProperty()

    def todaysDate(self, *args):
        self.time = str(datetime.datetime.now().strftime('%c'))
        self.date = str(datetime.datetime.now().date())


    def build(self):
        Clock.schedule_interval(self.todaysDate, 1)
        return AppLayout()

def main():
    EpochApp().run()

if __name__ == '__main__':
    main()

