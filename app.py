### Imports
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

###Load the datasets
ev = pd.read_csv('https://raw.githubusercontent.com/Frans-Grau/ElectricVehicleVsChargingStations/main/Datasets/WA-Final.csv')
cs = pd.read_csv('https://raw.githubusercontent.com/Frans-Grau/ElectricVehicleVsChargingStations/main/Datasets/Cstations2.csv')

### Preporocessing (if needed)
# Split the coordinates column into longitude and latitude
ev[['longitude', 'latitude']] = ev['Vehicle Location'].str.extract(r'POINT \((-?\d+\.\d+) (-?\d+\.\d+)\)')
# Convert longitude and latitude to numeric
ev[['longitude', 'latitude']] = ev[['longitude', 'latitude']].astype(float)

### Plots 
#Pie1
evcounts = ev.groupby("Make")['Model'].count().reset_index().sort_values('Model',ascending=False)
top_5 = evcounts[:5]
other = evcounts[5:].sum()
other["Make"] = "OTHER"
evcounts = top_5.append(other, ignore_index=True)
fig1 = px.pie(evcounts, values="Model", names="Make",hole=.5)

#Bar2
grapescore = ev.groupby('Model')['Make'].count().sort_values(ascending=False)
fig2 = px.bar(grapescore[:10], y=grapescore.index[:10], x=grapescore.values[:10],labels=dict(x="", y=""))
fig2.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")
#pie2
df1 = ev['Electric Vehicle Type'].value_counts()
fig3 = px.pie(ev, values=df1.values, names=df1.index,hole=.5)

#Map4
fig4 = px.scatter_mapbox(ev, lat="latitude", lon="longitude", hover_name="City",
                        color_discrete_sequence=["blue"], zoom=5, height=300)
fig4.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})

### Layout
st.set_page_config(page_title = 'CleanMobility', layout='wide', menu_items=None)
tab1, tab2 = st.tabs(['EV - Population', 'Charging Stations'])

## Inside Page1: 'EV-Population' 
with tab1: 
    st.markdown('') ## empty space
    col1, col2, col3 = st.columns([2,0.5,2])
    with col1:
        st.subheader('Largest EV- Carmakers')
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.markdown('')
    with col3:
        st.subheader('Popular Models')
        st.plotly_chart(fig2, use_container_width=True)
    
    st.title('') ## big empty space
    col3, col4, col5 = st.columns([2,0.5,2])
    with col3:
        st.subheader('EV - Types')
        st.plotly_chart(fig3, use_container_width=True)
    with col4:
        st.markdown('')
    with col5:
        st.subheader('Where are EVs located?')
        st.plotly_chart(fig4, use_container_width=True)



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
