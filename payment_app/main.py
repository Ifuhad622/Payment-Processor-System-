import os
from kivy.config import Config

# Set environment variable for display
os.environ['DISPLAY'] = ':1'

# Optionally, configure Kivy to use Xvfb as the window provider
Config.set('kivy', 'window_backend', 'x11')  # or 'dummy' depending on your setup

# Import the rest of your application components
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import yaml
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import initialize_database
from payment_processor import PaymentProcessor

# Load environment variables from .env file
load_dotenv()

# Load configuration from config.yaml
with open('config/config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

DATABASE_FILE = config['database']['file']

class PaymentApp(BoxLayout):
    def __init__(self, **kwargs):
        super(PaymentApp, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.processor = PaymentProcessor()

        self.add_widget(Label(text="User Name:"))
        self.user_input = TextInput(multiline=False)
        self.add_widget(self.user_input)

        self.add_widget(Label(text="Amount Due:"))
        self.amount_due_input = TextInput(multiline=False)
        self.add_widget(self.amount_due_input)

        self.add_widget(Label(text="Payment Amount:"))
        self.payment_amount_input = TextInput(multiline=False)
        self.add_widget(self.payment_amount_input)

        self.result_label = Label(text="")
        self.add_widget(self.result_label)

        self.process_button = Button(text="Process Payment")
        self.process_button.bind(on_press=self.process_payment)
        self.add_widget(self.process_button)

    def process_payment(self, instance):
        user_name = self.user_input.text
        amount_due = float(self.amount_due_input.text)
        payment_amount = float(self.payment_amount_input.text)
        self.processor.make_payment(user_name, amount_due, payment_amount)
        self.result_label.text = f"Payment processed for {user_name}!"

class PaymentAppApp(App):
    def build(self):
        return PaymentApp()

if __name__ == '__main__':
    # Initialize database connection
    engine = create_engine(f'sqlite:///{DATABASE_FILE}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Pass configuration to initialize_database if needed
    initialize_database()  # Modify if initialize_database() requires arguments

    PaymentAppApp().run()
