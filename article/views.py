from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from.models import UserModel, ArticleModel, Comment
from django.core.paginator import Paginator
# Create your views here.

def HomePage(request):
    all_articles = ArticleModel.objects.all()
    return render(request, 'index.html', {'all_articles': all_articles})

def ArticleDetail(request, id):
    # if title is found in the database then we are fetching the article
    article_data = ArticleModel.objects.get(id=id)
    title = article_data.title
    content = article_data.content
    date = article_data.date
    author = article_data.author
    id = article_data.id

    # ------------------------- FOR comment ------------------------
    comment_data = Comment.objects.all()
    # comment_data = Comment.objects.get(post_id=id)
    # print(comment_data.body)
    # c_name = comment_data.name
    # c_email = comment_data.email
    # c_body = comment_data.body
    # c_time = comment_data.created
    data = {
        'title': title,
        'date': date,
        'content': content,
        'author': author,
        'id': id,
        # Comment --------------
        # 'c_name': c_name,
        # 'c_email': c_email,
        # 'c_body': c_body,
        # 'c_time': c_time,
        'comment_data': comment_data
    }
    
    return render(request, 'articledetailpage.html', data)

def SubmitArticle(request):
    if request.method == 'POST':
        # post = id
        # print(post,"---------------------------------------------------------------pist")
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = request.POST.get('date')
        author = request.POST.get('author')
        print(title, content, date)
        if(title !='' and content !='' and date !='' and author !='' ):
            ArticleModel(title=title, content=content, date=date, author=author).save()

    return render(request, 'submitarticle.html')


def SubmitComment(request, id):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        body = request.POST.get('body')
        email = request.POST.get('email')
        print(name, body, email)
        # if(name !='' and email !='' and body !=''):
        Comment(name=name, email=email, body=body, post_id=id).save()

    return HttpResponse("Comment Added")

def EditComment(request, id):
    comment_data = Comment.objects.get(id=id)
    c_name = comment_data.name
    c_email = comment_data.email
    c_body = comment_data.body

    data = {
        'c_name': c_name,
        'c_email': c_email,
        'c_body': c_body,
    }
    
    if request.method == 'POST':
        
        # name = request.POST.get('name')
        body = request.POST.get('body')
        # email = request.POST.get('email')
        # print(name, body, email)
        if(body !=''):
            Comment.objects.filter(id=id).update(body=body)
        # Comment(name=name, email=email, body=body, post_id=id).save()

        return HttpResponse("Comment Updated")
    
    return render(request, 'editcomment.html', data)

def deleteComment(request, id):
    # username = request.GET['username']
    Comment.objects.filter(id=id).delete()
    return HttpResponse("Comment Deleted")
