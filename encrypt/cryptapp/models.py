from django.db import models

# Create your models here.
class EncryptedText(models.Model):
    encrypted_text=models.BinaryField()