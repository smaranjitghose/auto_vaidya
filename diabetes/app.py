import streamlit as st  
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn import metrics
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb



def predict(X,algo):
        
    if(algo=='svc'):
        model = pickle.load(open('test/models/svc.pkl', 'rb'))

    if(algo=='logreg'):
        model = pickle.load(open('test/models/logreg.pkl', 'rb'))

    if(algo=='knn'):
        model = pickle.load(open('test/models/knn.pkl', 'rb'))

    if(algo=='tree'):
        model = pickle.load(open('test/models/tree.pkl', 'rb'))

    if(algo=='xgb'):
        model = pickle.load(open('test/models/xgb.pkl', 'rb'))

    X = np.array(X)
    ss = StandardScaler()
    X = ss.fit_transform(X.reshape(-1, 1))
    #print(X.shape)
    ans=(model.predict(X.T))
    #print(ans)
    if(ans==0):
        #print("Healthy :)")
        return 0
    else:
        #print("Diabetic :(")
        return 1

st.title('Diabetes Prediction App!!')

age=st.number_input('Age',min_value=1,max_value=125)
bmi=st.number_input('Body Mass Index',min_value=15,max_value=45)
dpf=st.number_input('Diabetic Pedigree Fraction',min_value=0.0,max_value=5.0)
preg=st.number_input('Pregnancies(* for males enter 0)',min_value=0,max_value=20,value=1)

ins=st.number_input('Insulin',min_value=0,max_value=250,value=0)
skin=st.number_input('Skin Thickness',min_value=10,max_value=45)
glu=st.number_input('Glucose',min_value=60,max_value=325)
bp=st.number_input('Blood Pressure(*Enter Diastolic Press. in mm of hg)',min_value=30,max_value=180)

algo=st.radio("Which algo would you prefer",('KNN','SVC','Logisitc Regression','Decision Tree','XGBoost'))  


if(algo=='KNN'):
    algo='knn'
if(algo=='SVC'):
    algo='svc'
if(algo=='Logisitc Regression'):
    algo='logreg'
if(algo=='Decision Tree'):
    algo='tree'
if(algo=='XGBoost'):
    algo='xgb'

if(st.button('Submit')):
    if(preg is None or glu is None or age is None or ins is None or skin is None or bp is None or dpf is None or bmi is None or algo is None ):
        st.error('Please enter all fields')
    X=np.array([preg,glu,bp,skin,ins,bmi,dpf,age])
    X = [float(i) for i in X]
    ans=predict(X,algo)
    if(ans==0):
        st.success("You are healthy :)")
        st.balloons()
    else:
        st.warning("You are Diabetic :(")
    