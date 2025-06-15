import streamlit as st
from send_email import send_email

st.header("Contact Us ")

with st.form(key='form'):
    user_email = st.text_input('your email address')
    raw_message =  st.text_area('enter your message')
    message = f"""\
    Subject: New mail 
    
    From: {user_email}
    {raw_message}
    
"""
    button = st.form_submit_button('submit')
    if button:
        send_email(message)
        st.info('Email sent successfully')