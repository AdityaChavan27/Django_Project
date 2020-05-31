from django.db import models

# Create your models here.
class login(models.Model):
    Name=models.CharField(max_length=30)
    Password = models.CharField(max_length=20)
    Email = models.EmailField(max_length=30)

    def __str__(self):
        return self.Name

class session(models.Model):
    session=models.CharField(max_length=30)

    def __str__(self):
        return self.session

class student(models.Model):
    name=models.CharField(max_length=30)
    session=models.ForeignKey("session",on_delete=models.PROTECT)

    def __str__(self):
        return self.name

