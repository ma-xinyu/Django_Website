# Django入门

#### 介绍
python项目开发

#### 软件架构
Web框架


#### 安装教程

1.  在项目目录下创建虚拟环境: python -m venv ll_env(是字母ll不是数字11)
2.  进入虚拟环境: ll_env\Scripts\activate
3.  安装Django: pip install Django

#### 使用说明

1.  cd到本项目路径下（本项目 cd 到 learning_log 目录即可）
2.  进入虚拟环境: ll_env\Scripts\activate
3.  对项目下的子目录进行迁移: python manage.py makemigrations learning_logs
4.  应用迁移: python manage.migrate (迁移数据库)
5.  启动服务器: python manage.py runserver
6.  登录网站 localhost:8000/ 即可使用

### 开发记录

## 2021.8.6
1. gitee创建项目，文件创建，环境搭建
2. 创建应用程序: python manage.py startapp users
3. 将应用程序加载到settings中
4. 激活模型
5. Django shell查看数据

## 2021.8.7
1. URL映射: 单词不要打错
2. 编写模板 .html 文件
3. 模板继承
4. 流程: 在urls下加入映射（添加网站）; 在view下添加视图 ; 添加对应模板 .html文件
5. 完成index, topic, topics的模板编写

## 2021.8.8
1. 完成entry, new_topic, new_entry的模板编写
2. 完成编辑条目页面的编写: edit_entry
3. 新建user应用程序
4. 加入Login和Logout功能
5. 加入注册用户功能
6. 分用户管理个人数据: @login_required 限制访问，迁移数据库

## 2021.8.8
1. 美化界面
2. 安装: pip install django-bootstrap3
3. 在设置中更改

## 2021.8.8
1. 部署到服务器Heroku Toolbelt
2. email: @icloud.com   password:letter ma、number、symbol #
3. pip install dj-database-url 
4. pip install dj-static 
5. pip install static3 
6. pip install gunicorn
7. pip freeze > requirements.txt 让pip将项目中当前安装的所有包的名称都写入到文件requirements.txt中
8. 需要settings
9. 创建Procfile
10. 修改wsgi.py

## 2021.8.9
1. 部署
2. setting 中设置顶格
3. Procfile 留个空格
4. 迁移数据库
5. 创建超级用户
6. 改URL: heroku apps:rename mxy-log

## 2021.8.10
1. 确保项目安全
2. 创建自定义报错面板

## 日常维护
1. git commit -am " "
2. git push heroku master
3. heroku ps
4. heroku open

### 知识点
1. <a href="{% url 'learning_logs:edit_entry' entry.id %}">edit entry</a> 加入链接
2. <a type="button" class="btn btn-primary" 
   href="{% url 'learning_logs:edit_entry' entry.id %}"> edit entry</a> 按钮
3. <p align="right"></p> 靠右
4. 404表示文件或资源未找到; 500-内部服务器错误; 400-错误的请求

### 完善
1. 加入标题 （bingo）
2. 加入删除功能（bingo）
3. 删除按钮得离得远一点（bingo）
4. 管理员权限（cao,作为用户不行,进到服务器就行了）
5. 界面美化（bingo）

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
