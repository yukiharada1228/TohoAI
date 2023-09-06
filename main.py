import os
import requests
import streamlit as st
from streamlit_chat import message


st.title("TOHO AI")
if "generated" not in st.session_state:
    st.session_state.generated = []
if "past" not in st.session_state:
    st.session_state.past = []
with st.form("質問する"):
    user_message = st.text_area("AirCodeについての質問を入力してください")
    submitted = st.form_submit_button("質問する")
    if submitted:
        # Define the API endpoint URL
        api_endpoint = os.getenv("API_ENDPOINT")

        # Create a JSON request payload
        payload = {"question": user_message}

        # Make an HTTP POST request to the API
        response = requests.post(api_endpoint, json=payload)

        if response.status_code == 200:
            answer = response.json()["response"]
            st.session_state.past.append(user_message)
            st.session_state.generated.append(answer)
            
            if st.session_state["generated"]:
                for i in range(len(st.session_state.generated) - 1, -1, -1):
                    message(
                        st.session_state.generated[i], key=str(i), avatar_style="thumbs"
                    )
                    message(
                        st.session_state.past[i],
                        is_user=True,
                        key=str(i) + "_user",
                        avatar_style="avataaars",
                    )
