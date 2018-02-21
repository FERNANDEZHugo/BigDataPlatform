import pandas as pd

output=pd.read_csv('/home/hugo/Logiciel/hadoop-2.9.0/output.csv',sep='\t',header=None, names=['word','Callwild','Defoe'])

output=output.sort_values(by=['Callwild'],ascending=False)

print(output.head(20))

output=output.sort_values(by=['Defoe'],ascending=False)

print(output.head(20))