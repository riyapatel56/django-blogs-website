from django.urls import path
from article import views

urlpatterns = [

    path("", views.HomePage),
    path("submitarticle", views.SubmitArticle),
    path("articledetail/<int:id>", views.ArticleDetail),
    path("submitcomment/<int:id>", views.SubmitComment)

]