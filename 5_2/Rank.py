import pandas as pd

output=pd.read_csv('/home/hugo/Logiciel/hadoop-2.9.0/pagerank.csv',sep='\t',header=None, names=['node','pagerank'])

output=output.sort_values(by=['pagerank'],ascending=False)

print(output.head(20))
