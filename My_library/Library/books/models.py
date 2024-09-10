from django.db import models

from book_type.models import Book_type

from author.models import Author

from language.models import Language


class Book (models.Model):
    full_name = models.CharField(max_length=150, unique=True)
    img = models.FileField(upload_to='books')
    date = models.DateField(auto_now_add=True)
    type = models.ForeignKey(Book_type,on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(Language,on_delete=models.SET_NULL, null=True, blank=True)
    short_note = models.TextField()

    def __str__(self):
        return self.full_name
