import pickle,pprint
a = pickle.load(open('../bilibili_crawl/video_data.vec','rb'))
pprint.pprint(a[46900196])
data_all = []
columns = list(a[46900196].keys())
for id in a:
    ret = [id]+[a[id][i] for i in columns]
    data_all.append(ret)
print(data_all)
columns = ['id'] + columns

import pandas
data_df = pandas.DataFrame(data_all,columns=columns)
print(data_df.head())
pickle.dump(data_df,open('pd_data.vec','wb'))