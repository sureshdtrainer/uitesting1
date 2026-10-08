import time
from unittest.mock import Mock


payment_service = Mock()

def slow_payment(value):
    time.sleep(5)
    return {"status": "success"}


payment_service.process_payment.side_effect = slow_payment


start = time.time()

response = payment_service.process_payment(100)

elapsed = time.time() - start

print("Response:", response)
print("Response time:", elapsed)
