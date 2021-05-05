from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
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

def add_book(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        price = request.POST.get('price',)
        name = request.POST.get('name',)
        book_image = request.FILES['book_image']
        
        book= Book(name=name,desc=desc,price=price,book_image=book_image)
        book.save()
        
    return render(request, 'myapp/add_book.html')
    
def update(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'myapp/edit.html',{'form':form,'book':book})

def delete(request,id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')