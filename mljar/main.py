from mljar_client import MljarClient

from mljar import Mljar
import pandas as pd
import numpy as np
fname = '/home/piotr/webs/mljar/test/data/binary_part_iris_converted.csv'

df = pd.read_csv(fname)
print 'Data shape', df.shape
print 'Data columns', df.columns
#print df['class'].columns
cols = ['sepal length', 'sepal width', 'petal length', 'petal width']
#print df[cols].columns

model = Mljar(project = 'Example-Api', experiment = 'Experiment 1')
model.fit(X = np.array(df[cols]), y = df['class'])