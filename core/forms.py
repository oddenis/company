from django import forms
from .models import Branch, News
from django.core.exceptions import ValidationError

class Branchform(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок')
    text = forms.CharField(max_length=500, required=True)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Branch.objects.filter(title=title).exists():
            raise ValidationError('Заголовок уже есть')
        return title

class NewsForm(forms.ModelForm):
    # topic = forms.CharField(label='Заголовок', required=True)
    # news_content = forms.CharField(label='Новость', required=True)
    # author = forms.CharField(label='Автор')
    # categoria = forms.CharField(label='Категория', max_length=30)
    class Meta:
        model = News
        fields = ['topic', 'news_content', 'author', 'categoria']