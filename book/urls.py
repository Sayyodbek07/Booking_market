from django.urls import path
from book.views import *
urlpatterns = [
    path('book/list/',BookLIstView.as_view(),name = "list"),
    path('book/create/',BoookCreateView.as_view(),name = "create"),
    path('book/update/<int:pk>/',BookPutAndPatch.as_view(),name = "update"),
    path('book/delete/<int:pk>/',BookDeleteView.as_view(),name = "delete"),
]