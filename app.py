import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import numpy as np
import os
import base64
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from view import home
from view import predict

warnings.filterwarnings("ignore")

# streamlit run .\dashboard.py --server.port 8888

st.set_page_config(page_title="Dashboard Bonbon Ice Cream", page_icon="img/bonbon.png", layout="wide")

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("img/bg.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:background/png;base64,{img}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    # Menambahkan styling CSS untuk mengganti warna background sidebar dan option menu
    st.markdown(
        """
        <style>
        /* Ganti warna background sidebar */
        .edtmxes8 {  /* Sidebar Streamlit */
            background-color: #EC0A0B !important;  
        }
        
        .e14ksaui0 {
            background-color: #EC0A0B !important;  
        }

        .e14ksaui0 a:hover{
            background-color: #ffffff !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # Sidebar content
    st.sidebar.image("img/bonbon.png", caption="")
    st.sidebar.title("Selamat Datang!")

    # Sidebar menu with option_menu
    with st.sidebar:
        page = option_menu("Main Menu",
                                ["Home", "Model Clusters"],
                                icons=["house", "search"], default_index=0,
                                styles={
                                    "menu-title":{
                                        "color":"#EC0A0B"
                                    },
                                    "container": {
                                        "padding": "5!important",
                                        "background-color": "#FFFFFFFF"},
                                    "nav-link": {
                                        "font-size": "16px", 
                                        "text-align": "left", 
                                        "margin": "5px",
                                        "--hover-color": "#FDD776",
                                        "border": "2px solid #EC0A0B",
                                        "color":"#EC0A0B"
                                    },
                                    "nav-link-selected": {
                                        "background-color":"#ffffff"}
                                })
            
    # Conditional page rendering
    if page == "Home":
        home.main()
    # elif page == "Details":
    #     predict.main()

if __name__ == '__main__':
    main()