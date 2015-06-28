from django.apps import AppConfig


class ReceiptAppConfig(AppConfig):
    name = 'quizme.receipt'

    def ready(self):
        # Register signals
        from .signals import email_receipt
