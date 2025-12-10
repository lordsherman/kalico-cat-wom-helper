import streamlit as st
import requests
import pytz
from datetime import datetime
from wom import Metric

def get_est_timestamp(date_str, hour=12):
    est = pytz.timezone('America/New_York')
    naive_dt = datetime.strptime(f"{date_str} {hour:02d}:00:00", "%Y-%m-%d %H:%M:%S")
    est_dt = est.localize(naive_dt)
    return est_dt.astimezone(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%S.000Z")

# Get all metrics from the wom.py package
metric_list = [m.value for m in Metric]

st.title("Competition Starter Tool")

tab1, tab2 = st.tabs(["SOTW Competition", "BOTW Competition"])

with tab1:
    st.header("SOTW Competition")
    st.info("All SOTW competitions start and end at 12:00 PM EST on the specified dates.")
    
    title_numb = st.text_input("What number SOTW is running this week?", key="title_sotw")
    date_start = st.date_input("What day will the competition start?", key="date_start_sotw")
    date_end = st.date_input("What day will the competition end?", key="date_end_sotw")
    metric = st.selectbox("What is this week's skill?", options=metric_list, key="metric_sotw", index=None, placeholder="Search and select a metric...")
    wom_code = st.text_input("Enter your WOM code (for SOTW):", key="wom_sotw")
    
    if st.button("Submit SOTW", key="submit_sotw"):
        if not wom_code:
            st.error("Please enter the WOM code.")
        elif not metric:
            st.error("Please select a metric.")
        else:
            payload = {
                "title": "Cat Chat SOTW " + title_numb, 
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
    metric_botw = st.selectbox("What is this week's boss?", options=metric_list, key="metric_botw", index=None, placeholder="Search and select a metric...")
    wom_code_botw = st.text_input("Enter your WOM code (for BOTW):", key="wom_botw")
    
    if st.button("Submit BOTW", key="submit_botw"):
        if not wom_code_botw:
            st.error("Please enter the WOM code.")
        elif not metric_botw:
            st.error("Please select a metric.")
        else:
            payload = {
                "title": "Cat Chat BOTW " + title_numb_botw, 
                "metric": metric_botw, 
                "startsAt": get_est_timestamp(date_start_botw.strftime("%Y-%m-%d")), 
                "endsAt": get_est_timestamp(date_end_botw.strftime("%Y-%m-%d")), 
                "groupId": 909, 
                "groupVerificationCode": wom_code_botw
            }
            response = requests.post("https://api.wiseoldman.net/v2/competitions", json=payload)
            st.write("API Response:", response.text)
