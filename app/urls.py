from django.urls import path
from .views import createText

urlpatterns = [
    path('', createText, name='create_textmodel'),
    # Add other URLs as needed
]
