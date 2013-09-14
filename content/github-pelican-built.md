Title: 使用github和pelican搭建本站博客 
Date: 2013-07-13
Category: pelican
Tags: pelican, github
## 使用github和pelican搭建本站博客 ##

### 安装virtualenv虚拟环境 ###
安装虚拟环境是为了防止污染，linux本身的python环境

    easy_install virtualenv
### 使用virtualenv ###
```bash
virtualenv pelican   #创建虚拟环境
cd pelican
source bin/activate   #激活虚拟环境
```
### 安装pelican和markdown  ###
pelican 就是生成静态博客的程序<br />
markdow 是写博客使用的轻量级标记语言,不会使用的同学可以查看[帮助](http://wowubuntu.com/markdown/)

    $ pip install pelican
    $ pip install Markdown
    $ pip install ghp-import

### 建立blog目录 ###

    $ mkdir myblog
    $ cd myblog
### 开始创建 ###

    $ pelican-quickstart
基本按照提示设置就可以，稍后可以在pelicanconf.py文件中手动修改。
```bash
.
|-- content #所有文章放于此目录
|-- develop_server.sh  #用于开启测试服务器
|-- Makefile   #方便管理博客的Makefile
|-- output #静态生成文件
|-- pelicanconf.py #配置文件
|-- publishconf.py #配置文件
```
### 写一篇文章 ###

在`content`目录新建一个`test.md`文件, 填入一下内容:
```bash
Title: 文章标题
Date: 2013-04-18
Category: 文章类别
Tag: 标签1, 标签2    
这里是内容
```    
然后执行:

    make html
用以生成html

然后执行

    ./develop_server.sh start
开启一个测试服务器, 这会在本地 8000 端口建立一个测试web服务器, 可以使用浏览器打开:`http://localhost:8000`来访问这个测试服务器, 然后就可以欣赏到你的博客了


### Github上的准备 ###

在Github上创建一个新项目，把这个项目clone到myblog文件夹下。然后按照Github的规定建立一个没有父节点的分支gh-pages。<br />
注：在是用分支创建github的blog的时候，要先确保自己的github上有例如：zbing3.github.io命名的项目并且在`settings`中开启Github Pages
如图：
![Alt Github Pages](/static/upload/20130713144403.jpg)
点击`Automatic Page Generator`开启Github Pages服务

进入output目录中：
```bash
$ git init
$ git checkout --orphan gh-pages
$ git add .
$ git commit -m "first post"
$ git remote add origin git@github.com:zbing3/opslinux.git
$ git push origin gh-pages
```
这样上传完代码等10分钟左右，即可在浏览器中使用```http://zbing3.github.io/myblog```就能访问到自己的博客

## 未完待续…… ##
