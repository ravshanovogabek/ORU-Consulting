# services/models.py
from django.db import models

class Service(models.Model):
    COLOR_CHOICES = [
        ('emerald', 'Yashil'),
        ('blue', 'Ko‘k'),
        ('rose', 'Qizil'),
        ('yellow', 'Sariq'),
        ('purple', 'Binafsha'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='emerald')

    def __str__(self):
        return self.title
