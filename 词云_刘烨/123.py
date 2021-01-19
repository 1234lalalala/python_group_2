#encoding=utf-8
import numpy as np
from PIL import Image
import wordcloud
import jieba
import os
a = os.listdir('./danmu')

stopword=[i.strip() for i in open('./stop_words.txt',encoding='utf8')]
def func1(f):
	file = open(f,encoding="utf-8")
	result = file.read()
	file.close()
	return result

def func2(words,f):
	wordList = jieba.lcut(words)
	mk = np.array(Image.open('3.png'))
	c = wordcloud.WordCloud(scale=4,stopwords=stopword,background_color='white',mask=mk,font_path="simsun.ttc",)
	c.generate(" ".join(wordList))
	c.to_file(f)

for f_name in a:
	ret = func1('danmu/'+f_name)
	func2(ret,'picture/'+f_name[:-3] + '.jpg')
