# coding:utf-8
import itchat
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

import numpy as np
import PIL.Image as Image
import os

itchat.login()
friends = itchat.get_friends(update=True)[0:]
tList = []
os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join('/Users/t-mac/desktop', "640.jpeg")))

for i in friends:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    tList.append(
        signature)
    # 拼接字符串
    text = "".join(tList)
    #  jieba分词
    wordlist_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_jieba)
    #  wordcloud词云

    #  这里要选择字体存放路径，这里是Mac的，win的字体在windows／Fonts中
    my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                             max_font_size=40, random_state=42,
                             font_path='/Users/sebastian/Library/Fonts/Arial Unicode.ttf').generate(wl_space_split)

image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
