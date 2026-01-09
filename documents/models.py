# apps/documents/models.py
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200, verbose_name="Hujjat nomi")
    description = models.TextField(verbose_name="Tavsifi")
    icon = models.CharField(max_length=10, default="📄", verbose_name="Emoji yoki Icon")

    def __str__(self):
        return self.title
