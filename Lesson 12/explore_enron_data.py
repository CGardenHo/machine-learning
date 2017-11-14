#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:27:57 2017

@author: cgarden
"""

#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).
    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }
    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:
    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../datasets_Questions/final_project_dataset.pkl", "r"))
# How many data points (people) are in the dataset?
len(enron_data)

##### For each person, how many features are available?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3035498566/m-3010518798
len( enron_data["SKILLING JEFFREY K"].keys()) # 21

##### The “poi” feature records whether the person is a person of interest, according to our definition. How many POIs are there in the E+F dataset?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3021858558/m-3011778732
len( [1 for person in enron_data if enron_data[person]['poi'] ] ) # 18

# How many POIs are there in total?
poi_reader = open('../Datasets_Questions/poi_names.txt', 'r')
poi_reader.readline() # skip url
poi_reader.readline() # skip blank line

poi_count = 0
for poi in poi_reader:
	poi_count += 1

print poi_count # 35

##### What is the total value of the stock belonging to James Prentice?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3025828584/m-3010568605

[s for s in enron_data.keys() if "PRENTICE" in s] # ['PRENTICE JAMES']
enron_data['PRENTICE JAMES'].keys()
enron_data['PRENTICE JAMES']['total_stock_value'] # 1095040


# How many email messages do we have from Wesley Colwell to persons of interest?
enron_data["COLWELL WESLEY"]["from_this_person_to_poi"] # 11

# Whats the value of stock options exercised by Jeffrey K Skilling?
enron_data["SKILLING JEFFREY K"]["exercised_stock_options"] # 19250000

##### Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)? 
##### How much money did that person get?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3017538609/m-3005068624
execs = [s for s in enron_data.keys() if ("SKILLING" in s) or ("LAY" in s) or ("FASTOW" in s) ] 
max( [(enron_data[person]['total_payments'],person) for person in execs] ) # (103559793, 'LAY KENNETH L')

##### How many folks in this dataset have a quantified salary? What about a known email address?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3003098655/m-3003048586
len([enron_data[person]['salary'] for person in enron_data if enron_data[person]['salary'] != 'NaN']) # 95
len([enron_data[person]['email_address'] for person in enron_data if enron_data[person]['email_address'] != 'NaN' ] # 111

# How many people have NaN for total_payments? What is the percentage of total?
no_total_payments = len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN'))
print float(no_total_payments)/len(enron_data) * 100 #14.3835616438

# What percentage of POIs in the data have "NaN" for their total payments?
POIs = dict((key,value) for key, value in enron_data.items() if value['poi'] == True)
number_POIs = len(POIs)
no_total_payments = len(dict((key, value) for key, value in POIs.items() if value["total_payments"] == 'NaN'))
print float(no_total_payments)/number_POIs * 100  #0

# If 10 POIs with NaN total_payments were added, what is the new number of people? 
# What is the new number of people with NaN total_payments?#156, 31
print len(enron_data) + 10
print 10 + len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN'))

# What is the new number of POIs?
print 10 + len(POIs) #28

# What percentage have NaN for their total_payments?
print float(10)/(10 + len(POIs))*100 #35.7142857143
