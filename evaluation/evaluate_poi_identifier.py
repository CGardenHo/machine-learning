#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

data_dict = pickle.load(open("../../datasets_Questions/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
clf = DecisionTreeClassifier()
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
	features, labels, test_size=0.3, random_state=42)
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
print "[Q1] How many POIs are predicted for the test set for your POI identifier?"
print "[A1]", sum(pred) #4
print "[Q2] How many people total are in your test set?"
print "[A2]", len(pred) #29
print "[Q3] If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?"
print "[A3]", pred.tolist().count(0) / float(len(pred)) # 0.862068965517
print "[Q4] Do you get any true positives? (In this case, we define a true positive as a case where both the actual label and the predicted label are 1)"
true_positives = 0
for i in range(len(pred)):
	if (pred[i] == labels_test[i]) and labels_test[i] == 1:
		true_positives += 1
print "[A3]", true_positives #0
print "Precision score:", precision_score(pred, labels_test) #0
print "Recall score:", recall_score(pred, labels_test) #0


#truth = labels_test
prediction = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
truth = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
positives = [1]

binary_truth = [x in positives for x in truth]
binary_prediction = [x in positives for x in prediction]
for t, p in zip(binary_truth, binary_prediction):
    confusion_matrix[t,p] += 1

print confusion_matrix

from sklearn.metrics import precision_score
print "Precision Score: ", precision_score(prediction, truth)
from sklearn.metrics import recall_score
print "Recall Score: ", recall_score(prediction, truth)

#[0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
#[0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
# 0  1  2. 3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19
# 6, 8, 11, 14, 15, 17 # tp 6
# 0, 3, 4, 5, 7, 10, 12, 16, 18 # fn 9
# 1,2,19 #ft 3
# 9, 13, #fn 2
