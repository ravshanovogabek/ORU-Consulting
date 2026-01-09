from django.db import models

class Interview(models.Model):
    student_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='interview_images/')
    youtube_link = models.URLField()

    def youtube_id(self):
        try:
            if "v=" in self.youtube_link:
                return self.youtube_link.split("v=")[1].split("&")[0]
            elif "youtu.be/" in self.youtube_link:
                return self.youtube_link.split("youtu.be/")[1]
            return None
        except:
            return None

    def __str__(self):
        return f"{self.student_name} - {self.country}"
