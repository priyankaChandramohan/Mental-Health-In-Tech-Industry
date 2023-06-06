import numpy as np
import pandas as pd
from sklearn import datasets
import pickle
import plotly.express as px
import streamlit as st
import warnings
warnings.filterwarnings('ignore')


loaded_model = pickle.load(open('C:/Users/ankit/OneDrive/Desktop/streamlit_dashboard/mental_model.pkl'
                                , 'rb'))

def mental_health(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0]==0):
        return st.success('This person does not need treatment')
    else:
        return st.error('This person needs treatment')

def main():

    st.title('Mental Health in Tech Industry')

    age = st.text_input('Age of the Employee')
    gender = st.text_input('Gender of the Employee')
    family_history = st.text_input('family history of the mental problems')
    work_interfere = st.text_input('is your work getting affecting due to mental problems')
    no_employee = st.text_input('Number of employees in the company')
    benefits = st.text_input('Is your company giving benefits')
    care_options = st.text_input('Is your company having care_options')
    wellness_program = st.text_input('are you in any wellness program')
    anonymity = st.text_input('Anonymity: ')
    leave = st.text_input('does leave helps in mental problems')
    mental_health_consequence = st.text_input('mental health consequence: ')
    phys_health_consequence	= st.text_input('physical health consequence: ')
    coworkers = st.text_input('are co-workers helpful: ')

    if st.button('Mental Health Test Result'):
        diagnosis = mental_health(
            [age,gender,family_history,work_interfere,no_employee,benefits,care_options,wellness_program,anonymity,leave,mental_health_consequence,phys_health_consequence,coworkers])


if __name__ == '__main__':
    main()