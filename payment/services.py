from .models import Payment

def create_payment(data):
    payment = Payment(**data)
    payment.full_clean()
    payment.save()
    return payment