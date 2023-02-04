from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols=1
        self.inside=GridLayout
        self.inside.cols=2

        # self.inside=RoundedButton@Button(background_color:(0,0,0,0))

        # shutdown button
        self.shtdwn=Button(text="SHUTDOWN PC ")
        self.shtdwn.bind(on_press=self.clickedShtdwn)
        self.add_widget(self.shtdwn)
        # restart button
        self.restart=Button(text="RESTART PC ")
        self.restart.bind(on_press=self.clickedRestart)
        self.add_widget(self.restart)
        # Sleep button
        self.sleep=Button(text="SLEEP PC ")
        self.sleep.bind(on_press=self.clickedSleep)
        self.add_widget(self.sleep)
        # log out button
        self.Logout=Button(text="LOG OUT")
        self.Logout.bind(on_press=self.clickedLogOff)
        self.add_widget(self.Logout)


        # binding a function to an event
    # Shutdown Function
    def clickedShtdwn(self,instance):
        shutdown=os.system("shutdown /s /t 2")
        print("shutdown command clicked"+shutdown)

    # Restart function
    def clickedRestart(self,instance):
        restart=os.system("shutdown /r /t 2")
        print("Restart Button Clicked"+restart)

    #Sleep Function
    def clickedSleep(self,instance):
        sleep=os.system("hibernet /h")
        print("Sleep Button Clicked"+sleep)

    #Log Off function
    def clickedLogOff(self,instance):
        logout=os.system("shutdown /l")
        print("Log out button clicked"+logout)

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    MyApp().run()
