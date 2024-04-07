# Generated by Django 3.2.25 on 2024-04-07 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_news_date_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_categoria', models.CharField(default='Общество', max_length=30, verbose_name='Категория')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoria', verbose_name='Рубрика'),
        ),
    ]
