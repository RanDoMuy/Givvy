from django.apps import AppConfig


class CryptoGiveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crypto_give'

    def ready(self):
        from . import updater
        updater.start()
