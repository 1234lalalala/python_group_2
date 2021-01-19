import pickle,re
data = pickle.load(open('danmu_time.vec','rb'))
for key in data:
    # print(data[key])
    c_time = data[key]['time']
    tag = data[key]['tag']
    out = open(f'./ret/{tag}.txt','a',encoding='utf8')
    for s,t in data[key]['danmu']:
        if re.search('^\[.*\]',s):
            if len(s.split(',')) > 5:
                print(s)
                s = s.split(',')[4]
        out.write(s+'\t'+str(float(t)/c_time) + '\n')
