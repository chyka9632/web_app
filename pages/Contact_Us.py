
import streamlit as st
import pandas as pd
from send_email import send_email

with st.form(key="contact form"):
    user_email = st.text_input("Your Email Address")

    df = pd.read_csv("topics.csv")
    topic_options = st.selectbox("What topic do you want to discuss", df["topic"])

    raw_message = st.text_area("Text")
    message = f"""\
Subject: New message from {user_email}\n

From: {user_email}
Topic {topic_options}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email sent!")


