from django.contrib import admin
from .models import Post
''' c models.py импортирую класс Post'''

admin.site.register(Post)
""" Регистрирую свою модель """