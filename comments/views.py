from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Comment
from .serializers import CommentSerializers
from .permissions import IsOwner

class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [AllowAny]

class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticated]

class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticated, IsOwner]