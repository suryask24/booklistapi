# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book
from django.views.generic import RedirectView
from django.views.generic import TemplateView

# FBV: Home page
def home_view(request):
    return HttpResponse("Welcome to the Home page!")

# FBV: About page rendering a template
def about_view(request):
    return render(request, 'about.html')

# FBV: List of books
def book_list_view(request):
    return render(request, 'book_list.html')

# CBV: Home page using a class-based view
class HomePageView(View):
    def get(self, request):
        return HttpResponse("This is the Home Page (Class-based View).")

# CBV: About page rendering a template
class AboutPageView(View):
    def get(self, request):
        return render(request, 'about.html')

# GCBV: List of books using ListView
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

# GCBV: Book details
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        book_id = self.kwargs.get('pk')
        if book_id == '1':
            return Book(title='Sample Book', author='Sample Author', description='This is a sample book description.')
        return None

# Redirect view to an external URL
class CustomRedirectView(RedirectView):
    url = 'https://www.example.com'

# FBV: Custom function to get data
def get_custom_data():
    return {"message": "Hello from FBV"}

# CBV: Custom page that uses FBV data
class CustomPageView(TemplateView):
    template_name = 'custom_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_data'] = get_custom_data()
        return context
