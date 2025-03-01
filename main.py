import streamlit as st
import requests

with open("usable-metrics.txt", "r") as f:
    metric_list = [line.strip() for line in f]

st.title("Competition Starter Tool")

tab1, tab2 = st.tabs(["SOTW Competition", "BOTW Competition"])

with tab1:
    st.header("SOTW Competition")
    wom_code = st.text_input("Enter your WOM code (for SOTW):", key="wom_sotw")
    title_numb = st.text_input("What number SOTW is running this week?", key="title_sotw")
    date_start = st.text_input("What day will the competition start? (YYYY-MM-DD)", key="date_start_sotw")
    date_end = st.text_input("What day will the competition end? (YYYY-MM-DD)", key="date_end_sotw")
    metric = st.text_input("What is this week's skill? (lowercase skill name)", key="metric_sotw")
    
    if st.button("Submit SOTW", key="submit_sotw"):
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

with tab2:
    st.header("BOTW Competition")
    wom_code_botw = st.text_input("Enter your WOM code (for BOTW):", key="wom_botw")
    title_numb_botw = st.text_input("What number BOTW is running this week?", key="title_botw")
    date_start_botw = st.text_input("What day will the competition start? (YYYY-MM-DD)", key="date_start_botw")
    date_end_botw = st.text_input("What day will the competition end? (YYYY-MM-DD)", key="date_end_botw")
    metric_botw = st.text_input("What is this week's boss? (lowercase boss name)", key="metric_botw")
    
    if st.button("Submit BOTW", key="submit_botw"):
        if not wom_code_botw:
            st.error("Please enter the WOM code.")
        elif metric_botw not in metric_list:
            st.error("Please enter a usable metric (all lowercase).")
        else:
            payload = {
                "title": "Toe Beans BOTW " + title_numb_botw, 
                "metric": metric_botw, 
                "startsAt": date_start_botw + "T17:00:00.000Z", 
                "endsAt": date_end_botw + "T17:00:00.000Z", 
                "groupId": 909, 
                "groupVerificationCode": wom_code_botw
            }
            response = requests.post("https://api.wiseoldman.net/v2/competitions", json=payload)
            st.write("API Response:", response.text)
