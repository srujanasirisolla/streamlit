import streamlit as st
import joblib
st.title('Loan Approval Process Automation')
model=(joblib.load('c:/models/loan.joblib')
Gender=st.number_input('Enter gender Male:0 Female:1')
Married=st.number_input('Enter martial status Married:1 Unmarried:0')
income=st.number_input('Enter applicant income in thousands')
la=st.number_input('Enter loan amount in thousands')
if st.button('predict Approval'):
    predictions=model.predict([[Gender,Married,income,la]])
       if predictions=='y':
           st.text('loan approved')
       else:
           st.text('loan rejected')
           
       
       
       
