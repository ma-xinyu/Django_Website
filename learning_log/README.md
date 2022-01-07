# Django学习



## 一、项目准备与基础

1. Django是一个Web框架，一套用于帮助开发交互式网站的工具。Django能够响应网页请求，还能让你更轻松地读写数据库、管理用户等。

2. 在实际项目开发中，我们通常会根据自己的需求去下载各种相应的框架库，如Scrapy、Beautiful Soup等，但是可能每个项目使用的框架库并不一样，或使用框架的版本不一样，这样需要我们根据需求不断的更新或卸载相应的库。直接对我们的Python环境操作会让我们的开发甚至是生产环境和项目造成很多不必要的麻烦，管理也相当混乱，所以需要配置虚拟环境，在对应的虚拟环境中安装需求框架。

3. 数据库：需改数据库即迁移数据库，就是对书记库进行增删改查这些操作，首次执行命令migrate 时，将让Django确保数据库与项目的当前状态匹配。在使用SQLite的新项目中首次执行这个命令时，Django将新建一个数据库。

   命令makemigrations 让Django确定该如何修改数据库，使其能够存储与我们定义的新模型相关联的数据。输出表明Django创建了一个名为0001_initial.py的迁移文件，这个文件将在数据库中为模型Topic 创建一个表。

4. runserver：实现远程访问，Django为我们提供的轻量级的开发用的Web服务器，默认情况下，服务器运行在IP地址127.0.0.1的8000端口上

5. 命令startapp *appname* 让Django建立创建应用程序所需的基础设施：其中最重要的文件是models.py、admin.py和views.py。

   1. models.py来定义我们要在应用程序中管理的数据
   2. admin.py来注册我们自己新建的模型（主题和某一篇文章）
   3. views.py来接受请求中的信息，准备好生成网页所需的数据，再将这些数据发送给浏览器

6. settings.py：告诉Django哪些应用程序安装在项目中，在这里将项目加入进去

7. 每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤：修改models.py；对learning_logs 调用makemigrations ；让Django迁移项目



## 二、网站搭建

1. 创建超级用户：用命令创建超级用户createsuperuser ，用户密码加密：存储散列值；似乎用MD5加密也不错？

2. Django自动在管理网站中添加了一些模型，如User 和Group ，但对于我们创建的模型，必须手工进行注册，如注册Topic模型：

   ```python
   from django.contrib import admin
   from learning_logs.models import Topic 
   admin.site.register(Topic)
   #注册Topic模型
   ```

3. Django shell：可通过交互式终端会话以编程方式查看这些数据



## 三、创建网页

1. 使用Django创建网页的过程通常分三个阶段：定义URL、编写视图和编写模板。首先，你必须定义URL模式。URL模式描述了URL是如何设计的，让Django知道如何将浏览器请求 与网站URL匹配，以确定返回哪个网页。

   每个URL都被映射到特定的视图——视图函数获取并处理网页所需的数据。

2. ```python
   from django.conf.urls import include, url 
   from django.contrib import admin 
   urlpatterns = [ 
   	url(r'^admin/', include(admin.site.urls)), 
       #包含learning_logs的URL
       url(r'', include('learning_logs.urls', namespace='learning_logs')),
   ]
   ```

   在这个针对整个项目的urls.py文件中，变量urlpatterns 包含项目中的应用程序的URL。

   后面一行代码包含实参namespace ，让我们能够将learning_logs 的URL同项目中的其他URL区分开来，这 

   在项目开始扩展时很有帮助。

3. ```python
   """定义learning_logs的URL模式""" 
   from django.conf.urls import url 
   from . import views 
   urlpatterns = [ 
       # 主页 
       url(r'^$', views.index, name='index'), 
   ]
   ```

   实际的URL模式是一个对函数url() 的调用，这个函数接受三个实参，第一个是一个正则表达式。Django在urlpatterns 中查找与请求的URL字符串匹配的正则表达式，因此正则表达式定义了Django可查找的模式。

   正则表达式r'^$' 。其中的r 让Python将接下来的字符串视为原始字符串，而引号告诉Python正则表达式始于和终于何处。脱字符（^ ）让Python查看字符串的开头，而美元符号让Python查看字符串的末尾。总体而言，这个正则表达式让Python查找开头和末尾之间没有任何东西的URL，Python忽略项目的基础URL（http://localhost:8000/）。

   name="xxx"，是起的别名。

4. 编写主页：视图函数接受请求中的信息，准备好生成网页所需的数据，再将这些数据发送给浏览器（view.py）

   函数render() ，它根据视图提供的数据渲染响应，演示如何为主页编写视图：

   ```python
   from django.shortcuts import render 
   def index(request): 
   """学习笔记的主页""" 
   	return render(request, 'learning_logs/index.html')
   ```

   URL请求与我们刚才定义的模式匹配时，Django将在文件views.py中查找函数index() ，再将请求对象传递给这个视图函数。在这里，我们不需要处理任何数据，因此这个函数只包含调用render() 的代码。这里向函数render() 提供了两个实参：原始请求对象以及一个可用于创建网页的模板。

   模板编写：html的代码编写，模板间可以继承，因此可以编写通用模板，通用模板需要添加子模板链接

5. 编写其他页面：

   1. 先在urls.py中包含此url映射，表示当需要访问此网页时需要渲染加载views中哪个对应函数(views.topic)
   2. 再编写对应的函数，函数将信息return到创建页面的模板上（xxx.html），比如showall就可以return topics，在前端for循环展示

6. 编写特定页面，比如某一个topic下的所有entry

   1. 显示特定主题的页面的URL模式与前面的所有URL模式都稍有不同，它将使用主题的id 属性来指出请求的是哪个主题。例如，如果用户要查看主题Chess（其id 为1）的详细 页面，URL将为http://localhost:8000/topics/1/。

   ```python
   urlpatterns = [ 
       --snip-- 
       # 特定主题的详细页面 
       url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'), 
   ]
   ```

   r 让Django将这个字符串视为原始字符串，并指出正则表达式包含在引号内;（ /(?P<topic_id>\d+)/  ）与包含在两个斜杠内的整数匹配，并将这个整数存储在一个名为topic_id 的实参中，这部分表达式两边的括号捕获URL中的值；        ?P<topic_id> 将匹配的值存储到topic_id 中；而表达式\d+ 与包含在两个斜杆内的任何数字都匹配，不管这个数字为多少位。

   函数get到一个topic_id，return对应的topic和entry_list，渲染页面用topic.html，网址显示urlpatterns中的网址。

   ```python
   def topic(request, topic_id):
       #显示单个主题及其所有的条目
       topic = Topic.objects.get(id=topic_id)
       #确认用户是否允许
       if topic.owner != request.user:
           raise Http404
       entries = topic.entry_set.order_by('-date_added')
       context = {'topic': topic, 'entries': entries}
       return render(request, 'learning_logs/topic.html', context)
   ```

   

7. 要修改模板topics.html，让每个主题都链接到相应的网页

   ```html
   --snip-- 
   {% for topic in topics %} 
   <li>
       <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a> 
   </li> 
   {% empty %} 
   --snip--
   ```

   我们使用模板标签url 根据learning_logs中名为topic 的URL模式(name="xxx")来生成合适的链接。这个URL模式要求提供实参topic_id(正则表达式) ，因此我们在模板标签url 中添加了属性topic.id 。

   现在，主题列表中的每个主题都是一个链接，链接到显示相应主题的页面，如http://localhost:8000/topics/1/。

8. 总结：(important)
   1. html展示对应的信息，绑定链接到对应的URL模式上，其后可追加提供的信息
   2. 通过name="xxx"在urls.py的urlpatterns中匹配对应的映射，将get到的信息传给调用的函数
   3. 函数return需要的数据给对应的页面渲染，网址转到对应的urlpatterns中的网址



## 五、增删改查

1. 新增主题：首先新建froms.py，建立新建的对象的表单

   ```python
   from django import forms 
   from .models import Topic
   class TopicForm(forms.ModelForm): 
       class Meta: 
           model = Topic 
           fields = ['text'] 
           labels = {'text': ''}
   ```

   最简单的ModelForm 版本只包含一个内嵌的Meta 类，它告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段，我们根据模型Topic 创建一个表单，第二行表示该表单只包含字段text ，最后一行代码让Django不要为字段text 生成标签。

2. url:

   当用户要添加新主题时，我们将切换到http://localhost:8000/new_topic/

   ```python
   --snip-- 
   urlpatterns = [ 
   	--snip-- 
   	# 用于添加新主题的网页
   	url(r'^new_topic/$', views.new_topic, name='new_topic'),
   ]
   ```

   这个URL模式将请求交给视图函数new_topic() ，接下来我们将编写这个函数。

3. view：

   函数new_topic() 需要处理两种情形：

   ​	刚进入new_topic 网页（在这种情况下，它应显示一个空表单）；

   ​	对提交的表单数据进行处理，并将用户重定向到网页topics ；

   ```python
   from django.shortcuts import render 
   from django.http import HttpResponseRedirect 
   from django.core.urlresolvers import reverse 
   from .models import Topic 
   from .forms import TopicForm 
   --snip-- 
   def new_topic(request): 
       """添加新主题""" 
       if request.method != 'POST': 
           # 未提交数据：创建一个新表单  
           form = TopicForm() # 新建一个表单
       else:
           # POST提交的数据,对数据进行处理 
           form = TopicForm(request.POST) 
           if form.is_valid(): 
               form.save() 
               return HttpResponseRedirect(reverse('learning_logs:topics')) 
       context = {'form': form}
       return render(request, 'learning_logs/new_topic.html', context)
   ```

   导入了HttpResponseRedirect 类，用户提交主题后将使用这个类将用户重定向到网页topics，函数reverse() 根据指定的URL模型确定URL，这意味着Django将在页面被请求时生成URL，同时我们还导入了刚才创建的表单TopicForm 。

4. GET和POST请求

   ​	  创建Web应用程序时，将用到的两种主要请求类型是GET请求和POST请求。对于只是从服务器读取数据的页面，使用GET请求；在用户需要通过表单提交信息时，通常使用POST请求。处理所有表单时，我们都将指定使用POST方法。函数new_topic() 将请求对象作为参数。用户初次请求该网页时，其浏览器将发送GET请求；用户填写并提交表单时，其浏览器将发送POST请求。根据请求的类型，我们可以确定用户请求的是空表单（GET请求）还是要求对填写好的表单进行处理（POST请求）。

   ​	  测试确定请求方法是GET还是POST。如果请求方法不是POST，请求就可能是GET，因此我们需要返回一个空表单（即便请求是其他类型的，返回一个空表单也不会有任何问题）。我们创建一个TopicForm 实例，将其存储在变量form 中，再通过上下文字典将这个表单发送给模板。由于实例化TopicForm 时我们没有指定任何实参，Django将创建一个可供用户填写的空表单。 

   ​		要将提交的信息保存到数据库，必须先通过检查确定它们是有效的（见❹）。函数is_valid() 核实用户填写了所有必不可少的字段（表单字段默认都是必不可少的），且输入的数据与要求的字段类型一致（例如，字段text 少于200个字符，这是我们在第18章中的models.py中指定的）。这种自动验证避免了我们去做大量的工作。如果所有字段都有效，我们就可调用save() ，将表单中的数据写入数据库。保存数据后，就可离开这个页面了。我们使用reverse() 获取页面topics 的URL，并将其传递给HttpResponseRedirect() ，后者将用户的浏览器重定向到页面topics 。在页面topics 中，用户将在主题列表中看到他刚输入的主题。 

5. html:

   ```html
   <form action="{% url 'learning_logs:new_topic' %}" method='post'> 
       {% csrf_token %} 
       {{ form.as_p }} 
       <button name="submit">add topic</button> 
   </form>
   ```

   按下button，就会发送POST请求

6. 其他同上

7. 编辑：

   ​	我们首先需要导入模型Entry ，我们获取用户要修改的条目对象，以及与该条目相关联的主题。在请求方法为GET时将执行的if 代码块中，我们使用实参instance=entry 创建一个EntryForm 实例，这个实参让Django创建一个表单，并使用既有条目对象中的信息填充它。用户将看到既有的数据，并能够编辑它们。处理POST请求时，我们传递实参instance=entry 和data=request.POST ，让Django根据既有条目对象创建一个表单实例，并根据request.POST 中的相关数据对其进行修改。然后，我们检查表单是否有效，如果有效，就调用save() ，且不指定任何实参。接下来，我们重定向到显示条目所属主题的页面，用户将在其中看到其编辑的条目的新版本。

8. 删除：

   ​	delete();

   

## 六、用户查看自己的数据

1. 装饰器@login_required，实现数据库的功能罢了，当前用户在登录了才能看到数据，调用方法，如果用户未登录，就重定向到登录页面，为实现这种重定向，我们需要修改settings.py，让Django知道到哪里去查找登录页面。

2. 在Topic 中添加了字段owner ，建立到模型User 的外键关系，用过滤器filter(owner=request.user)。

   

## 七、前端设计--django-bootstrap3

1. 安装并在setting.py中添加bootstrap3

2. 我们需要让django-bootstrap3包含jQuery，这是一个JavaScript库，让你能够使用Bootstrap模板提供的一些交互式元素，在settings.py的末尾添加如下代码：

   ```python
   # django-bootstrap3的设置 
   BOOTSTRAP3 = { 
   	'include_jquery': True, 
   	}
   ```

   这些代码让你无需手工下载jQuery并将其放到正确的地方。 

   

## 八、部署到Heroku服务器中

1. 安装必要包

2. 创建requirements.txt，Heroku需要知道我们的项目依赖于哪些包，因此我们将使用pip来生成一个文件，其中列出了这些包

3. 创建runtime.txt，确保Heroku使用我们使用的Python版本

4. 修改settings.py

   ```python
   #'bootstrap3'的设置
   BOOTSTRAP3 = {
       'include_jquery':True,
       }
   
   # Heroku设置
   if os.getcwd() == '/app':
       import dj_database_url 
       DATABASES = { 
           'default': dj_database_url.config(default='postgres://localhost') 
           }
   
   # 让request.is_secure()承认X-Forwarded-Proto头
   SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') 
   
   # 支持所有的主机头（host header
   ALLOWED_HOSTS = ['*'] 
       
   # 静态资产配置
   BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
   STATIC_ROOT = 'staticfiles'
   STATICFILES_DIRS = ( 
       os.path.join(BASE_DIR, 'static'), 
       )
   ```

   ​	我们使用了函数getcwd() ，它获取当前的工作目录 （当前运行的文件所在的目录），在Heroku部署中，这个目录总是/app。在本地部署中，这个目录通常是项目文件夹的名称（就我们的项目而言，为learning_log），这个if 测试确保仅当项目被部署到Heroku时，才运行这个代码块。这种结构让我们能够将同一个设置文件用于本地开发环境和在线服务器。我们导入了dj_database_url ，用于在Heroku上配置服务器，Heroku使用PostgreSQL（也叫Postgres）——一种比SQLite更高级的数据库；这些设置对项目进行配置，使其在Heroku上使用Postgres数据库。

5. 创建启动进程的Procfile，告诉Heroku启动哪些进程，以便能够正确地提供项目提供的服务，这个文件只包含一行，你应将其命名为Procfile（其中的P为大写），不指定文件扩展名，并保存到manage.py所在的目录中。 

6. 修改wsgi.py，我们导入了帮助正确地提供静态文件的Cling，并使用它来启动应用程序，这些代码在本地也适用，因此无需将其放在if 代码块内。

7. 使用Git跟踪文件，推送到Heroku，建立数据库，给网站更名

