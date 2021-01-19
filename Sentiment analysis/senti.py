import jieba
stop_words = [i.strip() for i in open('./stop_words.txt',encoding='utf8')]
def text_cut(s):
    ret = jieba.lcut(s)
    return [i for i in ret if i not in stop_words]

def get_dict(f):
    return ([i.strip() for i in open(f) if i.strip()])

pos = set(get_dict('正面情感词语（中文）.txt') + get_dict('正面评价词语（中文）.txt')+get_dict('正面情感词语（英文）.txt')+ get_dict('正面评价词语（英文）.txt'))
neg = set(get_dict('负面情感词语（中文）.txt') + get_dict('负面评价词语（中文）.txt')+get_dict('负面情感词语（英文）.txt')+ get_dict('负面评价词语（英文）.txt'))


def get_senti_score(s):
    ret = 0
    for i in text_cut(s):
        if i in pos:
            ret += 1
        elif i in neg:
            ret -= 1
    return ret

def main(f_name):
    out = open('data_senti/'+f_name,'w',encoding='utf8')
    with open('data_process/'+f_name,encoding='utf8') as f:
        for i in f:
            if i.strip():
                out.write(i.strip()+'\t' + str(get_senti_score(i.strip())) + '\n')
import os
for i in os.listdir('data_process'):
    main(i)