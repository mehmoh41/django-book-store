from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg
# Create your views here.
def index(request) : 
    books = Book.objects.all().order_by("-rating") # title orders in DESC -title orders in ASC
    num_books = books.count();
    avg_rating = books.aggregate(Avg("rating"))
    return render(request , 'book_outlet/index.html' , {
        "books":  books,
        "books_count" : num_books,
        "avg_rating" : avg_rating
    })

def book_detail(request , slug) : 
    book = get_object_or_404(Book , slug = slug)
    return render(request , "book_outlet/book_detail.html" , {
        "title": book.title,
        "author": book.author,
        "rating" : book.rating,
        "is_best_selling_book" : book.is_best_selling_book,
    })
    

