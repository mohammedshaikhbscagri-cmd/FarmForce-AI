import hashlib
import hmac
from decimal import Decimal

from app.config import settings
from app.core.exceptions import PaymentException


class PaymentService:
    """Handles Razorpay payment lifecycle."""

    def __init__(self):
        # TODO: Initialize Razorpay client
        # import razorpay
        # self.client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        pass

    def create_order(self, amount: Decimal, booking_id: str) -> dict:
        """Create a Razorpay order and return order details."""
        # TODO: Integrate Razorpay order creation
        # amount_paise = int(amount * 100)
        # order = self.client.order.create({
        #     "amount": amount_paise,
        #     "currency": "INR",
        #     "receipt": str(booking_id),
        # })
        # return order
        return {
            "id": f"order_placeholder_{booking_id}",
            "amount": int(amount * 100),
            "currency": "INR",
        }

    def verify_payment(self, order_id: str, payment_id: str, signature: str) -> bool:
        """Verify Razorpay payment signature."""
        message = f"{order_id}|{payment_id}"
        expected = hmac.new(
            settings.RAZORPAY_KEY_SECRET.encode(),
            message.encode(),
            hashlib.sha256,
        ).hexdigest()
        if not hmac.compare_digest(expected, signature):
            raise PaymentException("Invalid payment signature")
        return True

    def release_to_worker(self, payment_id: str, worker_upi: str, amount: Decimal) -> dict:
        """Release escrow payment to worker via Razorpay Route transfer."""
        commission = amount * Decimal(str(settings.PLATFORM_COMMISSION_RATE))
        worker_payout = amount - commission
        # TODO: Implement Razorpay Route transfer
        # transfer = self.client.payment.transfer(payment_id, [{
        #     "account": worker_upi,
        #     "amount": int(worker_payout * 100),
        #     "currency": "INR",
        # }])
        return {
            "transfer_id": f"transfer_placeholder_{payment_id}",
            "worker_payout": float(worker_payout),
            "commission": float(commission),
        }
