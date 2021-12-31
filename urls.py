from django.urls import path

from .views import home, register, addPassword, getPasswords, filter

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('addPassword/', addPassword, name="addPassword"),
    path('passwords/<int:id>/', getPasswords, name="passwords"),
    path('passwords/<int:id>/filter/', filter, name="filter")
]
