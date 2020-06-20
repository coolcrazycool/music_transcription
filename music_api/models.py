from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile


class Melody(models.Model):
    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Converted', 'Converted')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    melody = models.FileField(upload_to="musics/%Y/%m/%d")
    name = models.CharField('Название мелодии', max_length=100, default='NoName')
    status = models.CharField(max_length=200, null=True, choices=STATUS, blank=True)
    pdf = models.FileField(upload_to="pdf/%Y/%m/%d", null=True, blank=True)

    def __str__(self):
        return self.name

# class PDF(models.Model):
#     melody = models.OneToOneField(Melody, on_delete=models.SET_NULL)
#     name = models.CharField
