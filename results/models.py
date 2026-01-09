from django.db import models

class Result(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="F.I.Sh.")
    university = models.CharField(max_length=100, verbose_name="Universitet")
    image = models.ImageField(upload_to='results/', verbose_name="Viza rasmi")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Viza natijasi"
        verbose_name_plural = "Viza natijalari"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.university}"
