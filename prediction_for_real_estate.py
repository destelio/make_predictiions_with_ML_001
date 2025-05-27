

import streamlit as st

import numpy as np

import joblib

from sklearn.ensemble import RandomForestRegressor
#import xgboost as xgb

model = joblib.load("model_loaded.pkl")



st.title("this is our first Real Estate predition model")


st.divider()

bed = st.number_input("Enter the number of bedrooms", value = 2, step = 1)

bath  = st.number_input("Enter the number of bathrooms", value = 2, step = 1)


pv_system_common_0 = st.number_input("Enter the number of bathrooms", value = 0, step = 1)

#st.text_input

pv_system_common_1 = st.number_input("Enter the number of bathrooms", value = 1, step = 1)


'''
if pv_system_common_0 == False:
	pv_system_common_0 = 0
else:
	pv_system_common_0 = 1


if pv_system_common_1 == True:
	pv_system_common_1 = 1
else:
	pv_system_common_1 = 0
'''

X = [bed, bath, pv_system_common_0, pv_system_common_1]

st.divider()



predictbutton = st.button("Predict!")


if predictbutton:

	X1 = np.array(X)

	#st.write(X1)


	x_small2 = X1.reshape(1, -1)

	#print(x_small2)

	#st.write(x_small2)


	prediction = model.predict(x_small2)#[0]

	st.write(prediction)

else:

	"Please use button for prediction"
