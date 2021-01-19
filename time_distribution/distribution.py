def get_topn(l,n):
    ret = {}
    for i in l:
        if i in ret:
            ret[i] += 1
        else:
            ret[i] = 1
    key = list(ret.keys())
    key.sort(key=lambda x:ret[x],reverse=True)
    return [(i,ret[i]) for i in key[:n]]




def func(f):
    data_dict = {i: [] for i in range(11)}

    with open('ret/'+ f,encoding='utf8') as f_in:
        for i in f_in:
            if len(i.strip().split('\t'))==2:
                # print(i)
                a,b = i.strip().split('\t')
                if float(b)>1:
                    continue
                data_dict[(int(float(b)*10//1))].append(a)

            # break
        for i in range(11):
            out = open(f'result/{i}.txt','a',encoding='utf8')
            out.write(f+'\t' + str(get_topn(data_dict[i],10))+'\n')

import os
for i in os.listdir('./ret'):
    func(i)
