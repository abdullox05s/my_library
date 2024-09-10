from django.db import models


class Language (models.Model):
    name = models.CharField(max_length=50, unique=True)
    img = models.FileField(upload_to='language')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
