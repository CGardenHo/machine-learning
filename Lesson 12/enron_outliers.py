#!/usr/bin/python

import pickle
import sys
import pandas as pd
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../datasets_Questions/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
#data_dict.pop ('TOTAL', 0) ### there's an outlier--remove it! 

data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


df = pd.DataFrame(data_dict)
df.loc['salary',:] = pd.to_numeric(df.loc['salary',:], errors='coerce')
df.loc['bonus',:] = pd.to_numeric(df.loc['bonus',:], errors='coerce')

print df.loc['salary',:].idxmax(axis=1)  #TOTAL, you may comment row 14

print [name for name in df.columns if df.loc['salary', name] > 10**6 and df.loc['bonus',name] > 5*10**6] 
#'LAY KENNETH L', 'SKILLING JEFFREY K', 'TOTAL'
