import streamlit as st
import pandas as pd
from src.App import App

app = App()

uploaded_file = st.file_uploader("Choose a file")


if uploaded_file:
    app.valida_arquivo(uploaded_file)

    