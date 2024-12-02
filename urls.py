from django.urls import path
from .views import home_view, about_view, HomePageView, AboutPageView, BookListView, BookDetailView, CustomRedirectView, CustomPageView

urlpatterns = [
    # Function-based views (FBVs)
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    
    # Class-based views (CBVs)
    path('home-cbv/', HomePageView.as_view(), name='home-cbv'),
    path('about-cbv/', AboutPageView.as_view(), name='about-cbv'),
    
    # Generic Class-based views (GCBVs)
    path('book-list/', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # Redirect view
    path('redirect/', CustomRedirectView.as_view(), name='redirect'),
    
    # Mixed FBV and CBV example
    path('custom-page/', CustomPageView.as_view(), name='custom-page'),
]
