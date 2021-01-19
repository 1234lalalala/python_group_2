import json,pprint
import pickle


def get_content(a):
    a = json.loads(a.strip())
    pprint.pprint(a)

    # {'aid':None,'tags':[('tag_name','type'),('tag_name','type')],'upData':['fans',],'videoData':['ctime','duration','pages':{'dimension': ['height','rotate','width']}
    # ,'stat':['coin','danmaku','like','favorite','reply','view','share'],'tname':None,"title":None]}
    data = {}
    data['aid'] = a['aid']
    data['cid'] = a['videoData']['cid']
    data['bvid'] = a['videoData']['bvid']
    data['tags'] = [(i['tag_name'], i['type']) for i in a['tags']]
    data['fans'] = a['upData']['fans']
    data['ctime'] = a['videoData']['ctime']
    data['duration'] = a['videoData']['duration']
    data['dimension'] = [a['videoData']['pages'][0]['dimension'][i] for i in ['height', 'rotate', 'width']]
    data['coin'] = a['videoData']['stat']['coin']
    data['danmaku'] = a['videoData']['stat']['danmaku']
    data['like'] = a['videoData']['stat']['like']
    data['favorite'] = a['videoData']['stat']['favorite']
    data['reply'] = a['videoData']['stat']['reply']
    data['view'] = a['videoData']['stat']['view']
    data['share'] = a['videoData']['stat']['share']
    data['tname'] = a['videoData']['tname']
    data['title'] = a['videoData']['title']
    # print(a)
    return data

def get_file(f_list):
    ret = {}
    c_time = {}
    for f_name in f_list:
        with open(f_name,encoding='utf8') as f:
            for a in f:
                try :
                    data = get_content(a)
                except:
                    print(a)
                    continue
                ret[data['aid']] = data
                c_time[data['cid']] = data
                break
    print(len(ret))
    # pickle.dump(ret,open('./video_data.vec','wb'))
    # pickle.dump(c_time, open('./ctime.vec', 'wb'))


get_file(['video_content.json','video_content1.json','video_content2.json','video_content_1500_1600.json','video_content_1600_1700.json','video_content_1700_2000.json','video_content_2000_2200.json'])