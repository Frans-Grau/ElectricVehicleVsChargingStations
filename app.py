### Imports
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import plotly
import plotly.express as px

###Load the datasets
ev = pd.read_csv('https://raw.githubusercontent.com/Frans-Grau/ElectricVehicleVsChargingStations/main/Datasets/WA-Final.csv')
cs = pd.read_csv('https://raw.githubusercontent.com/Frans-Grau/ElectricVehicleVsChargingStations/main/Datasets/Cstations2.csv', low_memory=False)

### Preporocessing (if needed)
# Split the coordinates column into longitude and latitude
ev[['longitude', 'latitude']] = ev['Vehicle Location'].str.extract(r'POINT \((-?\d+\.\d+) (-?\d+\.\d+)\)')
# Convert longitude and latitude to numeric
ev[['longitude', 'latitude']] = ev[['longitude', 'latitude']].astype(float)

##Cs name changes
cs.loc[cs['Facility Type'] == 'FUEL_RESELLER', 'Facility Type'] = 'GAS_STATION'
cs.loc[cs['Facility Type'] == 'GROCERY', 'Facility Type'] = 'CONVENIENCE_STORE'
cs.loc[cs['EV Network'] == 'Tesla Destination', 'EV Network'] = 'Tesla'
cs.loc[cs['EV Network'] == 'ChargePoint Network', 'EV Network'] = 'ChargePoint'
to_keep= ['Tesla','ChargePoint','Non-Networked','SemaCharge Network']
cs['EV Network1'] = cs['EV Network'].where(cs['EV Network'].isin(to_keep), 'Other')

### Plots 
#Pie1
evcounts = ev.groupby("Make")['Model'].count().reset_index().sort_values('Model',ascending=False)
top_5 = evcounts[:5]
other = evcounts[5:].sum().to_frame().T
other["Make"] = "OTHER"
evcounts = pd.concat([top_5,other], ignore_index=True)
fig1 = px.pie(evcounts, values="Model", names="Make",hole=.5)

#Bar2
grapescore = ev.groupby('Model')['Make'].count().sort_values(ascending=False)
fig2 = px.bar(grapescore[:10], y=grapescore.index[:10], x=grapescore.values[:10],labels=dict(x="", y=""))
fig2.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")
#Pie2
df1 = ev['Electric Vehicle Type'].value_counts()
fig3 = px.pie(ev, values=df1.values, names=df1.index,hole=.5)

#Map4
fig4 = px.scatter_mapbox(ev, lat="latitude", lon="longitude", hover_name="City",
                        color_discrete_sequence=["blue"], zoom=5, height=400)
fig4.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})

##Bar5
cs2 = cs.groupby(['Facility Type',"EV Network1"])['City'].count().reset_index().sort_values(by='City', ascending=False)
to_keep1 = ['CONVENIENCE_STORE','HOTEL','CAR_DEALER','GAS_STATION','MUNI_GOV','OFFICE_BLDG','FED_GOV']
cs2 = cs2[cs2['Facility Type'].isin(to_keep1)]
fig5 = px.bar(cs2, y=cs2['City'], x=cs2['Facility Type'], color=cs2['EV Network1'],labels=dict(x="", y=""))
fig5.update_yaxes(title_text='Chargers')
fig5.update_layout(legend_title_text='EV Network',paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")

##Pie6
cscounts = cs.groupby("EV Network1")['State'].count().reset_index().sort_values('State',ascending=False)
fig6 = px.pie(cscounts, values="State", names="EV Network1",hole=.5)


##Map7
fig7 = px.scatter_mapbox(cs, lat="Latitude", lon="Longitude", hover_name="City",
                        color_discrete_sequence=["blue"], zoom=3, height=400)
fig7.update_layout(mapbox_style="open-street-map",margin={"r":0,"t":0,"l":0,"b":0})

##Bar8
cs1 = cs.groupby(['State',"EV Network1"])['City'].count().reset_index().sort_values(by='City', ascending=False)
top5 = ['CA','TX','NY','FL','MA','GA','WA']
cs1 = cs1[cs1['State'].isin(top5)].sort_values(by='City',ascending=False)
fig8 = px.bar(cs1, y=cs1['City'], x=cs1['State'], color=cs1['EV Network1'],labels=dict(x="", y=""))
fig8.update_yaxes(title_text='Chargers')
fig8.update_layout(legend_title_text='EV Network',paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")
##Pie9
to_keep3= ['WA']
cs['State1'] = cs['State'].where(cs['State'].isin(to_keep3), 'U.S')
cscounts = cs.groupby("State1")['State'].count().reset_index().sort_values('State',ascending=False)
fig9 = px.pie(cscounts, values="State", names="State1",hole=.5)

##Map10 -11
cswa= cs[cs['State']=='WA']
fig10 = px.scatter_mapbox(cswa, lat="Latitude", lon="Longitude", hover_name="City",
                        color_discrete_sequence=["red"], zoom=5, height=250)
fig10.update_layout(mapbox_style="open-street-map",margin={"r":0,"t":0,"l":0,"b":0})

fig11 = px.scatter_mapbox(ev, lat="latitude", lon="longitude", hover_name="City",
                        color_discrete_sequence=["blue"], zoom=5, height=250)
fig11.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})

### Layout
st.set_page_config(page_title = 'CleanMobility', layout='wide', menu_items=None)
tab1, tab2, tab3 = st.tabs(['EV - Population', 'Charging Stations', 'Washington Vs USA'])

## Inside Page1: 'EV-Population' 
with tab1:
    st.header('EV in Washington State - USA')
    # st.markdown('') ## empty space
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
        st.subheader('Charging Stations location')
        st.plotly_chart(fig5, use_container_width=True)
    with col22:
        st.markdown('')
    with col23:
        st.subheader('EV Network biggest players')
        st.plotly_chart(fig6, use_container_width=True)
    
    st.title('') ## big empty space
    # st.plotly_chart(fig7, use_container_width=True)
    col24, col25, col26 = st.columns([2,0.5,2])
    with col24:
        st.subheader('States holding the most charging stations')
        st.plotly_chart(fig8, use_container_width=True)
    with col25:
        st.markdown('')
    with col26:
        st.subheader('Charging stations across the U.S')
        st.plotly_chart(fig7,use_container_width=True)


## Inside Page3: 'WA VS US'
with tab3:
    st.markdown('')
    col31, col32, col33 = st.columns([2,0.5,2])
    with col31:
        st.subheader('Charging Stations in Washington')
        st.plotly_chart(fig10, use_container_width=True)
    with col32:
        st.markdown('')
    with col33:
        st.subheader('EVs in Washington')
        st.plotly_chart(fig11, use_container_width=True)
        
    col34, col35, col36 = st.columns([2,0.5,2])
    with col34:
        st.subheader('Washington Vs U.S')
        st.plotly_chart(fig9, use_container_width=True)
    with col35:
        st.markdown('')
    with col36:
        st.subheader('Takeaway')
        # st.plotly_chart(fig7,use_container_width=True)