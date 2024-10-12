from django.db import models


class User(models.Model):
    telegram_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=10, choices=[('uz', "O'zbek"), ('ru', "Русский")])

    def __str__(self):
        return self.name
