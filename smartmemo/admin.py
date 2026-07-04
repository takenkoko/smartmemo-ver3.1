from django.contrib import admin
from .models import Memo, Category
# Register your models here.

admin.site.register(Memo)
admin.site.register(Category)