import streamlit as st
import requests

with open("usable-metrics.txt", "r") as f:
    metric_list = [line.strip() for line in f]

st.title("Competition Starter Tool")

title_numb = st.text_input("What number SOTW is running this week?")
date_start = st.text_input("What day will the competition start? (YYYY-MM-DD)")
date_end = st.text_input("What day will the competition end? (YYYY-MM-DD)")
metric = st.text_input("What is this week's skill? (lowercase skill name)")
wom_code = st.text_input("Enter your group verification code (WOM):")

if st.button("Submit"):
    if not wom_code:
        st.error("Please enter the WOM code.")
    elif metric not in metric_list:
        st.error("Please enter a usable metric (all lowercase).")
    else:
        payload = {
            "title": "Kalico Cat SOTW " + title_numb, 
            "metric": metric, 
            "startsAt": date_start + "T16:00:00.000Z", 
            "endsAt": date_end + "T16:00:00.000Z", 
            "groupId": 909, 
            "groupVerificationCode": wom_code
        }
        response = requests.post("https://api.wiseoldman.net/v2/competitions", json=payload)
        st.write("API Response:", response.text)
