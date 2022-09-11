from collections import defaultdict
import re
import pickle
print("Введите асолютный путь файла для обучения")
s=input()

try:
    with open('model.pkl', 'rb') as file:
        f=pickle.load(file)
        sl=defaultdict(dict,f)
except:
    sl=defaultdict(dict)
with open(s, encoding='utf-8') as d:
    q=''
    for c in d:
        q+=c.strip().lower()
    result = re.split(r'\s*[?,!–().;]\s*', q)
    for c in result:
        g=re.split(r'\s*[,: -]\s*', c)
        g=list(map(lambda x: x.lower(), g))
        for j in range(len(g)-1):
            for i in range(j+1,len(g)):
                tup=tuple(g[j:i])
                if g[i] in sl[tup].keys():
                    sl[tup][g[i]]+=1
                else:
                    sl[tup][g[i]]=1
with open('model.pkl', 'wb') as qw:
    sl=dict(sl)
    pickle.dump(sl, qw)
print(sl)