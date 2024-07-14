from django.db import models
from django.core.mail import send_mail

# Create your models here.

class TextModel(models.Model):
    clipboard = models.CharField(max_length=120)

    def save(self, *args, **kwargs):
        subject = "New TextModel Created"
        message = f"the phrase is \"{self.clipboard}\" "
        recipient_list = ["emelieasadel@gmail.com"]
        send_mail(subject, message, None, recipient_list)

        print("done")
        super().save(*args, **kwargs)