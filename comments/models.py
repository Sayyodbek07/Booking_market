from django.db import models
from book.models import Book
from accounts.models import Account

class Comment(models.Model):
    book = models.ForeignKey(
    Book,
    on_delete=models.CASCADE,
    related_name="comments"
    )

    user = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        related_name="book_comments"
    )
    
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.book}"