# Import App and Builder (GUI)
from kivy.app import App
from kivy.lang import Builder
import requests

# Create the App
GUI = Builder.load_file('screen.kv')

# Create the build Function
class myApp(App):

    def build(self):
        return GUI

    def on_start(self):
        self.root.ids['CAD'].text = f"1 CAD = R${self.get_cotation('CAD')}"
        self.root.ids['USD'].text = f"1 USD = R${self.get_cotation('USD')}"

    def get_cotation(self, moeda):
        url = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        response = requests.get(url)
        content = response.json()
        cotation = content[f'{moeda}BRL']['bid']

        return cotation

# Run App
myApp().run()