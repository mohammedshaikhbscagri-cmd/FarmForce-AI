from app.config import settings


def send_sms(to: str, body: str) -> bool:
    """Send an SMS via Twilio. Returns True on success."""
    # TODO: Implement Twilio SMS sending
    # from twilio.rest import Client
    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # client.messages.create(body=body, from_=settings.TWILIO_PHONE, to=to)
    print(f"[SMS] To: {to} | Body: {body}")
    return True
