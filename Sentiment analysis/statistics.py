#统计每一个分类下的弹幕pos和neg分布
def get_all_senti(f):
    return [int(i.strip().split('\t')[-1]) for i in open(f,encoding='utf8') if i.strip()]

def get_all_senti1(f):
    ret = []
    for i in open(f, encoding='utf8'):
        print(i)
        ret.append(int(i.strip().split('\t')[-1]))
    return ret
import os
for i in os.listdir('data_senti'):
    ret = get_all_senti('data_senti/' + i)
    print(i,len([i for i in ret if i>0]),len([i for i in ret if i<0]),len([i for i in ret if i==0]))