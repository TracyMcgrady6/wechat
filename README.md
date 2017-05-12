# wechat
python 玩微信，超有趣
## itchat

无意间发现的一个有意思的开源项目itchat，相当于微信api，扫码登录后去抓包爬取信息，还可以post去发送信息。
GitHub star数量4，非常火，作者是@LittleCoder，已经把微信的接口完成了，大大的方便了我们对微信的挖掘，以下的功能也通过itchat来实现。

安装itchat这个库
```python
pip install itchat
```
先来段简单的试用，实现微信的登录，运行下面代码会生成一个二维码，扫码之后手机端确认登录，就会发送一条信息给‘filehelper’，这个filehelper就是微信上的文件传输助手。

```python
import itchat
# 登录
itchat.login()
#  发送消息
itchat.send(u'你好', 'filehelper')
```

##1. 微信好友男女比例

想统计下自己微信里好友的性别比例，当然也是很简单，先获取好友列表，统计列表里性别计数
```python
import itchat

# 先登录
itchat.login()
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0
# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算# 1表示男性，2女性
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
# 总数算上，好计算比例啊～
total = len(friends[1:])
# 好了，打印结果
print(u"男性好友：%.2f%%" % (float(male) / total * 100))
print(u"女性好友：%.2f%%" % (float(female) / total * 100))
print(u"其他：%.2f%%" % (float(other) / total * 100))
```
结果：

![](http://upload-images.jianshu.io/upload_images/2127249-d6abf7e2c3ed4599.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



结果是个意外。。。。
##2. 好友昵称，备注，以及个性签名
其实还可以爬出很多每个好友的其他属性，比如家乡等等信息！
直接上代码：
```python
# coding:utf-8
import itchat

# 先登录
itchat.login()
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
for i in friends:
    # 获取个性签名
    # print(i)
    name = i['RemarkName']
    nickname = i['NickName']
    # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji",
                                                                                        "")
    print(name + "," + nickname + "," + signature)
```
运行效果如图：


![](http://upload-images.jianshu.io/upload_images/2127249-870ed5909953a3e1.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##3.好友个性签名词云
获取好友列表的时候，返回的json信息中还看到了有个性签名的信息，脑洞一开，把大家的个性签名都抓下来，看看高频词语，还做了个词云。
先全部抓取下来 
打印之后你会发现，有大量的span，class，emoji，emoji1f3c3等的字段，因为个性签名中使用了表情符号，这些字段都是要过滤掉的，写个正则和replace方法过滤掉
贴代码：
```python
# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Imaged
import itchat

os.path.dirname(__file__)
alice_coloring = np.array(Imaged.open(os.path.join('/Users/t-mac/desktop', "640.jpeg")))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                         max_font_size=40, random_state=42,
                         font_path='/Users/sebastian/Library/Fonts/Arial Unicode.ttf').generate(wl_space_split)
image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
# 保存图片 并发送到手机
my_wordcloud.to_file(os.path.join('/Users/t-mac/desktop', "wechat_cloud.png"))
itchat.send_image("wechat_cloud.png", 'filehelper')
```
效果如图：


![](http://upload-images.jianshu.io/upload_images/2127249-4242f9d0b02454fa.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
