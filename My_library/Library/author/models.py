from django.db import models

class Author (models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    img = models.FileField(upload_to='author')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


