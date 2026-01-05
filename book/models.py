from django.db import models
from accounts.models import Account

class Book(models.Model):
    owner = models.ForeignKey(
    Account,
    on_delete=models.CASCADE,
    related_name="books",
    help_text="Kitobni joylagan foydalanuvchi"
    )
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255, default=None)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
