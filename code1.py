pip install mlxtend 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
df=pd.read_excel('/content/drive/MyDrive/step3/dataset.xlsx', engine='openpyxl')
df.isnull().sum()
df.info()
df=df.drop(['pkSeqID','flgs','proto','state','subcategory','attack','stime','ltime','saddr','daddr',],axis=1)
df.shape
df=df[(df.sport != "0x0303" )]
df=df[(df.sport != "0x000d" )]
df=df[(df.sport != "0x0008" )]
df=df[(df.sport != "0x0011" )]
df['sport']=pd.to_numeric(df['sport'],downcast='float')
df['dport']=pd.to_numeric(df['dport'],downcast='float')
df= df.sample(frac = 1)
X=X.astype({'pkts': 'float','bytes': 'float', 'seq': 'float','spkts': 'float','dpkts': 'float','sbytes': 'float','dbytes': 'float'})
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y_org=le.fit_transform(y)
