本来我不想写说明的,但是,我不得不写,因为该主题已经不是最初的一个版本了,并且经过我很多次的修改,加入了很多只适合我的东西,所以需要说明一下,以免到手后无法使用.

#JekyllBootstrap4Pelican

顾名思义,便知,该主题为JekyllBootstrap到Pelican的mod主题.所以版权由JekyllBootstrap的作者所有.

在这里存放了一个最初的版本,如果你有兴趣查看当时的版本是多么的糟糕,请移步[https://gitcafe.com/lanbing/CodeNut/tree/master/Pelican/JekyllBootstrap4Pelican-0.1](https://gitcafe.com/lanbing/CodeNut/tree/master/Pelican/JekyllBootstrap4Pelican-0.1)

##使用方法

下载该源码[https://gitcafe.com/lanbing/CodeNut/tree/master/Pelican/JekyllBootstrap4Pelican-update](https://gitcafe.com/lanbing/CodeNut/tree/master/Pelican/JekyllBootstrap4Pelican-update),将其JekyllBootstrap4Pelican-update放到Pelican的根目录下,也就是和content是同级的.

建议将JekyllBootstrap4Pelican-update重命名为JekyllBootstrap4Pelican.

然后在`pelicanconf.py`中加入/替换代码`THEME = "JekyllBootstrap4Pelican"` .

##需要的插件

我在该主题中引用了一些插件,分别如下:

neighbors,上一篇 下一篇,获取地址 [https://gitcafe.com/lanbing/CodeNut/tree/master/Pelican/Pelican-plugins](https://gitcafe.com/lanbing/CodeNut/tree/master/Pelican/Pelican-plugins)

对应的主题文件代码为`\JekyllBootstrap4Pelican-update\templates\article.html`中的.

```
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

random_article 随机日志,对应`\JekyllBootstrap4Pelican-update\templates\base.html`

    <li><a href="/random.html">Random</a></li>

related_posts,相关日志,对应 `\JekyllBootstrap4Pelican-update\templates\article.html`

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

Latest Articles ,最新日志,对应`\JekyllBootstrap4Pelican-update\templates\article.html`

```
	<h4>Latest Articles</h4>
	<script language="JavaScript" src="http://feed2js.org/feed2js.php?src=http%3A%2F%2Fwww.codenut.net%2Frss.xml&num=10&utf=y"  charset="UTF-8" type="text/javascript"></script>
```

sitemap(可选),无对应代码.

相关使用方法,请参考 [http://www.codenut.net/post/2013-06-30-pelican-plugins/](http://www.codenut.net/post/2013-06-30-pelican-plugins/) 或 [https://gitcafe.com/lanbing/CodeNut/tree/master/Pelican/Pelican-plugins](https://gitcafe.com/lanbing/CodeNut/tree/master/Pelican/Pelican-plugins)

##Disqus社会化评论

请修改`\JekyllBootstrap4Pelican-update\templates\article.html`中

    var disqus_shortname = 'codenut'; // required: replace example with your forum shortname

的ID为自己的ID即可.
