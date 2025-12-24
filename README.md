# Booking_market

## Turli xil kitoblarni online sotish uchun
### 1. Foydalanuvchilarga kitoblar ro'yxatini ko'rsatish
### 2. Admin kitob joylay olish, o'zgartira olish o'chira olish

### Ozod - book app ni ichida models yaratish. Hamma kitoblar ro'yxatini ko'rolsin. Faqat o'zgaritirolsin.
### Sayodbek - comments ichida models bo'ladi shu modelsni foreign key orqali book data base ga bog'lash.
### faqat ro'yxatdan o'tganlar izoh yozolsin

### kutubxonalar:
### 1. django
### 2. django-rest-framework
### 3. posgresql

---------------------------------

### pip install -r requirements.txt

### python manage.py runserver

---

### Data base

### book
    class Book(models.Model):
    owner = models.ForeignKey(
        accounts,
        on_delete=models.CASCADE,
        related_name="books",
        help_text="Kitobni joylagan foydalanuvchi"
    )
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

### comment
    class Comment(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        accounts,
        on_delete=models.SET_NULL,
        null=True,
        related_name="book_comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.book}"
