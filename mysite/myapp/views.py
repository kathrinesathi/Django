from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.


def index(request):
    Book_list = Book.objects.all()
    context = {
        'Book_list':Book_list
    }
    return render(request, 'myapp/index.html', context)
    # return HttpResponse('<h1>Hello world</h1>')

    
# def products(request):
#     return HttpResponse('Book_list')

def detail(request,book_id):
    book= Book.objects.get(id=book_id)
    return render(request, 'myapp/detail.html',{'book':book})
    # return HttpResponse ("This is book no %s" % book_id)