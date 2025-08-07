'''

Dependency Inversion Principle (DIP): 

High-level modules should not depend on low-level modules; both should depend on abstractions. 
Abstractions should not depend on details; details should depend on abstractions. 
This principle encourages decoupling between modules and promotes the use of abstractions/interfaces to reduce dependencies.

'''

class PaymentGateway:
    def process_payment(self):
        pass

class PayPal(PaymentGateway):
    def process_payment(self):
        print("Processing payment via PayPal")

class Stripe(PaymentGateway):
    def process_payment(self):
        print("Processing payment via Stripe")

class PaymentProcessor:
    def __init__(self, gateway):
        self.gateway = gateway
    
    def process(self):
        self.gateway.process_payment()


paypal_gateway = PayPal()
processor = PaymentProcessor(paypal_gateway)
processor.process()  # Outputs: Processing payment via PayPal

stripe_gateway = Stripe()
processor = PaymentProcessor(stripe_gateway)
processor.process()  # Outputs: Processing payment via Stripe
