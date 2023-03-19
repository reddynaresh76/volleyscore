from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class ScheduleScreen(Screen):

    def __init__(self, **kwargs):
        super(ScheduleScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        header_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        header_label = Label(text='Game Schedule', font_size=24)
        header_layout.add_widget(header_label)
        back_button = Button(text='Back', size_hint=(0.2, 1))
        back_button.bind(on_press=self.go_back)
        header_layout.add_widget(back_button)
        layout.add_widget(header_layout)

        schedule_layout = GridLayout(cols=3, spacing=10, size_hint_y=None)
        schedule_layout.bind(minimum_height=schedule_layout.setter('height'))
        
        # Example schedule data
        games = [
            {"team1": "Team A", "team2": "Team B", "time": "10:00"},
            {"team1": "Team C", "team2": "Team D", "time": "11:00"},
            {"team1": "Team E", "team2": "Team F", "time": "12:00"},
        ]
        
        for game in games:
            team1_label = Label(text=game["team1"], size_hint_y=None, height=40)
            schedule_layout.add_widget(team1_label)
            team2_label = Label(text=f"vs {game['team2']}", size_hint_y=None, height=40)
            schedule_layout.add_widget(team2_label)
            time_label = Label(text=game["time"], size_hint_y=None, height=40)
            schedule_layout.add_widget(time_label)
        
        layout.add_widget(schedule_layout)
        self.add_widget(layout)

    def go_back(self, _):
        self.manager.current = 'home'

