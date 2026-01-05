from rest_framework import serializers
from book.models import Book

class BookSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(required=False) # Fayl yuklash imkonini beradi
    class Meta:
        model = Book
        fields = "__all__"