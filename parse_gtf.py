import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()
df = pd.read_table('/Users/karthik/Downloads/ENCFF000MUO.gtf', sep = '\t', header = None)
print(df.head())

transcript_ids = []
FPKM = []
c = 0
for i in df.index:
    c+= 1 
    s = str(df[8][i])
    t = s.split(';')[1].split("\"")[1]
    f = s.split(';')[2].split("\"")[1]
    transcript_ids.append(t)
    FPKM.append(f)
tdf = pd.DataFrame(columns=["Read Count", "FPKM"])
for i in set(FPKM):
    tdf.loc[i] = FPKM.count(i)
tdf["FPKM"] = tdf.index.values
tdf = tdf.sort('FPKM')
max = tdf['FPKM'].max()
min = tdf['FPKM'].min()
avg = (min + max)/2
tdf.drop("FPKM", axis = 1)
print(max, min, avg)
plt.figure()
tdf.plot(logy=True, kind='line', xticks=[min, avg, max])
plt.savefig('plotfpkm.png')




