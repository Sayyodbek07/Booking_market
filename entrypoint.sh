#!/bin/sh

# Migrations
echo "Applying migrations..."
python manage.py migrate

# Superuser yaratish
echo "Creating superuser if not exists..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); \
username = '${DJANGO_SUPERUSER_USERNAME}'; \
email = '${DJANGO_SUPERUSER_EMAIL}'; \
password = '${DJANGO_SUPERUSER_PASSWORD}'; \
User.objects.filter(username=username).exists() or User.objects.create_superuser(username=username, email=email, password=password)"

# Server ishga tushirish
exec "$@"