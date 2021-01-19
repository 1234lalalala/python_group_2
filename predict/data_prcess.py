import re,emoji
def data_process(line):
    ret = re.sub(r'http[:.a-zA-Z/]*','',line)
    ret = re.sub(r'(AV|av)[0-9]*','',ret)
    ret = re.sub(r'@.*?:','',ret)
    ret = emoji.demojize(ret).replace('_',' ')
    ret = re.sub('[\[(].*?[\])]','',ret)
    return ret



def main(f):
    out = open('data_process/'+f,'w',encoding='utf8')
    with open('review/'+f,encoding='utf8') as f:
        for line in f:
            line = line.strip()
            ret = data_process(line)
            if ret:
                out.write(ret+'\n')
import os
for i in os.listdir('review'):
    print(i)
    main(i)
# print(data_process('最新视频！前方高能！进来享受这场华丽的视觉盛宴吧！av50331935'))