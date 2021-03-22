from django.shortcuts import render
from django.http import HttpResponse
# from .models import Book
# Create your views here.


def index(request):
    # Book_list = Book.objects.all()
    # return render(request, 'home/index.html')
    return HttpResponse('<h1>Hello world</h1>')

    
def products(request):
    return HttpResponse('products')