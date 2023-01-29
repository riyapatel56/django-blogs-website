from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=4)

class ArticleModel(models.Model):
    author = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, unique=True)
    content = models.CharField(max_length=200)
    date= models.DateField()

    # def __str__(self):
    #     return self.title

class Comment(models.Model): 
    post = models.ForeignKey(ArticleModel,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    # created = models.DateTimeField(auto_now_add=True) 
    # updated = models.DateTimeField(auto_now=True) 
    # active = models.BooleanField(default=True) 

    # class Meta: 
    #     ordering = ('created',) 

    # def __str__(self): 
    #     return 'Comment by {}'.format(self.name,) 
