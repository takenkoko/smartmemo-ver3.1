from django.db import models

# Create your models here.
class Category(models.Model):
       #カテゴリ機能追加
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Memo(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
