from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import BookSerializers
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Book

class BookLIstView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [AllowAny]

class BoookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    parser_classes = (MultiPartParser, FormParser) # SHU QATOR MUHIM
    permission_classes = [IsAuthenticated]

class BookPutAndPatch(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsAdminUser]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsAdminUser]