from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
Window.size = (300, 500)
screen_helper = """

ScreenManager:
    MainScreen:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    SecondScreen:
    CreateScreen:
    RegisterScreen:

<MainScreen>:
    name:'main'
    md_bg_color: 0, 1, 1, .5
    MDToolbar:
        title: "Login"
        specific_text_color: app.theme_cls.accent_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
    MDTextField:
        hint_text: "Enter password"
        helper_text: "or click on forgot password"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text: "Enter username"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'second'
    MDRectangleFlatButton:
        text: 'Register'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'register'
    MDRectangleFlatButton:
        text: 'Exit'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'second'
<RegisterScreen>:
    name:'register'
    MDToolbar:
        title: "Register"
        specific_text_color: app.theme_cls.accent_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
    MDTextField:
        hint_text: "Enter username"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text: "Enter NIC"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text: "Enter Email"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text: "Enter contact number"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Register'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'second'
<SecondScreen>:
    name: 'second'
    MDToolbar:
        title: "Welcome to the VJournal"
        specific_text_color: app.theme_cls.accent_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
    MDTextField:
        hint_text: "Enter username"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Create a journal'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'createnew'
    MDRectangleFlatButton:
        text: 'Use a exsisting one'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'createnew'
    MDRectangleFlatButton:
        text: 'Exit'
        on_press: root.manager.current = 'second'
    MDRectangleFlatButton:
        text: 'Upload a file'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'upload'
    MDRectangleFlatButton:
        text: 'View your profile'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'profile'

<CreateScreen>:
    name : 'createnew'
    MDToolbar:
        title: "Create a journal"
        specific_text_color: app.theme_cls.accent_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
<MenuScreen>:
    name: 'menu'
    MDToolbar:
        title: "View your details"
        specific_text_color: app.theme_cls.accent_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'upload'

<ProfileScreen>:
    name: 'profile'
    MDToolbar:
        title: "Personal details"
        specific_text_color: app.theme_cls.accent_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: 'upload'
    MDToolbar:
        title: "Upload a journal"
        specific_text_color: app.theme_cls.accent_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

"""


class MenuScreen(Screen):
    pass

class CreateScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SecondScreen(name='second'))
sm.add_widget(CreateScreen(name='createnew'))
sm.add_widget(CreateScreen(name='register'))

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
