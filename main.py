from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LockerApp(App):
    def build(self):
        self.clicks = 0
        layout = FloatLayout()
        
        self.label = Label(
            text="ХА ХА ХА лох повëлся\nкод Амир лох",
            font_size=24,
            halign="center",
            valign="middle",
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        self.label.bind(size=self.label.setter('text_size'))
        
        self.input = TextInput(
            hint_text="Введите код",
            multiline=False,
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        self.input.bind(text=self.check_code)
        
        layout.add_widget(self.label)
        layout.add_widget(self.input)
        
        btn = Button(
            opacity=0,
            size_hint=(0.3, 0.3),
            pos_hint={'center_x': 0.5, 'center_y': 0.8}
        )
        btn.bind(on_press=self.secret_tap)
        layout.add_widget(btn)
        
        return layout

    def check_code(self, instance, value):
        if value == "Амир лох":
            App.get_running_app().stop()

    def secret_tap(self, instance):
        self.clicks += 1
        if self.clicks >= 7:
            App.get_running_app().stop()

if __name__ == '__main__':
    LockerApp().run()
