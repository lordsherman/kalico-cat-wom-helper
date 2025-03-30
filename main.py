import streamlit as st
import requests
import pytz
from datetime import datetime

def get_est_timestamp(date_str, hour=12):
    est = pytz.timezone('America/New_York')
    naive_dt = datetime.strptime(f"{date_str} {hour:02d}:00:00", "%Y-%m-%d %H:%M:%S")
    est_dt = est.localize(naive_dt)
    return est_dt.astimezone(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%S.000Z")

with open("usable-metrics.txt", "r") as f:
    metric_list = [line.strip() for line in f]

st.title("Competition Starter Tool")

tab1, tab2 = st.tabs(["SOTW Competition", "BOTW Competition"])

with tab1:
    st.header("SOTW Competition")
    st.info("All SOTW competitions start and end at 12:00 PM EST on the specified dates.")
    
    title_numb = st.text_input("What number SOTW is running this week?", key="title_sotw")
    date_start = st.date_input("What day will the competition start?", key="date_start_sotw")
    date_end = st.date_input("What day will the competition end?", key="date_end_sotw")
    metric = st.text_input("What is this week's skill? (lowercase skill name)", key="metric_sotw")
    wom_code = st.text_input("Enter your WOM code (for SOTW):", key="wom_sotw")
    
    if st.button("Submit SOTW", key="submit_sotw"):
        if not wom_code:
            st.error("Please enter the WOM code.")
        elif metric not in metric_list:
            st.error("Please enter a usable metric (all lowercase).")
        else:
            payload = {
                "title": "Toe Beans SOTW " + title_numb, 
                "metric": metric, 
                "startsAt": get_est_timestamp(date_start.strftime("%Y-%m-%d")), 
                "endsAt": get_est_timestamp(date_end.strftime("%Y-%m-%d")), 
                "groupId": 909, 
                "groupVerificationCode": wom_code
            }
            response = requests.post("https://api.wiseoldman.net/v2/competitions", json=payload)
            st.write("API Response:", response.text)

with tab2:
    st.header("BOTW Competition")
    st.info("All BOTW competitions start and end at 12:00 PM EST on the specified dates.")
    
    title_numb_botw = st.text_input("What number BOTW is running this week?", key="title_botw")
    date_start_botw = st.date_input("What day will the competition start?", key="date_start_botw")
    date_end_botw = st.date_input("What day will the competition end?", key="date_end_botw")
    metric_botw = st.text_input("What is this week's boss? (lowercase boss name)", key="metric_botw")
    wom_code_botw = st.text_input("Enter your WOM code (for BOTW):", key="wom_botw")
    
    if st.button("Submit BOTW", key="submit_botw"):
        if not wom_code_botw:
            st.error("Please enter the WOM code.")
        elif metric_botw not in metric_list:
            st.error("Please enter a usable metric (all lowercase).")
        else:
            payload = {
                "title": "Toe Beans BOTW " + title_numb_botw, 
                "metric": metric_botw, 
                "startsAt": get_est_timestamp(date_start_botw.strftime("%Y-%m-%d")), 
                "endsAt": get_est_timestamp(date_end_botw.strftime("%Y-%m-%d")), 
                "groupId": 909, 
                "groupVerificationCode": wom_code_botw
            }
            response = requests.post("https://api.wiseoldman.net/v2/competitions", json=payload)
            st.write("API Response:", response.text)
