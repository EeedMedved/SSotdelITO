# Generated by Django 3.1.2 on 2020-11-01 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('new', 'Новая'), ('designate', 'Назначена'), ('inwork', 'В работе'), ('finished', 'Завершена')], default='new', max_length=15)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tickets', to='tickets.category')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tickets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
