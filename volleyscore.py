import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from teammanagement import TeamManagementScreen
from schedule_screen import ScheduleScreen


kivy.require('2.0.0')


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        welcome_label = Label(text='Welcome to VolleyScore', font_size=24)
        layout.add_widget(welcome_label)

        team_mgmt_btn = Button(text='Team Management', size_hint=(1, 0.2))
        team_mgmt_btn.bind(on_press=self.go_to_team_mgmt)
        layout.add_widget(team_mgmt_btn)
        
        schedule_btn = Button(text='Schedule', size_hint=(1, 0.2))
        schedule_btn.bind(on_press=self.go_to_schedule)
        layout.add_widget(schedule_btn)
        
        self.add_widget(layout)

    def go_to_team_mgmt(self, _):
        self.manager.current = 'team_mgmt'

    def go_to_schedule(self, _):
        self.manager.current = 'schedule'



class VolleyScoreApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(TeamManagementScreen(name='team_mgmt'))
        sm.add_widget(ScheduleScreen(name='schedule'))
        return sm


if __name__ == '__main__':
    VolleyScoreApp().run()
