import pandas as pd
import numpy as np

df = pd.read_table('0512_post_info.txt',sep='\t',names = ["post_id","duration_time","face","text"],index_col ="post_id")

df = df.sort_index(ascending=True)
df1 = df[df["text"] != "0"]
m,n = df1.shape
print(m,n)


f = open("vectors.txt","r")
lines = f.readlines()
f.close()
a,b = len(lines),len(lines[1].strip().split(" "))
print(a,b)
vector_dic = {}

for i in range(a):
    if i % 10000 == 1:
        print(i/a)
    s = lines[i].strip().split(" ")
    if len(s) != 251:
        print("mistake",s)
    else:
        vector_dic[s[0]] = s[1:]
print("over",len(vector_dic))

max_length = 100
content = np.zeros((m,max_length,250))


t = 0
for text in df["text"]:
    s = text.strip().split(",")
    s = [str(p) for p in s ]
    if len(s) == 1 and int(s[0]) == 0:
        print(t,s)
        t += 1
    else:
        if len(s)<= max_length:
            for i in range(len(s)):
                if s[i] in b:
                    content[t,i,:] = b[s[i]]
                else:
                    content[t,i,:]= np.random.uniform(-0.1,0.1,size=250)
        elif len(s) > max_length:
            for i in range(max_length):
                if s[i] in b:
                    content[t,i] = b[s[i]]
                else:
                    content[t,i,:]= np.random.uniform(-0.1,0.1,size=250)
        else:
            print("mistake")
        t += 1

np.save("content_text.npy",content)
