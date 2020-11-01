from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ('title',)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('designate', 'Назначена'),
        ('inwork', 'В работе'),
        ('finished', 'Завершена')
    )

    author = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='tickets')
    responsible = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tickets')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
