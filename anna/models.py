from django.db import models

# Create your models here.
class NewUser(models.Model):
    first_name = models.CharField(max_length=20, null=True, help_text="your name")
    last_name = models.CharField(max_length=20, null=True, help_text="your surname")
    phone_number = models.CharField(
        max_length=20, null=True, help_text="enter your mobile number here"
    )
    email = models.CharField(max_length=20, null=True, help_text="enter your Email")

    def __str__(self):
        return f'{self.last_name} {self.first_name}'