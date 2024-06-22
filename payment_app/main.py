from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from database import initialize_database
from payment_processor import PaymentProcessor

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
    initialize_database()
    PaymentAppApp().run()
