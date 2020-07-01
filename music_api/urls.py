from django.urls import path
from .views import MelodyView
app_name = ""
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('melodys/', MelodyView.as_view(), name="melodys"),
]