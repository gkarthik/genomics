import pysam
import pandas as pd
import matplotlib.pyplot as plt

bamfile = pysam.AlignmentFile("/Users/karthik/Downloads/ENCFF000MUK_2.bam", "rb")
print(bamfile.header)

iter=bamfile.fetch(until_eof=True)
reads=[]
df = pd.DataFrame(columns=["quality"])
count = 0
q = []
for read in iter:
    quality = read.mapping_quality
    q.append(quality)
df['quality'] = q
cdf = pd.DataFrame(columns=['count'])
for i in set(q):
    cdf.loc[i] = q.count(i)
plt.figure()
p = cdf.plot(kind= 'bar')
plt.savefig('plot_tmp.png')




