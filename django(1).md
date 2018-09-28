﻿# Djiango笔记

#### 1. anacoda下安装Django

直接搜索Django即可，在pycharm选择解释器时注意一定要选择anacoda的环境源。

这里我所用的开发环境为：Django 2.1 ，python 3.6 

#### 2. 创建

>2.1 新建一个工程

在工作文件夹里面打开PowerShell,输入：`django-admin startproject PROJECTNAME`

此时Django其实就可以工作了，切换到内层含 `manage.py` 的文件夹输入:  `python manage.py runserver 80`

在游览器打开 `127.0.0.1` ,如果看到 hello python的页面，这证明之前创建的Django已经正确的运行了。这是Django内置的一个应用，在项目创始时已由python自动生成。

> 2.2 创建自己的应用

一个项目下可以创建许多应用，在manage.py同级文件夹下运行：`python manage.py startapp APPNAME`

即可创建一个应用。

#### 3. 开始第一个页面

> 3.1 改变语言和时区 

之前我们在打开Django自动生产的页面时，发现其为英文的，我们可以更改项目的设置文件`setting.py`对项目语言和时区进行更改。把 `LANGUAGE_CODE` 的值改为 `zh-hans`，`TIME_ZONE` 的值改为 `Asia/Shanghai`

> 3.2 注册应用

其实之前我们所创建的app是没有注册到项目工程中的，故打开`setting.py`,找到`INSTALLED_APPS`列表，加入`APPNAME`
可以看到原列表中已有很多内置应用了，这些应用提供了各种各样的功能。当然如果不需要可以注释掉。

> 3.3 创建数据库模型

Django默认的数据库为sqlite3，如要连接其他的数据库添加相应的驱动即可。同时Django提供了一套 ORM（Object Relational Mapping）系统,可以把python语言自动转化为数据库语言。

在 APPNAME/model.py 文件下，写入：

        from django.db import models

        class Category(models.Model):
            name = models.CharField(max_length=100)

其中`Category`是python的一个标准类，继承`models.Model`. `name` 是其中的一个属性，它是`models。CharFileld`的一个实例。

数据库模型中有三种关系，一对一，多对一，多对多，这些关系都在django的官方文档里面有讲到。

> 3.4 迁移数据库

即将python代码转化为数据库语言，在数据库里创建数据表

在manage.py文件同目录下打开PowerShell，

① 运行：`python manage.py makemigration`

这会在该应用目录下生成 `0001_initial.py`文件，记录对模型做出的修改情况。

② 运行`python manage.py migrate`

将之前生产的文件翻译为数据库语言并写入数据库。

额外的，可输入`python manage.py sqlmigrate APPNAME 0001` 查看具体的数据库语言写入句子。

> 3.5 项目首页视图

有三个值得思考的问题：
1. Django如何接受http请求
2. Django如何处理这个请求
3. Gjango如何相应这个请求

首先Django需要知道用户访问不同网址时该如何处理这些网址。把不同网址对应的处理函数写在一个`urls.py`文件里，当用户访问某个网址时，就会在该文件中寻找，如果找到就会调用和它绑定在一起的处理函数(视图函数)

在应用的文件夹下面创建一个`urls.py`的文件，写入：

        # APPNAME/urls.py
        from django.contrib import admin # 导入管理员页面
        from django.urls import path 
        from django.conf.urls import url,include

        urlpatterns = [
            path(r'admin/', admin.site.urls),
            path(r'',include('blog.urls')),
        ]




*   编辑app下的 `models.py` 文件，改变模型。
*  在项目setting里添加app
*   运行 [`python manage.py makemigrations`](https://docs.djangoproject.com/zh-hans/2.1/ref/django-admin/#django-admin-makemigrations) +appname为模型的改变生成迁移文件。
*   运行 [`python manage.py makemigrations`](https://docs.djangoproject.com/zh-hans/2.1/ref/django-admin/#django-admin-makemigrations) +appname为模型的改变生成迁移文件。
*   运行 [`python manage.py makemigrations`](https://docs.djangoproject.com/zh-hans/2.1/ref/django-admin/#django-admin-makemigrations) +appname为模型的改变生成迁移文件。
*   运行 [`python manage.py migrate`](https://docs.djangoproject.com/zh-hans/2.1/ref/django-admin/#django-admin-migrate) +appname 来应用数据库迁移。


#创建一个管理员账号

    python manage.py createsuperuser

键入你想要使用的用户名，然后按下回车键：

    Username: admin



然后提示你输入想要使用的邮件地址：

    Email address: admin@example.com

### 向管理页面中加入投票应用

打开 polls/admin.py 文件

    from django.contrib import admin

    from .models import Question

    admin.site.register(Question)



















## 涉及到的 `大块代码`

    blog/models.py

    from django.db import models
    from django.contrib.auth.models import User


    class Category(models.Model):
        """
        Django 要求模型必须继承 models.Model 类。
        Category 只需要一个简单的分类名 name 就可以了。
        CharField 指定了分类名 name 的数据类型，CharField 是字符型，
        CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
        当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
        Django 内置的全部类型可查看文档：
        https://docs.djangoproject.com/en/2.10/ref/models/fields/#field-types
        """
        name = models.CharField(max_length=100)


    class Tag(models.Model):
        """
        标签 Tag 也比较简单，和 Category 一样。
        再次强调一定要继承 models.Model 类！
        """
        name = models.CharField(max_length=100)


    class Post(models.Model):
        """
        文章的数据库表稍微复杂一点，主要是涉及的字段更多。
        """

        # 文章标题
        title = models.CharField(max_length=70)

        # 文章正文，我们使用了 TextField。
        # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
        body = models.TextField()

        # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
        created_time = models.DateTimeField()
        modified_time = models.DateTimeField()

        # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
        # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
        excerpt = models.CharField(max_length=200, blank=True)

        # 这是分类与标签，分类与标签的模型我们已经定义在上面。
        # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
        # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
        # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
        # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
        # 如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
        # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
        category = models.ForeignKey(Category)
        tags = models.ManyToManyField(Tag, blank=True)

        # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
        # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
        # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
        # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
        author = models.ForeignKey(User)