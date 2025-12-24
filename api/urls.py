from api.spectacular.urls import urlpatterns as doc_urls
from comments.urls import urlpatterns as comment
from book.urls import urlpatterns as books
from accounts.urls import urlpatterns as accounts

app_name = 'api'
urlpatterns = []

urlpatterns += comment
urlpatterns += books
urlpatterns += accounts
urlpatterns += doc_urls