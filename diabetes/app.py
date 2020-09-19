import streamlit as st   

st.title('Diabetes app!!')
st.success("You are healthy :)")
st.warning("You are Diabetic :(")
st.error("Enter all the details")

age=st.number_input('Age',min_value=1,max_value=125)
bmi=st.number_input('BMI',min_value=15,max_value=45)
dpf=st.number_input('DPF',min_value=0.0,max_value=5.0)
preg=st.number_input('Preg',min_value=0,max_value=20,value=1)
ins=st.number_input('Insulin',min_value=0,max_value=125,value=0)
skin=st.number_input('Skin Thickness',min_value=10,max_value=45)
glu=st.number_input('Glucose',min_value=60,max_value=325)
bp=st.number_input('Blood Pressure',min_value=30,max_value=220)

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
print(algo)

if(st.button('Submit')):
    print("ff")