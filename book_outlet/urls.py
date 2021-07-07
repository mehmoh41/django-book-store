from django.urls import path
from . import views # from the current import views file
urlpatterns = [
    path("" , views.index),
    path("<slug:slug>" , views.book_detail , name="book-detail")
]
