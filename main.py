import pandas as pd
from sklearn import svm

def input_data():
  return pd.read_csv('./data/train.csv')

x = list(p for p,s,a in zip(input_data()['pclass'],input_data()['sex'],input_data()['age']))
y = list(input_data()['survival'])
print(x)



