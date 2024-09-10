from django.urls import path

from .views import *

urlpatterns = [
    path('',book),
    path('author_filter/<int:a>/', author_filter),
    path('language_filter/<int:a>/', language_filter),
    path('type_filter/<int:a>/', type_filter),
    path('search/',search)
]