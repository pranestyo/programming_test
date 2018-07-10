from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.core.urlresolvers import reverse

from datetime import date


# Create your models here.
@python_2_unicode_compatible
class Book(models.Model):
	TYPE_OF_BOOK_CHOICES = (
		('one_of_novel','One of Novel'),
		('documentation','Documentation'),
		('other','Other'),
		) 

	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	date_published = models.DateField()
	number_of_page = models.IntegerField()
	type_of_book = models.CharField(max_length=20, choices=TYPE_OF_BOOK_CHOICES)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book_edit', kwargs={'pk':self.pk})
