from django.urls import path
from .views import (
    CommentCreateView,
    CommentListView,
    CommentDetailView,
    CommentDeleteView,
)

urlpatterns = [
    path("comments/add/", CommentCreateView.as_view(), name="comment-add"),
    path("comments/list/", CommentListView.as_view(), name="comment-list"),
    path("<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    path("<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
