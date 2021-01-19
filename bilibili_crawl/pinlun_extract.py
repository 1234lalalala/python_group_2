import pprint,json,pickle
aid_tname = pickle.load(open('ret/video_data.vec', 'rb'))
def func(s,aid):
    try:
        with open(f"./ret/review_{aid_tname[aid]['tname']}.txt",'a',encoding='utf8') as out:
            out.write(s+'\n')
    except:
        pass
def main(f_name):
    with open(f_name,encoding='utf8') as f:
        for i in f:
            a = json.loads(i.strip())
            aid = (a['aid'])
            for j in (a['review']):
                if 'data' in j and j['data'][ 'hots']:
                    for k in (j['data'][ 'hots']):
                        func(k['content']['message'],aid)
                        if k['replies']:
                            for l in k['replies']:
                                func(l['content']['message'],aid)

for i in ['video_review.json','video_review1.json','video_review2.json','video_review_1500_1600.json','video_review_1600_1700.json','video_review_1700_2000.json','video_review_2000_2200.json']:
    print(i)
    main(i)