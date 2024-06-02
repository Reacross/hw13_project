import logging
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.
from .utils import get_mongodb

from .forms import AuthorForm, QuoteForm
from .models import Quote, Author

logging.basicConfig(filename="logfilename.log", level=logging.INFO)

def main(request, page=1):
    # db = get_mongodb() для початкової роботи з БД монго. Закоментовано після міграції на SQLite
    quotes = Quote.objects.select_related('author').prefetch_related('tags').all()#db.quotes.find()  для початкової роботи з БД монго. Закоментовано після міграції на SQLite
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_info(request, id):
    author = Author.objects.get(pk=id)
    return render(request, 'quotes/author_info.html', context={'author':author})

@login_required
def add_author(request):
    form = AuthorForm
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:root')
    return render(request, 'quotes/upload_author.html', context={'form': form})

@login_required
def add_quote(request):
    form = QuoteForm()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:root')
    return render(request, 'quotes/upload_quote.html', context={'form': form})
