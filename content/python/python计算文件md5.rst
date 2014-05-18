python计算文件md5
####################
:title: python计算文件md5
:slug: python_md5
:date: 2014-05-04 16:05:23
:tags: md5,python
:category: python
:author: 创e
:lang: 
:summary: 


Python中，用于加密的md5方法在hashlib模块中，文件的MD5校验码是根据文件的内容生成的信息摘要，方法如下:

.. code-block:: python

    from hashlib import md5
 
    def md5_file(name):
        m = md5()
        a_file = open(name, 'rb')    #使用二进制格式读取文件内容
        m.update(a_file.read())
        a_file.close()
        return m.hexdigest()
     
    if __main__ == '__init__':
        print md5_file('/home/ce/1.txt')

