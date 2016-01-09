# coding=utf-8

# write code...
# -*- coding: utf-8 -*-
import  random
from sklearn.svm import SVC
from sklearn import grid_search
import  datetime

from sklearn.metrics import precision_recall_fscore_support
import numpy as np

# 学習データ
print "データ取り込むよ"
data_training_tmp = np.loadtxt('data.csv', delimiter=',')

# for i in xrange(10):
#     data_training_tmp.append([random.randint(0,2),random.randint(0,2),random.randint(0,1),0])
print "正規化するよ"
normalizedT = []
for column in xrange(len(data_training_tmp[0]) - 1):
	row = data_training_tmp[:,column]
	mean = np.mean(row)
	std = np.std(row)
	newRow = []
	for data in row:
		if std != 0:
			newRow.append((data - mean)/std)
		else:
			newRow.append(float(0))
	normalizedT.append(newRow)
normalizedT.append(data_training_tmp[:,len(data_training_tmp[0]) -1].transpose())
normalized = np.array(normalizedT)
normalized = normalized.transpose()
# for i in xrange(len(data_training_tmp)):

# print normalized
data_training = [[x[0], x[1], x[2], x[3], x[4]] for x in normalized]
label_training = [int(x[5]) for x in normalized]

data_training = np.array(data_training)
label_training = np.array(label_training)

# print type(data_training[0][0])
# print type(label_training[0])
# data_training = [[x[0], x[1], x[2], x[3], x[4]] for x in data_training_tmp]
# label_training = [int(x[5]) for x in data_training_tmp]

# 試験データ
#data_test = np.loadtxt('CodeIQ_mycoins.txt', delimiter=' ')
data_test_raw = np.loadtxt('data.csv', delimiter=',')

normalizedTtest = []
for column in xrange(len(data_test_raw[0]) - 1):
	row = data_test_raw[:,column]
	mean = np.mean(row)
	std = np.std(row)
	newRow = []
	for data in row:
		if std != 0:
			newRow.append((data - mean)/std)
		else:
			newRow.append(float(0))
	normalizedTtest.append(newRow)
normalizedTtest.append(data_test_raw[:,len(data_test_raw[0]) -1].transpose())
print "配列の長さ",len(normalizedTtest[0])
normalizedTest = np.array(normalizedTtest)
print "npArrayにしたもののShape: ",str(normalizedTest.shape)
print "npArrayの配列の長さ: ",len(normalizedTest[0])
normalizedTest = normalizedTest.transpose()
# for i in xrange(len(data_training_tmp)):
print "transposeあと: ",normalizedTest.shape
# print normalized
data_test = [[x[0], x[1], x[2], x[3], x[4]] for x in normalizedTest]
label_test = [int(x[5]) for x in normalizedTest]

data_test = np.array(data_test)
label_test = np.array(label_test)
data_ttest = []
# data_test.append([0.8,0.6,1,1,1])
for i in xrange(5):
    data_ttest.append(data_test[:,i])
data_ttest = np.array(data_ttest)
data_ttest = data_ttest.transpose()


# data_test = []
# # data_test.append([0.8,0.6,1,1,1])
# for i in xrange(5):
#     data_test.append(data_training[:,i])
# data_test = np.array(data_test)
# data_test = data_test.transpose()


# 学習
print "学習系動かすよ"
print datetime.datetime.today()
estimator = SVC(kernel = 'linear', class_weight = {1: 4})

costParams = []
for i in xrange(-3, 5):
	costParams.append(2 ** i)

print costParams

params = {'C': costParams}
clf= grid_search.GridSearchCV(estimator, params)
clf.fit(data_training, label_training)
# estimator.fit(data_training, label_training)

# 予測するよー
print "予測するよ"
# label_prediction = estimator.predict(data_test)
label_prediction = clf.predict(data_ttest)

print clf.best_params_
print clf.best_score_
# print estimator.get_params(1)
# print clf.score(data_test, label_test)
# print(label_prediction)
# print(estimator.score(data_training, label_training))
print precision_recall_fscore_support(label_test, label_prediction)
print datetime.datetime.today()
