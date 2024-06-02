from django.forms import ModelForm, TextInput, DateInput
from django.db import models

from django import forms

from .models import Author, Quote, Tag

class AuthorForm(ModelForm):
    fullname = models.CharField(max_length=50)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class TagForm(ModelForm):
    name = models.CharField(max_length=50)

    class Meta:
        model = Tag
        fields = ['name']

class QuoteForm(ModelForm):
    quote = models.TextField()
    tags = forms.MultipleChoiceField(choices=Tag.objects.values_list())
    author = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']