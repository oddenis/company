
from django.shortcuts import render, redirect

from .models import Branch, Feedback, News
from .forms import Branchform, NewsForm
import datetime
from django.views.generic.detail import DetailView


def main(request):

    return render(request, "main.html")

def about(request):
    
    return render(request, "about.html")

def contacts(request):
    
    return render(request, "contacts.html")

def branches(request):
    branch = Branch.objects.all()
    context = {"branch": branch}
    return render(request, "branches/branches_list.html", context)

def branches_detail(request, branch_id):

    # получили нужный филиал
    branch = Branch.objects.all()

    # передали его в контекст
    context = {"branch": branch}

    # соединили
    return render(request, "branches/detail.html", context)

class BranchDetailView(DetailView):
    model = Branch
    template_name = "branches/detail.html"
    pk_url_kwarg = 'branch_id'

def branch_add(request):
    # context = {}
    # title = request.POST.get('title')
    # txt = request.POST.get('text')
    # print(type(txt))
    # if len(str(txt)) < 10:
    #     return render(request, "branches/branch_add.html", context)
    # else:
    #     b=Branch(title=title, text=txt)
    #     b.save()
    # return redirect('branches')

    branch_form = Branchform()
    if request.method == 'POST':
        branch_form=Branchform(request.POST)
        if branch_form.is_valid():
            title = branch_form.cleaned_data['title']
            text = branch_form.cleaned_data['text']
            b = Branch(title=title, text = text)
            b.save()

    context = {'branch_form':branch_form}
    return render(request, "branches/branch_add.html", context)

def addnews(request):
    # if request.method == 'POST':
    #     topic = request.POST.get('topic')
    #     news_content = request.POST.get('news_content')
    #     author = request.POST.get('author')
    #     news = News(topic=topic, news_content=news_content, author=author)
    #     news.save()
    # getnews=News.objects.all()
    # context = {'news':getnews}
    # return render(request, "addnews.html", context)


    date_today = datetime.datetime.today()

    if request.method == 'POST':
        newsform = NewsForm(request.POST)
        if newsform.is_valid():
            topic_form = newsform.cleaned_data['topic']
            content_form = newsform.cleaned_data['news_content']
            author_form = newsform.cleaned_data['author']
            news = News(topic=topic_form, news_content=content_form, author=author_form)
            news.save()
        getnews=News.objects.all()
        newsform = NewsForm()
        context = {'news':getnews, 'newsform':newsform}
        return render(request, "addnews.html", context)
    newsform = NewsForm()
    getnews = News.objects.filter(date_news=date_today.strftime('%Y-%m-%d'))
    #getnews = News.objects.all()

    context = {'news': getnews, 'newsform':newsform}
    return render(request, "addnews.html", context)



def feedback(request):
    if request.method=='POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        back = Feedback(title=title, text=text)
        back.save()
    back = Feedback.objects.all()
    context = {
            'back':back
               }
    return render(request, "feedback.html", context)