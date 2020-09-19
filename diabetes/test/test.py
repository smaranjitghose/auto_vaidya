## scikit learn version used is version 0.23.2.
import argparse
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
from sklearn import metrics
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb

# Argument parser 
# Here the user needs to provide the 8 feature values and the algo he wants to use.
# logreg:Logistic Regression
# svc:SVC
# xgb:Xgboost
# tree:Decision Tree
# knn: K-nearest neighbor 

ap = argparse.ArgumentParser()
# various features
ap.add_argument("-p", "--pregnancies", required=True,help="if man then 0 else number of children for woman")
ap.add_argument("-g", "--glu", required=True,help="Blood Sugar Level of the user")
ap.add_argument("-b", "--bp", required=True,help="Blood Pressure of the user")
ap.add_argument("-s","--skin",required=True,help="skin Thickness of the user")
ap.add_argument("-i", "--insulin", required=True,help="Insulin level of the user")
ap.add_argument("-m", "--bmi", required=True,help="Body Mass Index of the user")
ap.add_argument("-d", "--dpf", required=True,help="Diabetes Pedigree Function of the user")
ap.add_argument("-a", "--age", required=True,help="Age of the user")
# for algos enter
ap.add_argument("-w","--algo", required=True,help="for logistic regression enter logreg for XGBoost enter xgb for SVC enter svc and for knn enter knn for decision tree enter tree")
args = vars(ap.parse_args())

# display 
# print((args['pregnancies'],args['glu'],args['bp'],args['skin'],args['insulin'],args['bmi'],args['dpf'],args['age']))
X=np.array([args['pregnancies'],args['glu'],args['bp'],args['skin'],args['insulin'],args['bmi'],args['dpf'],args['age']])
X = [float(i) for i in X] 
print(X)
# the algorithm selected
print(args['algo'])

algo=args['algo']
if(algo=='svc'):
    model = pickle.load(open('models/svc.pkl', 'rb'))
    print(model)

if(algo=='logreg'):
    model = pickle.load(open('models/logreg.pkl', 'rb'))
    print(model)

if(algo=='knn'):
    model = pickle.load(open('models/knn.pkl', 'rb'))
    print(model)

if(algo=='tree'):
    model = pickle.load(open('models/tree.pkl', 'rb'))
    print(model)

if(algo=='xgb'):
    model = pickle.load(open('models/xgb.pkl', 'rb'))
    print(model)

X = np.array(X)
ss = StandardScaler()
X = ss.fit_transform(X.reshape(-1, 1))
print(X.shape)
ans=(model.predict(X.T))

if(ans==0):
    print("Healthy :)")
else:
    print("Diabetic :(")

