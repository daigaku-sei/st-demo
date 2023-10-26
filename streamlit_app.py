import streamlit as st
from session_state import SessionState
import requests

# Get the user's IP address
user_ip = st.request.headers.get('X-Forwarded-For', st.request.remote_ip)

# Create a SessionState object with the user's IP as the ID
session_state = SessionState.get(user_id=user_ip)

# Access the user_id
st.write(session_state.user_id)
