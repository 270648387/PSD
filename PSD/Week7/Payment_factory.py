from abc import ABC, abstractmethod

# Abstract base class
class Processor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Concrete payment processor for different classes
class PayPalPayment(Processor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class StripePayment(Processor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe"
    

class CreditCardPayment(Processor):
    def process_payment(self, amount):
        return f"Processing ${amount} via CreditCard"
    
class AfterpayPayment(Processor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Afterpay"
    
class ApplepayPayment(Processor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Applepay"
    
# Factory pattern: creates payment processor instances
class ProcessorFactory:
    _processors = {
        "paypal": PayPalPayment,
        "stripe": StripePayment,
        "creditcard": CreditCardPayment,
        "afterpay": AfterpayPayment
    }

    @staticmethod
    def create_processor(payment_method):
        processor_class = ProcessorFactory._processors.get(payment_method.lower())
        if not processor_class:
            raise ValueError(f"Unsupported payment method: {payment_method}")
        return processor_class()

# Adding new payment processor to factory easily
ProcessorFactory._processors["applepay"] = ApplepayPayment


# Singleton pattern: Payment gateway class
class PaymentGateway:   
    _instance = None  
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def checkout(self, payment_method, amount):
        processor = ProcessorFactory.create_processor(payment_method)
        return processor.process_payment(amount)
    

def checkout(payment_method, amount):
    gateway = PaymentGateway()
    return gateway.checkout(payment_method, amount)

#Print outcome
if __name__ == "__main__":
    print("=== Payment System Test ===")
    print(checkout("paypal", 100))
    print(checkout("creditcard", 200))
    print(checkout("afterpay", 300))
    print(checkout("applepay", 400))
        
