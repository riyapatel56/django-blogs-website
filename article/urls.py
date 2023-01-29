from django.urls import path
from article import views

urlpatterns = [

    path("", views.HomePage),
    path("submitarticle", views.SubmitArticle),
    path("articledetail/<str:title>", views.ArticleDetail),
    path("submitcomment", views.SubmitComment)

]