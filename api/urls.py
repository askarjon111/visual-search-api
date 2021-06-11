from django.urls import path
from api import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('items/', views.ItemList.as_view()),
    path('items/<int:pk>/', views.ItemDetail.as_view()),
]

