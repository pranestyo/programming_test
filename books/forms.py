from django.forms import ModelForm
from django import forms
from datetime import date
from django.forms import widgets
from django.core.exceptions import ValidationError

from books.models import Book

class DateInput(forms.DateInput):
	input_type = 'date'

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['title','author','date_published','number_of_page','type_of_book']
		labels = {
			'title':"Title",
			'author':"Author",
			'date_published':"Date Published",
			'number_of_page':"Number of Page",
			'type_of_book':"Type of Book",
		}
		error_messages = {
			'title':{
				'required':"Title can not be empty"
			},
			'author':{
				'required':"Author can not be empty"
			}
		}
		widgets = {
			'date_published': DateInput()
		}
