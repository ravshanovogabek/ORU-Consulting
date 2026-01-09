from django.db import models

class Contact(models.Model):
    phone_number = models.CharField(
        max_length=20,
        verbose_name="Telefon raqami"
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="Email"
    )

    class Meta:
        verbose_name = "Aloqa ma'lumoti"
        verbose_name_plural = "Aloqa ma'lumotlari"

    def __str__(self):
        return self.phone_number
