from app.config import settings


class NotificationService:
    """Handles push, SMS, and WhatsApp notifications."""

    async def send_push(self, user_id: str, title: str, message: str) -> bool:
        """Send push notification via Firebase Cloud Messaging."""
        # TODO: Implement FCM push notification
        # import firebase_admin.messaging as fcm
        # fcm.send(fcm.Message(notification=fcm.Notification(title=title, body=message), topic=user_id))
        print(f"[PUSH] user={user_id} title={title}")
        return True

    async def send_sms(self, phone: str, message: str) -> bool:
        """Send SMS via Twilio."""
        # TODO: Implement Twilio SMS
        # from twilio.rest import Client
        # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # client.messages.create(body=message, from_=settings.TWILIO_PHONE, to=phone)
        print(f"[SMS] to={phone} message={message}")
        return True

    async def send_whatsapp(self, phone: str, message: str) -> bool:
        """Send WhatsApp message via Twilio WhatsApp API."""
        # TODO: Implement Twilio WhatsApp
        # from twilio.rest import Client
        # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # client.messages.create(
        #     body=message,
        #     from_=f"whatsapp:{settings.TWILIO_PHONE}",
        #     to=f"whatsapp:{phone}",
        # )
        print(f"[WHATSAPP] to={phone} message={message}")
        return True
