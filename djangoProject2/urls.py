from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzeria/', include('pizzeria.urls')),  # Assuming 'pizzeria/' as the URL prefix for your app
]
