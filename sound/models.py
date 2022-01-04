from django.db import models

class Sound(models.Model):
    name = models.CharField(max_length=70, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="images")
    audio = models.FileField(blank=True, null=True, upload_to="audios")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
