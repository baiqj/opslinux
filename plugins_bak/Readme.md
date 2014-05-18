本版本作为 [https://github.com/getpelican/](https://github.com/getpelican/) 的克隆版存在,最新更新请移步 [https://github.com/getpelican/](https://github.com/getpelican/) .

附文:

##几个不错的Pelican插件以及使用介绍 

原文 [http://www.codenut.net/post/2013-06-30-pelican-plugins/](http://www.codenut.net/post/2013-06-30-pelican-plugins/)

Pelican资源下载 [https://github.com/getpelican](https://github.com/getpelican)

Pelican插件 [https://github.com/getpelican/pelican-plugins](https://github.com/getpelican/pelican-plugins)

我感觉有用的插件主要有下面几个

neighbors,邻居导航,也就是我们常说的上一篇下一篇文章

random_article,随机日志,使用一个js跳转到随机页面.(并非直接输出随机日志..)

related_posts,相关文章,根据tags判断的.

sitemap,地图,你懂的.

要使用插件,你首先要去下载(废话).

然后建立一个plugins的文件夹.与content是同级的.

![](http://files.xxdns.net/20130630081129883.jpg)

然后打开pelicanconf.py,定义插件目录和启用插件.

在该段中,我已经包含了几个插件的参数,不需要的自行删减.

```
#加载plugins
PLUGIN_PATH = "plugins"
PLUGINS = ["sitemap","neighbors","random_article","related_posts"]
#sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.8,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
#随机跳转到某一日志
RANDOM = 'random.html'
#相关文章
RELATED_POSTS_MAX = 10
```

邻居导航,在模版中调用如下代码,可根据自己的情况修改:

```html
   <div class="pagination">
      <ul>
	  {% if article.prev_article %}
        <li class="prev"><a href="{{ SITEURL }}/{{ article.prev_article.url}}">← Previous</a></li>
		{% else %}
        <li class="prev"><a href="/">← Previous</a></li>
		{% endif %}
        <li><a href="/archives.html">Archive</a></li>
		{% if article.next_article %}
        <li class="next"><a href="{{ SITEURL }}/{{ article.next_article.url}}">Next →</a></li>
		{% else %}
        <li class="next"><a href="/">Next →</a></li>
		{% endif %}
      </ul>
    </div>
```

相关文章

```
	    {% if article.related_posts %}
	<h4>Related Articles</h4>
        <ul>
        {% for related_post in article.related_posts %}
            <li><a href="{{ SITEURL }}/{{ related_post.url }}">{{ related_post.title }}</a></li>
        {% endfor %}
        </ul>
    {% endif %}	
```

随机日志链接

    <li><a href="/random.html">Random</a></li>

sitemap(可选)

    <li><a href="/sitemap.xml">sitemap</a></li>