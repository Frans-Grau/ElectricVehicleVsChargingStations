### Imports
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit_nested_layout
from streamlit_option_menu import option_menu

###Load the datasets

### Preporocessing (if needed)

### Layout
st.set_page_config(page_title = 'CleanMobility', layout='wide', menu_items=None)
tab1, tab2 = st.tabs(['EV - Population', 'Charging Stations'])

## Inside Page1: 'EV-Population' 
with tab1: 
    col1, col2, col3 = st.columns([2,0.5,2])
    with col1:
        st.markdown('Column 1, page1')
    with col2:
        st.markdown('COlumn 2, page1')
    with col3:
        st.markdown('Column 3, page1')


## Inside Page2: 'Charging Stations'
with tab2:
    col21, col22, col23 = st.columns([2,0.5,2])
    with col21:
        st.markdown('Column 1, page2')
    with col22:
        st.markdown('Column 2, page2')
    with col23:
        st.markdown('Column 3, page2')
