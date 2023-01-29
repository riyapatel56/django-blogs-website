from django.shortcuts import get_object_or_404, render
from.models import UserModel, ArticleModel, Comment
from django.core.paginator import Paginator
# Create your views here.

def HomePage(request):
    all_articles = ArticleModel.objects.all()
    return render(request, 'index.html', {'all_articles': all_articles})

def ArticleDetail(request, title):
    # if title is found in the database then we are fetching the article
    article_data = ArticleModel.objects.get(title=title)
    title = article_data.title
    content = article_data.content
    date = article_data.date
    author = article_data.author
    id = article_data.id
    data = {
        'title': title,
        'date': date,
        'content': content,
        'author': author,
        'id': id,
    }
    return render(request, 'articledetailpage.html', data)

def SubmitArticle(request):
    if request.method == 'POST':
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = request.POST.get('date')
        author = request.POST.get('author')
        print(title, content, date)
        if(title !='' and content !='' and date !='' and author !='' ):
            ArticleModel(title=title, content=content, date=date, author=author).save()

    return render(request, 'submitarticle.html')


def SubmitComment(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        body = request.POST.get('body')
        email = request.POST.get('email')
        print(name, body, email)
        # if(name !='' and email !='' and body !=''):
        Comment(name=name, email=email, body=body,).save()

    # return render(request, 'submitarticle.html')