from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # /blog/
    path("<int:bulan>", views.challenge_bulanan_by_number),
    path("<str:bulan>", views.challenge_bulanan, name="tantangan-bulanan")
]
