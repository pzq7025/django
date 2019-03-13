from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from . import models

"""
    :render(渲染):使用blog下面的html文件, 新建一个和应用名相同的文件夹可以减小冲突
    :字典获取数据除了直接使用键名  还可以使用get方法
"""


def index(request):
    """
    main use interface
    :param request:
    :return: all article objects.
    """
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {"articles": articles})


def article_page(request, article_id):
    """
    the page of article
    :param request:
    :param article_id:
    :return: the correspond of page
    """
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    """
    the edit of page   if the article of id equals zero return the new edit page of url
    else return the correspond of page
    :param request:
    :param article_id:
    :return: the edit of page url
    """
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    """
    response the action if the id equals zero return the index html
    else  Assignment the correspond the param
    :param request:
    :return: action html
    """
    # 这里是提交响应的函数
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        # 提交完之后返回主界面
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {"articles": articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})
