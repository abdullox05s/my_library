from django.shortcuts import render

from .models import Book
from author.models import Author

from book_type.models import Book_type
from language.models import Language

#
def book (request):
    data = {
        'books':Book.objects.all(),
        'authors': Author.objects.all(),
        'languages':Language.objects.all(),
        'types':Book_type.objects.all(),
        "number": Book.objects.all().count()
    }
    return render (request,'library-main-page.html',data)


def author_filter (request,a):
    f = Author.objects.get(id=a)
    data = {
        'author_filter':Book.objects.filter(author=f),
        'authors': Author.objects.all(),
        'languages': Language.objects.all(),
        'types': Book_type.objects.all(),
        'number': Book.objects.filter(author=f).count()
    }

    return render(request, "author-filter.html", data)

def language_filter (request,a):
    f = Language.objects.get(id=a)
    data = {
        'language_filter':Book.objects.filter(language=f),
        'authors': Author.objects.all(),
        'languages': Language.objects.all(),
        'types': Book_type.objects.all(),
        'number': Book.objects.filter(language=f).count()
    }

    return render(request, "language-filter.html", data)

def type_filter (request,a):
    f = Book_type.objects.get(id=a)
    data = {
        'type_filter':Book.objects.filter(type=f),
        'authors': Author.objects.all(),
        'languages': Language.objects.all(),
        'types': Book_type.objects.all(),
        'number':Book.objects.filter(type=f).count()
    }

    return render(request, "type-filter.html", data)

def search (request):
    if request.method == "POST":
        k = request.POST.get('kitob')
        data = {
            'searched_book': Book.objects.filter(full_name__icontains=k.upper()),
            'authors': Author.objects.all(),
            'languages': Language.objects.all(),
            'types': Book_type.objects.all(),
            'number':Book.objects.filter(full_name__icontains=k.upper()).count()

        }
        # s= Book.objects.filter(full_name__icontains=)
    # print(s)
    return render(request,'search-page.html', data)