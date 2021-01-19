import json,pprint
import pickle
c_time = pickle.load(open('./ctime.vec', 'rb'))
# print(c_time)
def process(s):
    return (s['content'],s['p'].split(',')[0])
def get_content(a):
    a = json.loads(a.strip())
    # pprint.pprint(a)
    # {'aid':None,'tags':[('tag_name','type'),('tag_name','type')],'upData':['fans',],'videoData':['ctime','duration','pages':{'dimension': ['height','rotate','width']}
    # ,'stat':['coin','danmaku','like','favorite','reply','view','share'],'tname':None,"title":None]}
    data = {}
    data['cid'] = a['cid']
    data['danmu'] = [process(i) for i in a['danmu']]
    data['time'] = c_time[ a['cid']]['duration']
    data['tag'] = c_time[ a['cid']]['tname']
    return data

def get_file(f_list):
    ret = {}

    for f_name in f_list:
        with open(f_name,encoding='utf8') as f:
            for a in f:
                # print(a)
                try :
                    data = get_content(a)
                except:
                    print(a[8:18])
                    continue
                ret[data['cid']] = data
                # print(ret)
                # break
    print(len(ret))
    return ret

ret = get_file(['video_danmu.json','video_danmu2.json','video_danmu_1500_1600.json','video_danmu_1600_1700.json','video_danmu_1700_2000.json','video_danmu_2000_2200.json'])
pickle.dump(ret,open('./ret/danmu_time.vec','wb'))
for key in ret:
    data = ret[key]
    f_name= './danmu/' + data['tag'] + '.txt'
    with open(f_name,'a',encoding='utf8') as f:
        for i in data['danmu']:
            f.write(i[0] + '\n')