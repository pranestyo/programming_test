from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime

from books.forms import BookForm
from books.models import Book

# Create your views here.
def book_list(request, template_name='book_list.html'):
    books = Book.objects.all()
    data = {}
    data['object_list'] = books
    return render(request, template_name, data)

def book_create(request, template_name='book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_update(request, pk, template_name='book_form.html'):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name='book_confirm_delete.html'):
    book = get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('book_list')
    return render(request, template_name, {'object':book})