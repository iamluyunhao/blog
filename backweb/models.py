from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    login_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class Category(models.Model):
    # 类型
    name = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'category'


class Article(models.Model):
    # 标题
    title = models.CharField(max_length=30, null=False)
    # 分类
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    # 内容描述
    desc = models.CharField(max_length=100, null=True)
    # 文章内容
    content = models.TextField()
    # 标题图片
    icon = models.ImageField(upload_to='article', null=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'

