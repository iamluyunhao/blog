from django.core.paginator import Paginator
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from backweb.form import AddArtForm, UpdateArtForm
from backweb.models import User, Article, Category


def index(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        article = Article.objects.all()
        art_num = len(article)
        return render(request, 'backweb/index.html', {'art_num': art_num, 'user': user})


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')

    user = User.objects.filter(username=username, password=password).first()
    if not user:
        return render(request, 'backweb/login.html')

    request.session['user_id'] = user.id
    return HttpResponseRedirect(reverse('backweb:index'))


def logout(request):
    if request.method == 'GET':
        request.session.flush()
        return HttpResponseRedirect(reverse('backweb:login'))


def art(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        page_num = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        paginator = Paginator(articles, 10)
        page = paginator.page(page_num)
        category = Category.objects.all()
        return render(request, 'backweb/article.html', {'page': page, 'category': category, 'user': user})


def add_art(request):
    if request.method == 'GET':
        return render(request, 'backweb/add-article.html')
    elif request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            category_id = int(form.cleaned_data['category'])
            desc = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            Article.objects.create(title=title, category_id=category_id,
                                   desc=desc, content=content, icon=icon)
            return HttpResponseRedirect(reverse('backweb:art'))
        else:
            return render(request, 'backweb/add-article.html', {'form': form, 'user': user})


def up_art(request, id):
    if request.method == 'GET':
        article = Article.objects.get(pk=id)
        return render(request, 'backweb/add-article.html', {'article': article})
    elif request.method == 'POST':
        form = UpdateArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            category_id = int(form.cleaned_data['category'])
            desc = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            article = Article.objects.get(pk=id)
            article.title = title
            article.category_id = category_id
            article.desc = desc
            article.content = content
            article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('backweb:art'))
        else:
            article = Article.objects.get(pk=id)
            return render(request, 'backweb/add-article.html', {'article': article})


def del_art(request, id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:art'))


def notice(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        return render(request, 'backweb/notice.html', {'user': user})


def comment(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        return render(request, 'backweb/comment.html', {'user': user})


def category(request):
        if request.method == 'GET':
            user_id = request.session.get('user_id')
            user = User.objects.get(pk=user_id)
            return render(request, 'backweb/category.html', {'user': user})


def flink(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        return render(request, 'backweb/flink.html', {'user': user})


def loginlog(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        return render(request, 'backweb/loginlog.html', {'user': user})


def manage_user(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        return render(request, 'backweb/manage-user.html', {'user': user})


def setting(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        return render(request, 'backweb/setting.html', {'user': user})


def readset(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        return render(request, 'backweb/readset.html', {'user': user})



