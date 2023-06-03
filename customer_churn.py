import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import urllib.request

pipe = pickle.load(open('customer_churn.pkl', 'rb'))

st.title('Customer Churn Predictor')

st.markdown(
    f"""
        <style>
        .stApp {{
            background-image: url("https://wallpapercave.com/wp/wp6086966.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    gender_txt = st.text_input("Customer's Gender")
    if gender_txt == 'Male' or gender_txt == 'MALE' or gender_txt == 'M':
        gender = 1
    else:
        gender = 0

with col2:
    cursor_txt = st.text_input("Senior Citizen or not")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        senior = 1
    else:
        senior = 0

with col3:
    cursor_txt = st.text_input("Has Partner or not")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        partner = 1
    else:
        partner = 0

with col4:
    cursor_txt = st.text_input("Has Dependents or not")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        dependent = 1
    else:
        dependent = 0


col5, col6, col7 = st.columns(3)
with col5:
    tenure = st.number_input("Tenure of the Customer")
with col6:
    cursor_txt = st.text_input("Internet (Fiber Optic/DSL/No Internet)")
    if cursor_txt == 'Fiber Optic':
        fiber = 1
        dhl = 0
        no = 0
    elif cursor_txt == 'DSL':
        fiber = 0
        dhl = 1
        no = 0
    else:
        fiber = 0
        dhl = 0
        no = 1
with col7:
    cursor_txt = st.text_input("Contract (Monthly/One Year/Two Year)")
    if cursor_txt == 'Monthly':
        contract_month = 1
        contract_one = 0
        contract_two = 0
    elif cursor_txt == 'One Year':
        contract_month = 0
        contract_one = 1
        contract_two = 0
    else:
        contract_month = 0
        contract_one = 0
        contract_two = 1

col8, col9 = st.columns(2)
with col8:
    cursor_txt = st.text_input("Phone Service (Yes/No)")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        ps = 1
    else:
        ps = 0
with col9:
    cursor_txt = st.text_input("Has Multiple ph. lines or not")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        mpl = 1
    else:
        mpl = 0

col10, col11, col12, col13 = st.columns(4)
with col10:
    cursor_txt = st.text_input("Online Security (Yes/No)")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        os = 1
    else:
        os = 0
with col11:
    cursor_txt = st.text_input("Online Backup (Yes/No)")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        ob = 1
    else:
        ob = 0
with col12:
    cursor_txt = st.text_input("Device Protection (Yes/No)")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        dp = 1
    else:
        dp = 0
with col13:
    cursor_txt = st.text_input("Tech Support (Yes/No)")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        ts = 1
    else:
        ts = 0

col14, col15 = st.columns(2)
with col14:
    cursor_txt = st.text_input("Streams TV or not")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        stv = 1
    else:
        stv = 0
with col15:
    cursor_txt = st.text_input("Streams movies or not")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        sm = 1
    else:
        sm = 0

col16, col17 = st.columns(2)
with col16:
    cursor_txt = st.text_input("Paperless Billing (Yes/No)")
    if cursor_txt == 'Yes' or cursor_txt == 'YES' or cursor_txt == 'Y' or cursor_txt == 'yes':
        pb = 1
    else:
        pb = 0
with col17:
    monthly_chrg = st.number_input("Monthly Charges")


ec = 0
mc = 0
bt = 0
cc = 0
cursor_txt = st.text_input("Payment Method (Electronic Check/Mailed Check/Bank Transfer/Credit Card")
if cursor_txt == 'Electronic Check':
    ec = 1
    mc = 0
    bt = 0
    cc = 0
if cursor_txt == 'Mailed Check':
    ec = 0
    mc = 1
    bt = 0
    cc = 0
if cursor_txt == 'Bank Transfer':
    ec = 0
    mc = 0
    bt = 1
    cc = 0
if cursor_txt == 'Credit Card':
    ec = 0
    mc = 0
    bt = 0
    cc = 1

total_chrg = 0
if contract_month == 1:
    total_chrg = monthly_chrg
elif contract_one == 1:
    total_chrg = 12*monthly_chrg
elif contract_two == 1:
    total_chrg = 24*monthly_chrg

if st.button('Get Prediction about the Customer'):

    input_df = pd.DataFrame(
     {'gender': [gender], 'SeniorCitizen': [senior],'Partner': [partner], 'Dependents': [dependent], 'tenure': [tenure], 'PhoneService': [ps], 'MultipleLines': [mpl], 'OnlineSecurity': [os], 'OnlineBackup': [ob],'DeviceProtection': [dp], 'TechSupport': [ts], 'StreamingTV': [stv], 'StreamingMovies': [sm], 'PaperlessBilling': [pb], 'MonthlyCharges': [monthly_chrg], 'TotalCharges': [total_chrg], 'DSL': [dhl], 'Fiber optic': [fiber], 'No': [no], 'Month-to-month': [contract_month], 'One year': [contract_one], 'Two year': [contract_two], 'Bank transfer (automatic)': [bt], 'Credit card (automatic)': [cc], 'Electronic check': [ec], 'Mailed check': [mc]})
    result = pipe.predict(input_df)
    if result==1:
        urllib.request.urlretrieve('https://i.imgur.com/b3rBEqp.png', "churner.png")
        image = Image.open("churner.png")
        new_image = image.resize((70, 70))
        col18, mid, col19 = st.columns([35, 1, 20])
        with col18:
            st.header("This Customer is a Churner")
        with col19:
            st.image(new_image)
    else:
        urllib.request.urlretrieve('https://i.imgur.com/sh2mX7S.png', "non_churner.png")
        image = Image.open("non_churner.png")
        new_image = image.resize((70, 70))
        col20, mid, col21 = st.columns([45, 1, 20])
        with col20:
            st.header("This Customer is not a Churner")
        with col21:
            st.image(new_image)
  
      
    ques = ["Who are you?", "What is your name?", "Where do you live?"]
            
    st.write("\nCheck your preparation by answering the following questions!")
    if st.button("Solve the questions"):
            for i in range(len(ques)):
                st.write(ques[i])
                st.text_area("Write your answer")
