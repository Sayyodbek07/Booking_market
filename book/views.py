from rest_framework import generics
from .serializers import BookSerializers
from .models import Book
from rest_framework.permissions import AllowAny, IsAdminUser

class BookLIstView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [AllowAny]

class BoookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    authentication_classes = [IsAdminUser]

class BookPutAndPatch(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    authentication_classes = [IsAdminUser]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    authentication_classes = [IsAdminUser]
