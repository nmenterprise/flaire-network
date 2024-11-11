from django.db import models


class TextModel(models.Model):
    clipboard = models.CharField(max_length=120)

    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
