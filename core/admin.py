from django.contrib import admin

from .models import Branch, Feedback, News, Categoria

admin.site.register(Branch)
admin.site.register(Feedback)



class ListAdminNews(admin.ModelAdmin):
    list_display = ('id','topic', 'news_content', 'author', 'categoria', 'date_news')

admin.site.register(News, ListAdminNews)
admin.site.register(Categoria)