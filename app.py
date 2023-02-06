### Imports
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

###Load the datasets
ev = pd.read_csv('https://raw.githubusercontent.com/Frans-Grau/ElectricVehicleVsChargingStations/main/Datasets/WA-Final.csv')
### Preporocessing (if needed)


### Plots 
#Pie1
evcounts = ev.groupby("Make")['Model'].count().reset_index().sort_values('Model',ascending=False)
top_5 = evcounts[:5]
other = evcounts[5:].sum()
other["Make"] = "OTHER"
evcounts = top_5.append(other, ignore_index=True)
fig1 = px.pie(evcounts, values="Model", names="Make",hole=.5,title="Largest EV- Carmakers")


#Pie2 

### Layout
st.set_page_config(page_title = 'CleanMobility', layout='wide', menu_items=None)
tab1, tab2 = st.tabs(['EV - Population', 'Charging Stations'])

## Inside Page1: 'EV-Population' 
with tab1: 
    st.markdown('') ## empty space
    col1, col2, col3 = st.columns([2,0.5,2])
    with col1:
        st.subheader('Column 1, page1')
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.markdown('Column 2, page1')
    with col3:
        st.subheader('Column 3, page1')
    
    st.title('') ## big empty space
    col3, col4, col5 = st.columns([2,0.5,2])
    with col3:
        st.subheader('Column 1-row2, page1')
    with col4:
        st.markdown('Column 2-row2, page1')
    with col5:
        st.subheader('Column 3-row2, page1')



## Inside Page2: 'Charging Stations'
with tab2:
    st.markdown('') ## empty space
    col21, col22, col23 = st.columns([2,0.5,2])
    with col21:
        st.subheader('Column 1, page2')
    with col22:
        st.markdown('Column 2, page2')
    with col23:
        st.subheader('Column 3, page2')
    
    st.title('') ## big empty space
    col24, col25, col26 = st.columns([2,0.5,2])
    with col24:
        st.subheader('Column 1-row2, page2')
    with col25:
        st.markdown('Column 2-row2, page2')
    with col26:
        st.subheader('Column 3-row2, page2')
