import streamlit as st
import json

with(open('ocr_data.json')) as f:
    data = json.load(f)

st.write('')

