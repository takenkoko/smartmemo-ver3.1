from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
       #カテゴリ機能追加
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#ユーザーごとのメモ管理機能追加
class Memo(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,#ユーザーを削除したら、そのメモも削除
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=100)
    content = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,  
    )

    def __str__(self):
        return self.title