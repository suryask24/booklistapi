from django.contrib import admin
from django.urls import path, include  # include() is used to include the app's URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # This includes the URLs from the app
]
