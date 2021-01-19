import os
import time
from pprint import pprint

import requests,re,json
from lxml import etree

head  = {'cookie':"cookie: buvid3=7B4BFE65-C844-444A-9034-C9C6F8397C4849018infoc; LIVE_BUVID=AUTO7115526192154991; fts=1552619302; stardustvideo=1; rpdid=|(k|JRl)k)YY0J'ullY|YYuJ); im_notify_type_6715313=0; _uuid=7591483D-F50E-B61F-AE8B-3BCC2B3A347E31738infoc; sid=jb4ngc38; CURRENT_QUALITY=80; CURRENT_FNVAL=80; blackside_state=1; DedeUserID=6715313; DedeUserID__ckMd5=1a5a10df1674d454; SESSDATA=fffc21cf%2C1621500956%2Ceec25*b1; bili_jct=d0aeabd3bce910e3c2937f8cdebb2104; bp_video_offset_6715313=466773055710326638; bp_t_offset_6715313=466773055710326638; PVID=6; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f"}

a = 2000
b = 2200
file_content = f'video_content_{a}_{b}.json'
file_review = f'video_review_{a}_{b}.json'
file_danmu = f'video_danmu_{a}_{b}.json'


def get_video_list(url_num):
    url = f'https://api.bilibili.com/x/web-interface/popular/series/one?number={url_num}'
    data = (requests.get(url).text)
    return (json.loads(data)['data']['list'])

def get_video_content(bvid):
    url = f'https://www.bilibili.com/video/{bvid}'
    data = (requests.get(url).text)
    #数据存储
    with open(file_content,'a',encoding='utf8') as f:
        f.write(re.search(r'ATE__=({.*});',data).group(1)+'\n')

def get_review(aid):
    ret = {}
    ret['aid'] = aid
    ret['review'] = []
    for i in range(1,11):
        time.sleep(0.1)
        #爬取前十页的评论
        url = f'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={i}&type=1&oid={aid}&sort=1&_=1608180136003'
        data = json.loads(requests.get(url).text)
        ret['review'].append(data)
    with open(file_review,'a',encoding='utf8') as f:
        f.write(json.dumps(ret,ensure_ascii=False) + '\n')


def clean_danmu(s):
    _ = re.search(r'<d.*?>(.*?)</d>',s)
    if _:
        content = _.group(1)
    else:
        return None
    p = re.search(r'<d p="(.*?)">.*?</d>',s).group(1)
    return {'content':content,'p':p}
def get_danmu(cid,):
    time.sleep(2)
    url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid}'
    data = requests.get(url,headers=head)
    html = data.content
    html_doc = str(html, 'utf-8')
    danmu_all = re.findall(r'<d p=".*?">.*?</d>',html_doc)
    danmu_all = ([clean_danmu(i) for i in danmu_all])
    with open(file_danmu,'a',encoding='utf8') as f:
        f.write(json.dumps({'cid':cid,'danmu':danmu_all},ensure_ascii=False)+'\n')



if __name__ == '__main__':
    if not os.path.exists('./video.json'):
        with open('./video.json','w',encoding='utf8') as f:
            for i in range(1,92):
                for each in get_video_list(i):
                    f.write(json.dumps(each,ensure_ascii=False)+'\n')


    with open('video.json',encoding='utf8') as f:
        f = [i for i in f]

        for num,line in enumerate(f[a:]):
            print(num+a)
            data = json.loads(line.strip())
            # print(data)
            bvid = (data['bvid'])
            aid = (data['aid'])
            cid = (data['cid'])
            date = data['ctime']
            get_video_content(bvid)
            get_review(aid)
            get_danmu(cid)

