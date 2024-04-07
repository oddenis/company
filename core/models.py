from django.db import models

class Branch(models.Model):
    title = models.CharField(max_length=254, verbose_name='заголовок')
    text = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

class Feedback(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок', default='Супер')
    text = models.CharField(max_length=500, verbose_name='описание', default='Класс')
    def __str__(self):
        return self.title

class Categoria(models.Model):
    news_categoria = models.CharField(max_length=30, verbose_name='Категория', default='Общество')

    def __str__(self):
        return self.news_categoria

class News(models.Model):

    topic=models.CharField(max_length=250, verbose_name='Заголовок')
    news_content = models.TextField(verbose_name='Новость')
    author = models.CharField(max_length=50, verbose_name='Автор')
    date_news = models.DateField('дата создания новости', auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Рубрика', null=True)

    def __str__(self):
        return self.topic
