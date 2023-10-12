# pages/urls.py
from django.urls import path

# point views to look in the current directory:
from .views import home_page_view

# if the user requests the homepage represented by the empty string "", 
# Django should use the view called home_page_view
# ADD IT TO PROJECT/URLS.PY
urlpatterns = [
    path("", home_page_view, name="home"),
]