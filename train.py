import numpy as np
from sklearn import linear_model
from sklearn import svm
from sklearn.linear_model import lasso_path, enet_path

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error

from sklearn.utils import shuffle

import json

with open('dataset.txt', 'r') as f:
    dataset = json.load(f)
f.closed


features = dataset[0] #['WAIST_CIRC_NATURAL', 'STATURE', 'WEIGHT', 'CHEST_CIRC', 'NECK_CIRC-BASE']
X = []
y = []


for d in dataset[1:]:
    X.append(d[1:4])
    y.append(d[4])

X, y = shuffle(X, y)

print('Finding {0} with {1}'.format(features[4], ', '.join(features[:4])))
X_train, X_test = X[:1000], X[1000:]
y_train, y_test = y[:1000], y[1000:]


"""
clf = linear_model.SGDRegressor()
clf.fit(X_learn, y_learn)
clf.predict(X_test)
print(clf.score(X_test, y_test))
"""

#estimator = svm.LinearSVR()
estimator = linear_model.LassoCV()
fitted = estimator.fit(X_train, y_train)
y_pred = estimator.predict(X_test)


#i=0
#for p in predicted:
    #print("Predicted %s for %s" % p, y_test[i])
    #i += 1

print('SCORE: {0}'.format(estimator.score(X_test, y_test)))
print('Mean absolute error: {0}'.format(mean_absolute_error(y_test, y_pred)))
print('Median absolute error: {0}'.format(median_absolute_error(y_test, y_pred)))
