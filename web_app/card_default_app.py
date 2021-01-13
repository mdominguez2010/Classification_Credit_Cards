import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.ensemble import RandomForestClassifier

st.write('''
# Credit Card Default: A Demonstration
## By Marcos Dominguez, Data Scientist
''')

# Read Pickle and assign once again to variable shoes_list
with open('rf_rev.pickle','rb') as read_file:
    rf_rev = pickle.load(read_file)

# Read scaler
with open('scaler.pickle','rb') as read_file:
    scaler = pickle.load(read_file)

st.write(
'''
## Choose Monthly Status to Make a Prediction
'''
)

# User Inputs
#credit_limit = st.slider('Credit Limit', min_value=0, max_value=150000)
#credit_limit = st.selectbox('Credit Limit', ('$10,000','$50,000','$100,000'))

def to_digit(selection):

    """
    Takes a select_slider selection and converts it to it's corresponding digit format
    """
    if selection == 'On Time':
        selection = 0
    elif selection == '1 Month Late':
        selection = 1
    elif selection == '2 Months Late':
        selection = 2
    elif selection == '3 Months Late':
        selection = 3
    elif selection == '4 Months Late':
        selection = 4
    elif selection == '5 Months Late':
        selection = 5
    elif selection == '6 Months Late':
        selection = 6
    elif selection == '7 Months Late':
        selection = 7
    elif selection == '8 Months Late':
        selection = 8
    elif selection == '9 Months Late':
        selection = 9
    elif selection == '10 Months Late':
        selection = 10
    
    return selection

jun_hist = st.select_slider('June Status',('On Time','1 Month Late','2 Months Late',
                                            '3 Months Late','4 Months Late'))
jun_hist = to_digit(jun_hist)

jul_hist = st.select_slider('July Status',('On Time','1 Month Late','2 Months Late',
                                            '3 Months Late','4 Months Late'))
jul_hist = to_digit(jul_hist)

aug_hist = st.select_slider('August Status',('On Time','1 Month Late','2 Months Late',
                                            '3 Months Late','4 Months Late'))
aug_hist = to_digit(aug_hist)

sep_hist = st.select_slider('September Status',('On Time','1 Month Late','2 Months Late',
                                            '3 Months Late','4 Months Late'))

sep_hist = to_digit(sep_hist)


# may_hist = st.select_slider('May Status',('On Time','1 Month Late','2 Months Late',
#                                             '3 Months Late','4 Months Late'))
# may_hist = to_digit(may_hist)

# apr_hist = st.select_slider('April Status',('On Time','1 Month Late','2 Months Late',
#                                             '3 Months Late','4 Months Late'))
# apr_hist = to_digit(apr_hist)

input_data = pd.DataFrame({'September History':[sep_hist],'August History':[aug_hist],
                           'July History':[jul_hist], 'Jun_Hist':jun_hist})

input_data_scaled = scaler.transform(input_data)

pred = round(rf_rev.predict_proba(input_data_scaled)[0][1] * 100,0)

predict_button = st.button('Predict')

if predict_button:
    try:
        st.write(
        f'Likelihood of Default: {pred}%'    
        )
    except Exception as e:
        st.exception("Exception: %s\n"% e)