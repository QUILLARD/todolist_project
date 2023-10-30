from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class TodoList(models.Model):
    todo_title = models.CharField(max_length=150)
    todo_content = models.TextField(blank=True)
    todo_created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    todo_due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    todo_category = models.ForeignKey(Category, on_delete=models.PROTECT,  default="general")

    def __str__(self):
        return self.todo_title

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ['todo_created']
