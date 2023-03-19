from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty

from db_connection import create_connection, close_connection

DB_HOST = "ec2-54-211-246-119.compute-1.amazonaws.com "
DB_USER = "remote_user"
DB_PASSWORD = "password"
DB_DATABASE = "volleyscore"


class TeamManagementScreen(Screen):
    teams = ListProperty([])

    def __init__(self, **kwargs):
        super(TeamManagementScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        header_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        header_label = Label(text='Team Management', font_size=24)
        header_layout.add_widget(header_label)
        back_button = Button(text='Back', size_hint=(0.2, 1))
        back_button.bind(on_press=self.go_back)
        header_layout.add_widget(back_button)
        layout.add_widget(header_layout)

        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.team_input = TextInput(hint_text='Enter team name', multiline=False)
        input_layout.add_widget(self.team_input)
        add_button = Button(text='Add team')
        add_button.bind(on_press=self.add_team)
        input_layout.add_widget(add_button)
        layout.add_widget(input_layout)

        self.team_list_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.team_list_layout.bind(minimum_height=self.team_list_layout.setter('height'))
        layout.add_widget(self.team_list_layout)

        self.update_team_list()

        self.add_widget(layout)

    def go_back(self, _):
        self.manager.current = 'home'

    def insert_team(self, connection, team_name):
        cursor = connection.cursor()
        query = "INSERT INTO teams (name) VALUES (%s)"
        values = (team_name,)

        try:
            cursor.execute(query, values)
            connection.commit()
            print(f"Team '{team_name}' inserted successfully.")
        except mysql.connector.Error as error:
            print(f"Failed to insert team '{team_name}': {error}")
        finally:
            cursor.close()

    def add_team(self, _):
        team_name = self.team_input.text.strip()
        if team_name and team_name not in self.teams:
            self.teams.append(team_name)
            self.update_team_list()

            connection = create_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE)
            if connection:
                self.insert_team(connection, team_name)
                close_connection(connection)

    def remove_team(self, team_name):
        if team_name in self.teams:
            self.teams.remove(team_name)
            self.update_team_list()

    def update_team_list(self):
        self.team_list_layout.clear_widgets()
        for team_name in self.teams:
            team_label = Label(text=team_name, size_hint_y=None, height=40)
            self.team_list_layout.add_widget(team_label)
            remove_button = Button(text='Remove', size_hint_y=None, height=40)
            remove_button.bind(on_press=lambda instance: self.remove_team(team_name))
            self.team_list_layout.add_widget(remove_button)


