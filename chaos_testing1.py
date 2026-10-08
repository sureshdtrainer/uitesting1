from unittest.mock import Mock
import time

def call_payment_service(payment_service):
    response = payment_service.process_payment(100)
    return response


payment_service = Mock()

payment_service.process_payment.side_effect = Exception(
    "Payment service unavailable"
)

try:
    call_payment_service(payment_service)
except Exception as e:
    print("Application handled failure:", e)
